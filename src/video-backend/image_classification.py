import os
import sys
import argparse
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
import natsort
from torch.autograd import Variable

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

class CustomConvNet(torch.nn.Module):
    def __init__(self, num_classes):
        super(CustomConvNet, self).__init__()

        self.layer1 = self.conv_module(3, 16)
        self.layer2 = self.conv_module(16, 32)
        self.layer3 = self.conv_module(32, 64)
        self.layer4 = self.conv_module(64, 128)
        self.layer5 = self.conv_module(128, 256)
        self.gap = self.global_avg_pool(256, num_classes)

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = self.layer3(out)
        out = self.layer4(out)
        out = self.layer5(out)
        out = self.gap(out)
        out = out.view(-1, num_classes)

        return out

    def conv_module(self, in_num, out_num):
        return torch.nn.Sequential(
            torch.nn.Conv2d(in_num, out_num, kernel_size=3, stride=1, padding=1),
            torch.nn.BatchNorm2d(out_num),
            torch.nn.LeakyReLU(),
            torch.nn.MaxPool2d(kernel_size=2, stride=2))

    def global_avg_pool(self, in_num, out_num):
        return torch.nn.Sequential(
            torch.nn.Conv2d(in_num, out_num, kernel_size=3, stride=1, padding=1),
            torch.nn.BatchNorm2d(out_num),
            torch.nn.LeakyReLU(),
            torch.nn.AdaptiveAvgPool2d((1, 1)))

if __name__ == "__main__":
    args = parser.parse_args()
    transform = transforms.Compose([transforms.Resize([128, 128]),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    dir_path = args.dir
    # image_names = os.listdir(dir_path)
    image_names = os.listdir(dir_path + "/adult_temp")
    image_names = natsort.natsorted(image_names)
    dir_path = dir_path + "/adult_temp"
    num_classes = 2
    custom_model = CustomConvNet(num_classes=num_classes).to(device)
    weights_file = './adult_model.pth'
    ckpt = torch.load(weights_file, map_location=device)
    custom_model.load_state_dict(ckpt['custom_model'])
    f = open(args.dir + "/adult_result.txt", "w")
    custom_model.eval()
    #20200515_171607382
    with torch.no_grad():
        softmax = torch.torch.nn.Softmax()
        for image_source in image_names:
            print(image_source)
            #image_source = image_source.split(".")[0]
            image_name = image_source.split(".")[0]
            type = image_source.split(".")[1]
            print(image_source)
            if type == "jpg":
                # image = Image.open(os.path.join(dir_path, image_source))
                image = Image.open(os.path.join(dir_path, image_source)).convert('RGB')
                # image = image.resize((128, 128))
                image = transform(image)
                data = Variable(image)
                data = data.unsqueeze(0)
                image = data.to(device)
                # pred_y = custom_model(image)
                print(image_source)
                pred_y = custom_model(image)
                pred_y = softmax(pred_y)
                pred_y = pred_y.cpu().numpy()
                preds = pred_y.argsort()[0][-5:][::-1]
                pred_classes = [(pred, pred_y[0, pred]) for pred in preds]
                if pred_classes[0][0] == 0:
                    f.write(image_name + "\n")
