import torch
from torch import nn
from sklearn.metrics import accuracy_score
from tqdm import tqdm
from PIL import Image
import pandas
import os
import argparse
import cv2
from functions import *
import numpy as np
import torchvision.transforms as transforms
import torch.utils.data as data
import matplotlib.pyplot as plt
from functions import *
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle
action_name_path = './youhi_label.pkl'

CNN_fc_hidden1, CNN_fc_hidden2 = 1024, 768
CNN_embed_dim = 512   # latent dim extracted by 2D CNN
res_size = 224        # ResNet image size
dropout_p = 0.0       # dropout probability

# DecoderRNN architecture
RNN_hidden_layers = 3
RNN_hidden_nodes = 512
RNN_FC_dim = 256

save_model_path = "./ResNetCRNN_ckpt/"

with open(action_name_path, 'rb') as f:
    action_names = pickle.load(f)   # load UCF101 actions names

le = LabelEncoder()
le.fit(action_names)

list(le.classes_)

action_category = le.transform(action_names).reshape(-1, 1)
enc = OneHotEncoder()
enc.fit(action_category)

actions = []

all_y_list = labels2cat(le, actions)    # all video labels

def transform(self, img):
    return transforms.Compose([
        transforms.Resize([res_size, res_size]),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])(img)

def load_imgs_from_video(path: str)->list:
    """Extract images from video.
    Args:
        path(str): The path of video.
    Returns:
        A list of PIL Image.
    """
    video_fd = cv2.VideoCapture(path)
    video_fd.set(16, True)
    # flag 16: 'CV_CAP_PROP_CONVERT_RGB'
    # indicating the images should be converted to RGB.

    if not video_fd.isOpened():
        raise ValueError('Invalid path! which is: {}'.format(path))

    images = [] # type: list[Image]

    success, frame = video_fd.read()
    video_fd.set(3,342)
    video_fd.set(4,256)

    idx = 0

    while success:
        if idx == 28:
            break;

        images.append(Image.fromarray(frame))
        success, frame = video_fd.read()
        idx += 1

    return images

def eval(video_path: str):
    if not os.path.exists(video_path):
        raise ValueError('Invalid path! which is: {}'.format(video_path))

    use_cuda = torch.cuda.is_available()
    device = torch.device('cuda' if use_cuda else 'cpu')

    cnn_encoder = ResCNNEncoder(fc_hidden1=CNN_fc_hidden1, fc_hidden2=CNN_fc_hidden2, drop_p=dropout_p,
                                CNN_embed_dim=CNN_embed_dim).to(device)
    rnn_decoder = DecoderRNN(CNN_embed_dim=CNN_embed_dim, h_RNN_layers=RNN_hidden_layers, h_RNN=RNN_hidden_nodes,
                             h_FC_dim=RNN_FC_dim, drop_p=dropout_p, num_classes=4).to(device)

    cnn_encoder.load_state_dict(torch.load(os.path.join(save_model_path, 'cnn_encoder_epoch1.pth')))
    rnn_decoder.load_state_dict(torch.load(os.path.join(save_model_path, 'rnn_decoder_epoch1.pth')))

    model = nn.Sequential(
        cnn_encoder,
        rnn_decoder
    )

    model.to(device)
    model.eval()

    # Do inference
    pred_labels = []
    video_names = os.listdir(video_path)
    with torch.no_grad():
        for video in tqdm(video_names, desc='Inferencing'):
            # read images from video
            images = load_imgs_from_video(os.path.join(video_path, video))
            # apply transform
            images = [transform(None, img) for img in images]
            # stack to tensor, batch size = 1
            images = torch.stack(images, dim=0).unsqueeze(0)
            # do inference
            images = images.to(device)
            pred_y = model(images) # type: torch.Tensor
            pred_y = pred_y.argmax(dim=1).cpu().numpy().tolist()
            pred_labels.append([video, pred_y[0]])
            print(pred_labels[-1])

    # if len(labels) > 0:
    #     #     acc = accuracy_score(pred_labels, labels)
    #     #     print('Accuracy: %0.2f' % acc)
    #     #
    #     # # Save results
    #     # pandas.DataFrame(pred_labels).to_csv('result.csv', index=False)
    #     # print('Results has been saved to {}'.format('result.csv'))
    return pred_labels

# def parse_args():
#     parser = argparse.ArgumentParser(usage='python3 eval.py -i path/to/videos -r path/to/checkpoint')
#     parser.add_argument('-i', '--video_path', help='path to videos')
#     parser.add_argument('-r', '--checkpoint', help='path to the checkpoint')
#     args = parser.parse_args()
#     return args

if __name__ == "__main__":
    # args = parse_args()
    eval("C:/Users/says7/Downloads/example")
