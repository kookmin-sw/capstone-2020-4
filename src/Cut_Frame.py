import cv2
import numpy as np

#for videoNum in np.arange(1, 2):
  # 영상 번호
  # 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class
vidcap = cv2.VideoCapture('MP4 file in S3 bucket')

count = 0

while(vidcap.isOpened()):
    # read()는 grab()와 retrieve() 두 함수를 한 함수로 불러옴
    # 두 함수를 동시에 불러오는 이유는 프레임이 존재하지 않을 때
    # grab() 함수를 이용하여 return false 혹은 NULL 값을 넘겨 주기 때문
    ret, image = vidcap.read()

    #print(ret)
    if ret:
      # 캡쳐된 이미지를 저장하는 함수 
      cv2.imwrite("" % count, image)

      print('Saved frame%d.jpg' % count)
      count += 1
    else:
      print("The work(video number : " + str(videoNum) + ") is done!")
      break;

vidcap.release()  
