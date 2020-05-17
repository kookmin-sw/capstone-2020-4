import argparse
import os
from detecto.core import Model
from detecto import utils, visualize
from moviepy.tools import subprocess_call
from moviepy.config import get_setting
from torchvision import transforms
import cv2

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()
print(args.dir)
file_list = os.listdir(args.dir)

model = Model.load('model_weights4.pth', ['adult', 'blood'])
adult_list = []
blood_list = []

for file in file_list:
    path = args.dir + file
    video = cv2.VideoCapture(path)
    idx = 0

    while (video.isOpened()):
        ret, frame = video.read()
        width = video.get(3)
        height = video.get(4)
        if not ret:
            break
            
        else:
            prediction = model.predict(frame)
            labels, boxes, scores = prediction
            if len(labels) >= 1 and labels[0] == "blood" and scores[0] > 0.8:
              print(labels, scores)
              # img = cv2.imread(file_path, cv2.IMREAD_COLOR)
              cut_img = frame[int(boxes[0][1]):int(boxes[0][3]), int(boxes[0][0]):int(boxes[0][2])]
              img_hsv = cv2.cvtColor(cut_img, cv2.COLOR_BGR2HSV)
              lower_bound = (0, 130, 120)
              upper_bound = (10, 255, 255)
              height, width, channel = img_hsv.shape
              total = height * width
              img_mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
              if cv2.countNonZero(img_mask) / total > 0.1:
                  cv2.imwrite(args.dir/ + "roi_" + file, cut_img)


