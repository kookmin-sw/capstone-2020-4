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
    rgb_model = rgb_build_model()
#     print("Model %s is loaded. " % (args.arch))

    # define loss function (criterion) and optimizer
    criterion = nn.CrossEntropyLoss().cuda()
 
    rgb_optimizer = torch.optim.SGD(rgb_model.parameters(), 0.001,
                                momentum=0.9,
                                weight_decay=5e-4)

    if demo:
        resume_and_evaluate(rgb_optimizer, rgb_model)
                
def rgb_build_model():
    
    model = models.__dict__["rgb_resnet152"](pretrained=True, num_classes= 23)
    model.cuda()
    return model

def resume_and_evaluate(rgb_optimizer, rgb_model):
#     model = build_model()
#     optimizer = param_optimizer
    if resume:
        rgb_resume = "020_checkpoint_rgb.pth.tar"
        print("==> loading checkpoint '{}'".format(rgb_resume))
        rgb_checkpoint = torch.load(rgb_resume)
        rgb_start_epoch = rgb_checkpoint['epoch']
        rgb_best_prec1 = rgb_checkpoint['best_prec1']
        rgb_model.load_state_dict(rgb_checkpoint['state_dict'])
        rgb_optimizer.load_state_dict(rgb_checkpoint['optimizer'])

    if demo:
        rgb_model.eval()
#         flow = flow_test(flow_model)
        rgb = rgb_test(rgb_model)
#         print(len(flow), len(rgb))

def rgb_test(param_model):
    model = param_model
    f = open("rgb_result.txt", 'w')
    video_list = os.listdir(video)
    for file in video_list:
        f.write(file + "\n")
        frame_count = 2
        clip_mean = [0.485, 0.456, 0.406] * 1
        clip_std = [0.229, 0.224, 0.225] * 1
        rgb_value = []
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
        nn_output = torch.tensor(np.zeros((1, 23)), dtype=torch.float32).cuda()
        sampled_list = []
        first_count = 0
        while True:
            # read each frame and prepare it for feedforward in nn (resize and type)
            ret, orig_frame = vs.read()
            if ret is False:
                break

            else:
                orig_frame = cv2.resize(orig_frame,(342, 256), interpolation=cv2.INTER_LINEAR)    
                frame = cv2.cvtColor(orig_frame, cv2.COLOR_BGR2RGB)
                frame = transform(frame).view(1, 3, 224, 224).cuda()
                frame = frame.float().cuda(async=True)
                # feed the frame to the neural network
                nn_output = model(frame)
                # vote for class with 25 consecutive frames
                if frame_count % 10 == 0:
                    nn_output = softmax(nn_output)
                    nn_output = nn_output.data.cpu().numpy()
                    preds = nn_output.argsort()[0][-5:][::-1]
                    pred_classes = [(idx_to_class[str(pred+1)], nn_output[0, pred]) for pred in preds]

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
                    value = 0
                    for i in range(5):
                        y = y0 + i * dy
                        if pred_classes[i][0] == label:
                            value = pred_classes[i][1]

                    # reset the process
                    rgb_value.append(value)
                    f.write(str(value) + "\n")
                    nn_output = torch.tensor(np.zeros((1, 23)), dtype=torch.float32).cuda()
    #             cv2.imwrite("temp/" + str(frame_count) + ".jpg", orig_frame)
                # Display the resulting frame and the classified action
                frame_count += 1

        # When everything done, release the capture
        f.write("----\n")
        vs.release()  
        
    f.close()
    return rgb_value

if __name__ == '__main__':
    main()
