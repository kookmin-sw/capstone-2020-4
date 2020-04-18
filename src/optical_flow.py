import cv2
import numpy as np
import os
from natsort import natsorted, ns
# Create list of names here from my1.bmp up to my20.bmp

dir_list = os.listdir("./jpegs_256/")
dir_list = natsorted(dir_list)
idx = 0
for dir in dir_list:
    dir_path = "./jpegs_256/" + dir +"/"
    list_names = os.listdir(dir_path)
    list_names = natsorted(list_names)
    file_list = os.listdir(dir_path)
    file_list = natsorted(file_list)
    for i in range(0, len(file_list)):
        list_names[i] = dir_path + list_names[i]
# Read in the first frame
    
    frame1 = cv2.imread(list_names[0])
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

# Set counter to read the second frame at the start
    counter = 1

# Until we reach the end of the list...
    while counter < len(list_names):
    # Read the next frame in
        frame2 = cv2.imread(list_names[counter])
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    # Calculate optical flow between the two frames
        flow = cv2.calcOpticalFlowFarneback(prvs, next, 1, 0.5, 3, 15, 3, 5, 1.2, 0)

    # Normalize horizontal and vertical components
        horz = cv2.normalize(flow[...,0], None, 0, 255, cv2.NORM_MINMAX)     
        vert = cv2.normalize(flow[...,1], None, 0, 255, cv2.NORM_MINMAX)
        horz = horz.astype('uint8')
        vert = vert.astype('uint8')
    # Show the components as images
        print(dir)
        cv2.imwrite('u/'+dir + "/" +file_list[counter], horz)
        cv2.imwrite('v/'+dir +"/" + file_list[counter], vert)
        counter += 1

    idx += 1 


