import os
import time
import argparse
import shutil
import numpy as np
import cv2
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim
import torch.utils.data
import torchvision.transforms as transforms
import json
from collections import OrderedDict
import video_transforms
import models
import datasets

model_names = sorted(name for name in models.__dict__
    if name.islower() and not name.startswith("__")
    and callable(models.__dict__[name]))

dataset_names = sorted(name for name in datasets.__all__)

parser = argparse.ArgumentParser(description='PyTorch Two-Stream Action Recognition')
parser.add_argument('--resume', default='./checkpoints', type=str, metavar='PATH',
                    help='path to latest checkpoint (default: none)')
parser.add_argument('--demo', dest='demo', action='store_true', help='use model inference on video')
parser.add_argument('--label', default='smoke', type=str,
                    help='input label')
parser.add_argument('--video', default='', type=str,
                    help='input video')

best_prec1 = 0
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   
os.environ["CUDA_VISIBLE_DEVICES"]="0"

class UCF101_splitter():
    def __init__(self, path, split):
        self.path = path
        self.split = split

    def get_action_index(self):
        self.action_label={}
        with open(self.path+'classInd.txt') as f:
            content = f.readlines()
            content = [x.strip('\r\n') for x in content]
        f.close()
        for line in content:
            label,action = line.split(' ')
            #print label,action
            if action not in self.action_label.keys():
                self.action_label[action]=label

    def split_video(self):
        self.get_action_index()
        for path,subdir,files in os.walk(self.path):
            for filename in files:
                if filename.split('.')[0] == 'trainlist'+self.split:
                    train_video = self.file2_dic(self.path+filename)
                if filename.split('.')[0] == 'testlist'+self.split:
                    test_video = self.file2_dic(self.path+filename)
        self.train_video = self.name_HandstandPushups(train_video)
        self.test_video = self.name_HandstandPushups(test_video)

        return self.train_video, self.test_video

    def file2_dic(self,fname):
        with open(fname) as f:
            content = f.readlines()
            content = [x.strip('\r\n') for x in content]
        f.close()
        dic={}
        for line in content:
            #print line
            video = line.split('/',1)[1].split(' ',1)[0]
            key = video.split('_',1)[1].split('.',1)[0]
            label = self.action_label[line.split('/')[0]]   
            dic[key] = int(label)
            #print key,label
        return dic

    def name_HandstandPushups(self,dic):
        dic2 = {}
        for video in dic:
            n,g = video.split('_',1)
            if n == 'HandStandPushups':
                videoname = 'HandstandPushups_'+ g
            else:
                videoname=video
            dic2[videoname] = dic[video]
        return dic2

def main():
    global args, best_prec1
    args = parser.parse_args()
    global resume
    resume = True
    global demo
    demo = args.demo
    global label
    label = args.label
    global video
    video = args.video
    print("Building model ... ")
    flow_model = flow_build_model()
#     print("Model %s is loaded. " % (args.arch))

    # define loss function (criterion) and optimizer
    criterion = nn.CrossEntropyLoss().cuda()
    flow_optimaizer = torch.optim.SGD(flow_model.parameters(), 0.001,
                                momentum=0.9,
                                weight_decay=5e-4)
    if demo:
        resume_and_evaluate(flow_optimaizer, flow_model)
              
def flow_build_model():
    
    model = models.__dict__["flow_resnet152"](pretrained=True, num_classes= 23)
    model.cuda()
    return model

def resume_and_evaluate(flow_optimizer, flow_model):
#     model = build_model()
#     optimizer = param_optimizer
    if resume:
        flow_resume = "100_checkpoint.pth.tar"
        print("==> loading checkpoint '{}'".format(flow_resume))
        flow_checkpoint = torch.load(flow_resume)
        flow_start_epoch = flow_checkpoint['epoch']
        flow_best_prec1 = flow_checkpoint['best_prec1']
        flow_model.load_state_dict(flow_checkpoint['state_dict'])
        flow_optimizer.load_state_dict(flow_checkpoint['optimizer'])

    if demo:
        flow_model.eval()
        flow_test(flow_model)
#         rgb = rgb_test(rgb_model)
#         print(len(flow), len(rgb))

    
def flow_test(param_model):
    model = param_model
    video_list = os.listdir(video)
    f = open(video + "flow_result.txt", 'w')
    for file in video_list:
        if file.endswith("mp4"):
            f.write(file + "\n")
    #         file_data = OrderedDict()
            frame_count = 0
            clip_mean = [0.5, 0.5] * 10
            clip_std = [0.226, 0.226] * 10
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
            idx_to_class = {v: k for k, v in class_to_idx.items()}

            # Start looping on frames received from webcam
            vs = cv2.VideoCapture(video + file)
            softmax = torch.nn.Softmax()
            nn_output = torch.FloatTensor(2*10,224,224)
            count = 0
            idx = 0
            temp = ''
            x = []
            sampled_list = []
            while (vs.isOpened()):
                ret, image = vs.read()
                if ret is False:
                    break
                else:
                    image = cv2.resize(image,(342, 256), interpolation=cv2.INTER_LINEAR)
                    x.append(temp)
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
                        value = 0
                        for i in range(5):
                            if pred_classes[i][0] == label:
                                value = pred_classes[i][1]

                            temp += '{} - {:.2f}\n'.format(pred_classes[i][0], pred_classes[i][1])
                        f.write(str(value) + "\n")
                        nn_output = torch.FloatTensor(2*10,224,224)
                        count = 1

                    if count == 0:
                        old_frame = image.copy()
                        prev = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

                    else:
                        next = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        flow = cv2.calcOpticalFlowFarneback(prev, next, 1, 0.5, 3, 15, 3, 5, 1.2, 0)
                        horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)
                        vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
                        horz = horz.astype('uint8')
                        vert = vert.astype('uint8')
                        imgH = Image.fromarray(horz)
                        imgV = Image.fromarray(vert)

                        sampled_list.append(np.expand_dims(imgH, 2))
                        sampled_list.append(np.expand_dims(imgV, 2))

                        clip_input = np.concatenate(sampled_list, axis=2)
                        clip_input = transform(clip_input)
                        clip_input = clip_input.float().cuda(async=True)
                        imgH.close()
                        imgV.close()
                        prev = next.copy()

                    count += 1
                    idx += 1
            f.write("----\n")
    #         file_data[file] = flow_value
    #         with open('flow.json', 'w', encoding="utf-8") as make_file:
    #             json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
            print(idx)
            vs.release()
        
    f.close()    

if __name__ == '__main__':
    main()
