import os
import argparse
import cv2
import numpy as np

parser = argparse.ArgumentParser(description='PyTorch Two-Stream Action Recognition')
parser.add_argument('--video', default='', type=str,
                    help='input video')

args = parser.parse_args()

client = args.video.split(".")[0]

f = open("../static/" + client + "_subtitle_result.txt", 'r')

os.system("mkdir ../static/" + client + "_subtitle_img/")
path = "../static/" + client + "_subtitle_img/"

while(1):
    line = f.readline()
    if not line:
        break
    else:
        imgNum = line.split("/")[0]
        bound_box = line.split("/")[1]
        bound_boxes = bound_box.split(" ")
        print(imgNum, np.array(bound_boxes[0]), np.array(bound_boxes[2]))
        left = bound_boxes[0].replace("(", "")
        left = left.replace(")", "")
        left_x = int(left.split(",")[0])
        left_y = int(left.split(",")[1])
        right = bound_boxes[2].replace("(", "")
        right = right.replace(")", "")
        right_x = int(right.split(",")[0])
        right_y = int(right.split(",")[1])
        img =  cv2.imread(client + "/" + imgNum + ".jpg")
        dog = cv2.imread("./dog.png")
        dog = cv2.resize(dog, (right_x - left_x, right_y - left_y))
        img[left_y:right_y,left_x:right_x] = dog
        #img = cv2.rectangle(img,(left_x, left_y), (right_x, right_y),(0,0,255),3)
        cv2.imwrite(client + "/" + imgNum + ".jpg", img)
        os.system("cp " + client + "/" + imgNum + ".jpg ../static/" + client + "_subtitle_img/")
        

f.close()
os.system("mv ../static/" + client + "_blood_result.txt ../static/" + client)
os.system("mv ../static/" + client + "_blood_result.txt ../static/" + client)   
