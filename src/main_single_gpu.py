import os
import time
import argparse
import shutil
import numpy as np

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim
import torch.utils.data

import video_transforms
import models
import datasets

model_names = sorted(name for name in models.__dict__
    if name.islower() and not name.startswith("__")
    and callable(models.__dict__[name]))

dataset_names = sorted(name for name in datasets.__all__)

parser = argparse.ArgumentParser(description='PyTorch Two-Stream Action Recognition')
parser.add_argument('data', metavar='DIR',
                    help='path to dataset')
parser.add_argument('--settings', metavar='DIR', default='./datasets/settings',
                    help='path to datset setting files')
parser.add_argument('--modality', '-m', metavar='MODALITY', default='rgb',
                    choices=["rgb", "flow"],
                    help='modality: rgb | flow')
parser.add_argument('--dataset', '-d', default='ucf101',
                    choices=["ucf101", "hmdb51"],
                    help='dataset: ucf101 | hmdb51')
parser.add_argument('--arch', '-a', metavar='ARCH', default='rgb_resnet152',
                    choices=model_names,
                    help='model architecture: ' +
                        ' | '.join(model_names) +
                        ' (default: rgb_vgg16)')
parser.add_argument('-s', '--split', default=1, type=int, metavar='S',
                    help='which split of data to work on (default: 1)')
parser.add_argument('-j', '--workers', default=4, type=int, metavar='N',
                    help='number of data loading workers (default: 4)')
parser.add_argument('--epochs', default=250, type=int, metavar='N',
                    help='number of total epochs to run')
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
                    help='manual epoch number (useful on restarts)')
parser.add_argument('-b', '--batch-size', default=25, type=int,
                    metavar='N', help='mini-batch size (default: 50)')
parser.add_argument('--iter-size', default=5, type=int,
                    metavar='I', help='iter size as in Caffe to reduce memory usage (default: 5)')
parser.add_argument('--new_length', default=1, type=int,
                    metavar='N', help='length of sampled video frames (default: 1)')
parser.add_argument('--new_width', default=340, type=int,
                    metavar='N', help='resize width (default: 340)')
parser.add_argument('--new_height', default=256, type=int,
                    metavar='N', help='resize height (default: 256)')
parser.add_argument('--lr', '--learning-rate', default=0.001, type=float,
                    metavar='LR', help='initial learning rate')
parser.add_argument('--lr_steps', default=[100, 200], type=float, nargs="+",
                    metavar='LRSteps', help='epochs to decay learning rate by 10')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='momentum')
parser.add_argument('--weight-decay', '--wd', default=5e-4, type=float,
                    metavar='W', help='weight decay (default: 5e-4)')
parser.add_argument('--print-freq', default=50, type=int,
                    metavar='N', help='print frequency (default: 50)')
parser.add_argument('--save-freq', default=25, type=int,
                    metavar='N', help='save frequency (default: 25)')
parser.add_argument('--resume', default='./checkpoints', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')

best_prec1 = 0
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

def main():
    global args, best_prec1
    args = parser.parse_args()
    global resume
    resume = args.resume
    global demo
    demo = args.demo
    # create model
    print("Building model ... ")
    model = build_model()
    print("Model %s is loaded. " % (args.arch))

    # define loss function (criterion) and optimizer
    criterion = nn.CrossEntropyLoss().cuda()

    optimizer = torch.optim.SGD(model.parameters(), args.lr,
                                momentum=args.momentum,
                                weight_decay=args.weight_decay)


    if not os.path.exists(args.resume):
        os.makedirs(args.resume)
    print("Saving everything to directory %s." % (args.resume))

    cudnn.benchmark = True

    # Data transforming
    if args.modality == "rgb":
        is_color = True
        scale_ratios = [1.0, 0.875, 0.75, 0.66]
        clip_mean = [0.485, 0.456, 0.406] * args.new_length
        clip_std = [0.229, 0.224, 0.225] * args.new_length
    elif args.modality == "flow":
        is_color = False
        scale_ratios = [1.0, 0.875, 0.75]
        clip_mean = [0.5, 0.5] * args.new_length
        clip_std = [0.226, 0.226] * args.new_length
    else:
        print("No such modality. Only rgb and flow supported.")

    normalize = video_transforms.Normalize(mean=clip_mean,
                                           std=clip_std)
    train_transform = video_transforms.Compose([
            # video_transforms.Scale((256)),
            video_transforms.MultiScaleCrop((224, 224), scale_ratios),
            video_transforms.RandomHorizontalFlip(),
            video_transforms.ToTensor(),
            normalize,
        ])

    val_transform = video_transforms.Compose([
            # video_transforms.Scale((256)),
            video_transforms.CenterCrop((224)),
            video_transforms.ToTensor(),
            normalize,
        ])

    # data loading
    train_setting_file = "train_%s_split%d.txt" % (args.modality, args.split)
    train_split_file = os.path.join(args.settings, args.dataset, train_setting_file)
    val_setting_file = "val_%s_split%d.txt" % (args.modality, args.split)
    val_split_file = os.path.join(args.settings, args.dataset, val_setting_file)
    if not os.path.exists(train_split_file) or not os.path.exists(val_split_file):
        print("No split file exists in %s directory. Preprocess the dataset first" % (args.settings))

    train_dataset = datasets.__dict__[args.dataset](root=args.data,
                                                    source=train_split_file,
                                                    phase="train",
                                                    modality=args.modality,
                                                    is_color=is_color,
                                                    new_length=args.new_length,
                                                    new_width=args.new_width,
                                                    new_height=args.new_height,
                                                    video_transform=train_transform)
    val_dataset = datasets.__dict__[args.dataset](root=args.data,
                                                  source=val_split_file,
                                                  phase="val",
                                                  modality=args.modality,
                                                  is_color=is_color,
                                                  new_length=args.new_length,
                                                  new_width=args.new_width,
                                                  new_height=args.new_height,
                                                  video_transform=val_transform)

    print('{} samples found, {} train samples and {} test samples.'.format(len(val_dataset)+len(train_dataset),
                                                                           len(train_dataset),
                                                                           len(val_dataset)))

    train_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=args.batch_size, shuffle=True,
        num_workers=args.workers, pin_memory=True)
    val_loader = torch.utils.data.DataLoader(
        val_dataset,
        batch_size=args.batch_size, shuffle=True,
        num_workers=args.workers, pin_memory=True)

    if args.evaluate:
        validate(val_loader, model, criterion)
        return

    for epoch in range(args.start_epoch, args.epochs):
        adjust_learning_rate(optimizer, epoch)

        # train for one epoch
        train(train_loader, model, criterion, optimizer, epoch)

        # evaluate on validation set
        prec1 = 0.0
        if (epoch + 1) % args.save_freq == 0:
            prec1 = validate(val_loader, model, criterion)

        # remember best prec@1 and save checkpoint
        is_best = prec1 > best_prec1
        best_prec1 = max(prec1, best_prec1)

        if (epoch + 1) % args.save_freq == 0:
            checkpoint_name = "%03d_%s" % (epoch + 1, "checkpoint.pth.tar")
            save_checkpoint({
                'epoch': epoch + 1,
                'arch': args.arch,
                'state_dict': model.state_dict(),
                'best_prec1': best_prec1,
                'optimizer' : optimizer.state_dict(),
            }, is_best, checkpoint_name, args.resume)

def build_model():

    model = models.__dict__[args.arch](pretrained=True, num_classes=101)
    model.cuda()
    return model

def resume_and_evaluate(param_optimizer):
    model = build_model()
    optimizer = param_optimizer
    if resume:
        if os.path.isfile(resume):

            print("==> loading checkpoint '{}'".format(resume))
            checkpoint = torch.load(resume)
            start_epoch = checkpoint['epoch']
            best_prec1 = checkpoint['best_prec1']
            model.load_state_dict(checkpoint['state_dict'])
            optimizer.load_state_dict(checkpoint['optimizer'])
        else:
            print("==> no checkpoint found at '{}'".format(resume))

def resume_and_evaluate(param_optimizer):
    model = build_model()
    optimizer = param_optimizer
    if resume:
        if os.path.isfile(resume):

            print("==> loading checkpoint '{}'".format(resume))
            checkpoint = torch.load(resume)
            start_epoch = checkpoint['epoch']
            best_prec1 = checkpoint['best_prec1']
            model.load_state_dict(checkpoint['state_dict'])
            optimizer.load_state_dict(checkpoint['optimizer'])
        else:
            print("==> no checkpoint found at '{}'".format(resume))

    if demo:
        model.eval()
        #         flow_test(model)
        rgb_test(model)

    def rgb_test(param_model):
        model = param_model
        frame_count = 0
        clip_mean = [0.485, 0.456, 0.406] * args.new_length
        clip_std = [0.229, 0.224, 0.225] * args.new_length

        normalize = video_transforms.Normalize(mean=clip_mean,
                                               std=clip_std)
        # config the transform to match the network's format
        transform = video_transforms.Compose([
            # video_transforms.Scale((256)),
            video_transforms.CenterCrop((224)),
            video_transforms.ToTensor(),
            normalize,
        ])
        # config the transform to match the network's format
        #     transform = transforms.Compose([
        #             transforms.Resize((342, 256)),
        #             transforms.RandomCrop(224),
        #             transforms.ToTensor(),
        #             transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

        # prepare the translation dictionary label-action
        data_handler = UCF101_splitter(os.getcwd() + '/datasets/ucf101_splits/', None)
        data_handler.get_action_index()
        class_to_idx = data_handler.action_label
        print("hi")
        print(class_to_idx)
        idx_to_class = {v: k for k, v in class_to_idx.items()}

        # Start looping on frames received from webcam
        vs = cv2.VideoCapture("haha.avi")
        softmax = torch.nn.Softmax()
        nn_output = torch.tensor(np.zeros((1, 23)), dtype=torch.float32).cuda()
        sampled_list = []
        while True:
            # read each frame and prepare it for feedforward in nn (resize and type)
            ret, orig_frame = vs.read()
            orig_frame = cv2.resize(orig_frame, (340, 256), interpolation=cv2.INTER_LINEAR)
            if ret is False:
                break

            frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2RGB)

            sampled_list.append(frame)
            clip_input = np.concatenate(sampled_list, axis=2)
            #         frame = Image.fromarray(frame)
            frame = transform(frame).view(1, 3, 224, 224).cuda()
            frame = frame.float().cuda(async=True)
            # feed the frame to the neural network
            nn_output = model(frame)
            #         nn_output = softmax(nn_output)
            #         nn_output = nn_output.data.cpu().numpy()
            #         preds = nn_output.argsort()[0][-5:][::-1]
            #         pred_classes = [(idx_to_class[str(pred+1)], nn_output[0, pred]) for pred in preds]
            #         sampld_list = []
            # vote for class with 25 consecutive frames
            if frame_count % 10 == 0:
                nn_output = softmax(nn_output)
                nn_output = nn_output.data.cpu().numpy()
                preds = nn_output.argsort()[0][-5:][::-1]
                pred_classes = [(idx_to_class[str(pred + 1)], nn_output[0, pred]) for pred in preds]

                # reset the process
                nn_output = torch.tensor(np.zeros((1, 23)), dtype=torch.float32).cuda()
                sampled_list = []

            # Display the resulting frame and the classified action
            red = (0, 0, 255)
            green = (0, 255, 0)
            blue = (255, 0, 0)
            white = (255, 255, 255)
            yellow = (0, 255, 255)
            cyan = (255, 255, 0)
            magenta = (255, 0, 255)
            thickness = 2
            center_x = int(342 / 2.0)
            center_y = int(256 / 2.0)
            location = (center_x - 170, center_y + 80)
            fontScale = 1.5
            font = cv2.FONT_HERSHEY_SIMPLEX
            y0, dy = 180, 20
            for i in xrange(5):
                y = y0 + i * dy
                #             print(y)
                #             cv2.putText(orig_frame, 'sibal', location, font, fontScale, blue, thickness)
                cv2.putText(orig_frame, '{} - {:.2f}'.format(pred_classes[i][0], pred_classes[i][1]),
                            (5, y), font, 0.5, (0, 0, 255), 2)
                print('{} - {:.2f}'.format(pred_classes[i][0], pred_classes[i][1]))
            cv2.imwrite("temp/" + str(frame_count) + ".jpg", orig_frame)
            frame_count += 1

        # When everything done, release the capture
        vs.release()

def flow_test(param_model):
    model = param_model
    frame_count = 0
    clip_mean = [0.5, 0.5] * args.new_length
    clip_std = [0.226, 0.226] * args.new_length

    normalize = video_transforms.Normalize(mean=clip_mean,
                                               std=clip_std)
    # config the transform to match the network's format
    transform = video_transforms.Compose([
                # video_transforms.Scale((256)),
                video_transforms.CenterCrop((224)),
                video_transforms.ToTensor(),
                normalize,
            ])

    # prepare the translation dictionary label-action
    data_handler = UCF101_splitter(os.getcwd()+'/datasets/ucf101_splits/', None)
    data_handler.get_action_index()
    class_to_idx = data_handler.action_label
    print("hi")
    print(class_to_idx)
    idx_to_class = {v: k for k, v in class_to_idx.items()}

    # Start looping on frames received from webcam
    vs = cv2.VideoCapture("test.avi")
    softmax = torch.nn.Softmax()
    nn_output = torch.FloatTensor(2*10,224,224)
    count = 0
    idx = 0
    temp = ''
    x = []
    sampled_list = []
    while (vs.isOpened()):
        ret, image = vs.read()
        image = cv2.resize(image,(340, 256), interpolation=cv2.INTER_LINEAR)
        x.append(temp)
        if ret is False:
            break

        if count == 11:
            sampled_list = []
#             input_var = torch.autograd.Variable(clip_input, volatile=True)
            temp = ''
            input_var = clip_input.view(1, 20, 224, 224).cuda()
            output = model(input_var)
            output = softmax(output)
            output = output.data.cpu().numpy()
            preds = output.argsort()[0][-5:][::-1]
            pred_classes = [(idx_to_class[str(pred+1)], output[0, pred]) for pred in preds]
            for i in xrange(5):
                temp += '{} - {:.2f}\n'.format(pred_classes[i][0], pred_classes[i][1])

            print(temp)
            nn_output = torch.FloatTensor(2*10,224,224)
#             print(nn_output)
            count = 0

        if count == 0:
            old_frame = image.copy()
            prev = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
            count += 1

        else:
            next = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            flow = cv2.calcOpticalFlowFarneback(prev, next, 1, 0.5, 3, 15, 3, 5, 1.2, 0)
            horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)
            vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
            horz = horz.astype('uint8')
            vert = vert.astype('uint8')
            imgH = Image.fromarray(horz)
            imgV = Image.fromarray(vert)

#             H = transform(imgH)
#             V = transform(imgV)

            sampled_list.append(np.expand_dims(imgH, 2))
            sampled_list.append(np.expand_dims(imgV, 2))

            clip_input = np.concatenate(sampled_list, axis=2)
            clip_input = transform(clip_input)
            clip_input = clip_input.float().cuda(async=True)
#             sampled_list.append("sibal")
#             nn_output[2*(count-1),:,:] = H
#             nn_output[2*(count-1)+1,:,:] = V
            imgH.close()
            imgV.close()
            prev = next.copy()
            count += 1

        font = cv2.FONT_HERSHEY_SIMPLEX
        y0, dy = 180, 20
        for i, line in enumerate(x[idx].split('\n')):
            y = y0 + i*dy
            cv2.putText(image, line, (5, y ), font, 0.5, (0, 0, 255), 2)

        cv2.imwrite('./record/' + str(idx) + '.jpg', image)
        idx += 1

    vs.release()
def train(train_loader, model, criterion, optimizer, epoch):
    batch_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()

    # switch to train mode
    model.train()

    end = time.time()
    optimizer.zero_grad()
    loss_mini_batch = 0.0
    acc_mini_batch = 0.0

    for i, (input, target) in enumerate(train_loader):

        input = input.float().cuda(async=True)
        target = target.cuda(async=True)
        input_var = torch.autograd.Variable(input)
        target_var = torch.autograd.Variable(target)

        output = model(input_var)

        # measure accuracy and record loss
        prec1, prec3 = accuracy(output.data, target, topk=(1, 3))
        acc_mini_batch += prec1[0]
        loss = criterion(output, target_var)
        loss = loss / args.iter_size
        loss_mini_batch += loss.data[0]
        loss.backward()

        if (i+1) % args.iter_size == 0:
            # compute gradient and do SGD step
            optimizer.step()
            optimizer.zero_grad()

            # losses.update(loss_mini_batch/args.iter_size, input.size(0))
            # top1.update(acc_mini_batch/args.iter_size, input.size(0))
            losses.update(loss_mini_batch, input.size(0))
            top1.update(acc_mini_batch/args.iter_size, input.size(0))
            batch_time.update(time.time() - end)
            end = time.time()
            loss_mini_batch = 0
            acc_mini_batch = 0

            if (i+1) % args.print_freq == 0:

                print('Epoch: [{0}][{1}/{2}]\t'
                      'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                      'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                      'Prec@1 {top1.val:.3f} ({top1.avg:.3f})'.format(
                       epoch, i+1, len(train_loader)+1, batch_time=batch_time, loss=losses, top1=top1))

def validate(val_loader, model, criterion):
    batch_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()
    top3 = AverageMeter()

    # switch to evaluate mode
    model.eval()

    end = time.time()
    for i, (input, target) in enumerate(val_loader):
        input = input.float().cuda(async=True)
        target = target.cuda(async=True)
        input_var = torch.autograd.Variable(input, volatile=True)
        target_var = torch.autograd.Variable(target, volatile=True)

        # compute output
        output = model(input_var)
        loss = criterion(output, target_var)

        # measure accuracy and record loss
        prec1, prec3 = accuracy(output.data, target, topk=(1, 3))
        losses.update(loss.data[0], input.size(0))
        top1.update(prec1[0], input.size(0))
        top3.update(prec3[0], input.size(0))

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        if i % args.print_freq == 0:
            print('Test: [{0}/{1}]\t'
                  'Time {batch_time.val:.3f} ({batch_time.avg:.3f})\t'
                  'Loss {loss.val:.4f} ({loss.avg:.4f})\t'
                  'Prec@1 {top1.val:.3f} ({top1.avg:.3f})\t'
                  'Prec@3 {top3.val:.3f} ({top3.avg:.3f})'.format(
                   i, len(val_loader), batch_time=batch_time, loss=losses,
                   top1=top1, top3=top3))

    print(' * Prec@1 {top1.avg:.3f} Prec@3 {top3.avg:.3f}'
          .format(top1=top1, top3=top3))

    return top1.avg

def save_checkpoint(state, is_best, filename, resume_path):
    cur_path = os.path.join(resume_path, filename)
    best_path = os.path.join(resume_path, 'model_best.pth.tar')
    torch.save(state, cur_path)
    if is_best:
        shutil.copyfile(cur_path, best_path)

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count

def adjust_learning_rate(optimizer, epoch):
    """Sets the learning rate to the initial LR decayed by 10 every 150 epochs"""

    decay = 0.1 ** (sum(epoch >= np.array(args.lr_steps)))
    lr = args.lr * decay
    print("Current learning rate is %4.6f:" % lr)
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr

def accuracy(output, target, topk=(1,)):
    """Computes the precision@k for the specified values of k"""
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res

if __name__ == '__main__':
    main()

