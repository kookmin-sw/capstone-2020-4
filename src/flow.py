{\rtf1\ansi\ansicpg949\deff0\nouicompat{\fonttbl{\f0\fnil\fcharset129 \'b8\'bc\'c0\'ba \'b0\'ed\'b5\'f1;}}
{\*\generator Riched20 10.0.18362}\viewkind4\uc1 
\pard\sa200\sl276\slmult1\f0\fs20\lang18 import os\par
import time\par
import argparse\par
import shutil\par
import numpy as np\par
import cv2\par
from PIL import Image\par
import torch\par
import torch.nn as nn\par
import torch.nn.parallel\par
import torch.backends.cudnn as cudnn\par
import torch.optim\par
import torch.utils.data\par
import torchvision.transforms as transforms\par
import json\par
from collections import OrderedDict\par
import video_transforms\par
import models\par
import datasets\par
\par
model_names = sorted(name for name in models.__dict__\par
    if name.islower() and not name.startswith("__")\par
    and callable(models.__dict__[name]))\par
\par
dataset_names = sorted(name for name in datasets.__all__)\par
\par
parser = argparse.ArgumentParser(description='PyTorch Two-Stream Action Recognition')\par
parser.add_argument('--resume', default='./checkpoints', type=str, metavar='PATH',\par
                    help='path to latest checkpoint (default: none)')\par
parser.add_argument('--demo', dest='demo', action='store_true', help='use model inference on video')\par
parser.add_argument('--label', default='smoke', type=str,\par
                    help='input label')\par
parser.add_argument('--video', default='', type=str,\par
                    help='input video')\par
\par
best_prec1 = 0\par
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"   \par
os.environ["CUDA_VISIBLE_DEVICES"]="0"\par
\par
class UCF101_splitter():\par
    def __init__(self, path, split):\par
        self.path = path\par
        self.split = split\par
\par
    def get_action_index(self):\par
        self.action_label=\{\}\par
        with open(self.path+'classInd.txt') as f:\par
            content = f.readlines()\par
            content = [x.strip('\\r\\n') for x in content]\par
        f.close()\par
        for line in content:\par
            label,action = line.split(' ')\par
            #print label,action\par
            if action not in self.action_label.keys():\par
                self.action_label[action]=label\par
\par
    def split_video(self):\par
        self.get_action_index()\par
        for path,subdir,files in os.walk(self.path):\par
            for filename in files:\par
                if filename.split('.')[0] == 'trainlist'+self.split:\par
                    train_video = self.file2_dic(self.path+filename)\par
                if filename.split('.')[0] == 'testlist'+self.split:\par
                    test_video = self.file2_dic(self.path+filename)\par
        self.train_video = self.name_HandstandPushups(train_video)\par
        self.test_video = self.name_HandstandPushups(test_video)\par
\par
        return self.train_video, self.test_video\par
\par
    def file2_dic(self,fname):\par
        with open(fname) as f:\par
            content = f.readlines()\par
            content = [x.strip('\\r\\n') for x in content]\par
        f.close()\par
        dic=\{\}\par
        for line in content:\par
            #print line\par
            video = line.split('/',1)[1].split(' ',1)[0]\par
            key = video.split('_',1)[1].split('.',1)[0]\par
            label = self.action_label[line.split('/')[0]]   \par
            dic[key] = int(label)\par
            #print key,label\par
        return dic\par
\par
    def name_HandstandPushups(self,dic):\par
        dic2 = \{\}\par
        for video in dic:\par
            n,g = video.split('_',1)\par
            if n == 'HandStandPushups':\par
                videoname = 'HandstandPushups_'+ g\par
            else:\par
                videoname=video\par
            dic2[videoname] = dic[video]\par
        return dic2\par
\par
def main():\par
    global args, best_prec1\par
    args = parser.parse_args()\par
    global resume\par
    resume = True\par
    global demo\par
    demo = args.demo\par
    global label\par
    label = args.label\par
    global video\par
    video = args.video\par
    print("Building model ... ")\par
    flow_model = flow_build_model()\par
#     print("Model %s is loaded. " % (args.arch))\par
\par
    # define loss function (criterion) and optimizer\par
    criterion = nn.CrossEntropyLoss().cuda()\par
    flow_optimaizer = torch.optim.SGD(flow_model.parameters(), 0.001,\par
                                momentum=0.9,\par
                                weight_decay=5e-4)\par
    if demo:\par
        resume_and_evaluate(flow_optimaizer, flow_model)\par
              \par
def flow_build_model():\par
    \par
    model = models.__dict__["flow_resnet152"](pretrained=True, num_classes= 23)\par
    model.cuda()\par
    return model\par
\par
def resume_and_evaluate(flow_optimizer, flow_model):\par
#     model = build_model()\par
#     optimizer = param_optimizer\par
    if resume:\par
        flow_resume = "040_checkpoint_rgb.pth.tar"\par
        print("==> loading checkpoint '\{\}'".format(flow_resume))\par
        flow_checkpoint = torch.load(flow_resume)\par
        flow_start_epoch = flow_checkpoint['epoch']\par
        flow_best_prec1 = flow_checkpoint['best_prec1']\par
        flow_model.load_state_dict(flow_checkpoint['state_dict'])\par
        flow_optimizer.load_state_dict(flow_checkpoint['optimizer'])\par
\par
    if demo:\par
        flow_model.eval()\par
        flow = flow_test(flow_model)\par
#         rgb = rgb_test(rgb_model)\par
#         print(len(flow), len(rgb))\par
\par
    \par
def flow_test(param_model):\par
    model = param_model\par
    video_list = os.listdir(video)\par
    f = open("flow_result.txt", 'w')\par
    for file in video_list:\par
        f.write(file + "\\n")\par
#         file_data = OrderedDict()\par
        frame_count = 0\par
        clip_mean = [0.5, 0.5] * 10\par
        clip_std = [0.226, 0.226] * 10\par
        normalize = video_transforms.Normalize(mean=clip_mean,\par
                                                   std=clip_std)\par
        # config the transform to match the network's format\par
        transform = video_transforms.Compose([\par
                    # video_transforms.Scale((256)),\par
                    video_transforms.CenterCrop((224)),\par
                    video_transforms.ToTensor(),\par
                    normalize,\par
                ])\par
\par
        # prepare the translation dictionary label-action\par
        data_handler = UCF101_splitter(os.getcwd()+'/datasets/ucf101_splits/', None)\par
        data_handler.get_action_index()\par
        class_to_idx = data_handler.action_label\par
        idx_to_class = \{v: k for k, v in class_to_idx.items()\}\par
\par
        # Start looping on frames received from webcam\par
        vs = cv2.VideoCapture(video + file)\par
        softmax = torch.nn.Softmax()\par
        nn_output = torch.FloatTensor(2*10,224,224)\par
        count = 0\par
        idx = 0\par
        temp = ''\par
        x = []\par
        sampled_list = []\par
        flow_value = []\par
        while (vs.isOpened()):\par
            ret, image = vs.read()\par
            if ret is False:\par
                break\par
            else:\par
                image = cv2.resize(image,(342, 256), interpolation=cv2.INTER_LINEAR)\par
                x.append(temp)\par
                if count == 11:\par
                    sampled_list = []\par
        #             input_var = torch.autograd.Variable(clip_input, volatile=True)    \par
                    temp = ''\par
                    input_var = clip_input.view(1, 20, 224, 224).cuda()\par
                    output = model(input_var)\par
                    output = softmax(output)\par
                    output = output.data.cpu().numpy()\par
                    preds = output.argsort()[0][-5:][::-1]\par
                    pred_classes = [(idx_to_class[str(pred+1)], output[0, pred]) for pred in preds]\par
                    value = 0\par
                    for i in range(5):\par
                        if pred_classes[i][0] == label:\par
                            value = pred_classes[i][1]\par
\par
                        temp += '\{\} - \{:.2f\}\\n'.format(pred_classes[i][0], pred_classes[i][1])\par
                    flow_value.append(value)\par
                    f.write(str(value) + "\\n")\par
                    nn_output = torch.FloatTensor(2*10,224,224)\par
                    count = 1\par
\par
                if count == 0:\par
                    old_frame = image.copy()\par
                    prev = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)\par
\par
                else:\par
                    next = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\par
                    flow = cv2.calcOpticalFlowFarneback(prev, next, 1, 0.5, 3, 15, 3, 5, 1.2, 0)\par
                    horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)\par
                    vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)\par
                    horz = horz.astype('uint8')\par
                    vert = vert.astype('uint8')\par
                    imgH = Image.fromarray(horz)\par
                    imgV = Image.fromarray(vert)\par
\par
                    sampled_list.append(np.expand_dims(imgH, 2))\par
                    sampled_list.append(np.expand_dims(imgV, 2))\par
\par
                    clip_input = np.concatenate(sampled_list, axis=2)\par
                    clip_input = transform(clip_input)\par
                    clip_input = clip_input.float().cuda(async=True)\par
                    imgH.close()\par
                    imgV.close()\par
                    prev = next.copy()\par
\par
                count += 1\par
                idx += 1\par
        f.write("----\\n")\par
#         file_data[file] = flow_value\par
#         with open('flow.json', 'w', encoding="utf-8") as make_file:\par
#             json.dump(file_data, make_file, ensure_ascii=False, indent="\\t")\par
        print(idx)\par
        vs.release()\par
        \par
    f.close()    \par
    return flow_value\par
\par
if __name__ == '__main__':\par
    main()\par
}
 