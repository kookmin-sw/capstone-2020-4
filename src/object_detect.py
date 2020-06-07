import argparse
import os
from detecto.core import Model
from detecto import utils, visualize
from moviepy.tools import subprocess_call
from moviepy.config import get_setting
from torchvision import transforms
import cv2
import math
from moviepy.editor import VideoFileClip

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--video', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()
print(args.video)
dir = args.video.split(".")[0]
clip = VideoFileClip(args.video)
duration = math.floor(clip.duration)
cap = cv2.VideoCapture(args.video)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_count = math.floor(length / duration)
frame_count = frame_count / 2
file_list = os.listdir(dir)
os.system("mkdir " + dir + "/blood")
f = open(dir + "/blood.txt", "r")
count = 0
line = f.readline().split(",")

for file in file_list:
    if file.endswith("jpg"):
        count += 1


def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ Makes a new video file playing video file ``filename`` between
    the times ``t1`` and ``t2``. """
    name, ext = os.path.splitext(filename)
    if not targetname:
        T1, T2 = [int(1000 * t) for t in [t1, t2]]
        targetname = "%sSUB%d_%d.%s" % (name, T1, T2, ext)

    cmd = [get_setting("FFMPEG_BINARY"),
           "-i", filename,
           "-ss", "%0.2f" % t1,
           "-t", "%0.2f" % (t2 - t1),
           "-c:v", "libx264", "-c:a", "aac",
           "-strict", "experimental", "-b:a", "128k",
           targetname]

    subprocess_call(cmd)


print(line)
line.remove('')
if len(line) != 0:
    for x in range(len(line) - 1):
        video_name = math.floor(int(line[x]) / frame_count)
        ffmpeg_extract_subclip(args.video, math.floor(int(line[x]) / frame_count),
                               math.floor(int(line[x]) / frame_count) + 3, targetname=dir + f"/blood/{video_name}.mp4")

    video_name = math.floor(int(line[len(line) - 1]) / frame_count)
    print(frame_count, video_name, duration)
    if duration - math.floor(int(line[len(line) - 1]) / frame_count) > 3:
        ffmpeg_extract_subclip(args.video, math.floor(int(line[len(line) - 1]) / frame_count),
                               math.floor(int(line[len(line) - 1]) / frame_count) + 3,
                               targetname=dir + f"/blood/{video_name}.mp4")
    else:
        ffmpeg_extract_subclip(args.video, math.floor(int(line[len(line) - 1]) / frame_count), duration,
                               targetname=dir + f"/blood/{video_name}.mp4")
    #    os.system("rm " + dir + "/blood.txt")   

    model = Model.load('model_weights4.pth', ['adult', 'blood'])

    video_list = os.listdir(dir + "/blood")
    os.system("mkdir " + dir + "/blood/image")
    os.system("mkdir " + dir + "/blood/temp")

    idx = 0
    for video in video_list:
        video_name = video.split(".")[0]
        video = cv2.VideoCapture(dir + "/blood/" + video)
        idx = 0
        while (video.isOpened()):
            ret, frame = video.read()
            if not ret:
                break
            else:
                if int(video.get(1)) % 3 == 0:
                    cv2.imwrite(dir + "/blood/temp/" + video_name + "_" + str(idx) + ".jpg", frame)
                    idx += 1

        idx = 0
        temp_list = os.listdir(dir + "/blood/temp")
        for temp in temp_list:
            path = dir + "/blood/temp/" + temp
            image = utils.read_image(path)
            print(image.shape)
            prediction = model.predict(image)
            labels, boxes, scores = prediction
            if len(labels) >= 1 and labels[0] == "blood" and scores[0] > 0.7:
                print(labels, scores)
                img = cv2.imread(path, cv2.IMREAD_COLOR)
                cut_img = img[int(boxes[0][1]):int(boxes[0][3]), int(boxes[0][0]):int(boxes[0][2])]
                img_hsv = cv2.cvtColor(cut_img, cv2.COLOR_BGR2HSV)
                lower_bound = (0, 200, 80)
                upper_bound = (10, 255, 255)
                lower_bound2 = (175, 130, 80)
                upper_bound2 = (185, 255, 255)
                height, width, channel = img_hsv.shape
                total = height * width
                img_mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
                img_mask2 = cv2.inRange(img_hsv, lower_bound2, upper_bound2)
                hsv_img = img_mask | img_mask2
                if cv2.countNonZero(hsv_img) / total > 0.1:
                    print(video_name)
                    cv2.imwrite(dir + "/blood/image/" + video_name + "_" + str(idx) + ".jpg", cut_img)
                    idx += 1

    os.system("python3.6 image_classification.py --dir " + dir)
