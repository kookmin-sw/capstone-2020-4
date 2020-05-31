import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
import numpy as np
import cv2
import random
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from moviepy.tools import subprocess_call
from moviepy.config import get_setting
import os
import argparse
import socketio
import natsort

## get client ID
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
args = parser.parse_args()
client_folder = args.dir.split(".")[0]
os.system("mkdir " + client_folder + "/smoke")
os.system("mkdir " + client_folder + "/knife")

cfg = get_cfg()
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 5
cfg.merge_from_file("detectron2_repo/configs/COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml")
cfg.MODEL.WEIGHTS = "model_00025_710.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.1   # set the testing threshold for this model
cfg.DATASETS.TEST = ("detectron2",)
predictor = DefaultPredictor(cfg)

knife_list = []
smoke_list = []
video_len = 0
blood_text = open(client_folder + "/blood.txt", "w")
adult_text = open(client_folder + "/adult_result.txt", "w")
file_list = os.listdir(client_folder)
filelist = [file for file in file_list if file.endswith(".jpg")]
video_len = len(filelist)
adult_check = 0
file = 0
while file < len(filelist):
    file_name = str(file) + ".jpg"
    print(file_name)
    file_absolute_path = client_folder + '/' + file_name
    im = cv2.imread(file_absolute_path)
    outputs = predictor(im)
    if len(outputs["instances"].scores) > 0:
        label = outputs["instances"].pred_classes[0].item()
        score = outputs["instances"].scores[0].item()
        print(label, score)
        #adult
        if label == 0 and score >= 0.75:
            adult_check += 1
            adult_text.write(str(file) + "\n")
            file += 3
        # gun
        elif (label == 1 or label == 2) and score >= 0.7:
            blood_text.write(str(file) + ",")
            file += 3
        # knife
        elif label == 3 and score >= 0.75:
            knife_list.append(str(file))
            file += 3
        # smoke
        elif label == 4 and score >= 0.75:
            smoke_list.append(str(file))
            file += 3
    file += 1
adult_text.close()
blood_text.close()

if adult_check >= 1:
	os.system("mv " + client_folder + "/adult_result.txt ../static/" + client_folder)
smoke_list = natsort.natsorted(smoke_list)
knife_list = natsort.natsorted(knife_list)

sio = socketio.Client()
sio.connect("http://3.34.55.213:1234")
os.system("aws s3 cp " + client_folder + "/blood.txt " +  "s3://youhi-project/" + client_folder + "/blood.txt")
sio.emit("complete", args.dir)
sio.sleep(1)
sio.disconnect()

def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    name, ext = os.path.splitext(filename)
    if not targetname:
        T1, T2 = [int(1000*t) for t in [t1, t2]]
        targetname = "%sSUB%d_%d.%s" % (name, T1, T2, ext)
    cmd = [get_setting("FFMPEG_BINARY"),
           "-i", filename,
           "-ss", "%0.2f"%t1,
           "-t", "%0.2f"%(t2-t1),
           "-c:v",  "libx264",  "-c:a", "aac",
           "-strict", "experimental", "-b:a", "128k",
           targetname]
    subprocess_call(cmd)

if len(knife_list) != 0:
    for x in range(len(knife_list) - 1):
        video_name = knife_list[x]
        ffmpeg_extract_subclip(args.dir, int(knife_list[x]), int(knife_list[x]) + 3, targetname=client_folder + f"/knife/{video_name}.mp4")
    video_name = knife_list[len(knife_list)-1]
    print(video_len)
    if video_len - int(knife_list[len(knife_list)-1]) > 3:
        ffmpeg_extract_subclip(args.dir, int(knife_list[len(knife_list)-1]), int(knife_list[len(knife_list)-1]) + 3, targetname=client_folder + f"/knife/{video_name}.mp4")
    else:
        ffmpeg_extract_subclip(args.dir, int(knife_list[len(knife_list)-1]), video_len, targetname=client_folder + f"/knife/{video_name}.mp4")
    os.system("python3.6 flow.py --demo --label Knife --video " + client_folder +"/knife/ & python3.6 rgb.py --demo --label Knife --video " + client_folder + "/knife/")
    os.system("python3.6 fusion.py --video " + client_folder + "/knife/ --label knife")

if len(smoke_list) != 0:
    print(smoke_list)
    for x in range(len(smoke_list) - 1):
        video_name = smoke_list[x]
        ffmpeg_extract_subclip(args.dir, int(smoke_list[x]), int(smoke_list[x]) + 3, targetname=client_folder + f"/smoke/{video_name}.mp4")
    video_name = smoke_list[len(smoke_list)-1]
    if video_len - int(smoke_list[len(smoke_list)-1]) > 3:
        ffmpeg_extract_subclip(args.dir, int(smoke_list[len(smoke_list)-1]), int(smoke_list[len(smoke_list)-1]) + 3, targetname=client_folder + f"/smoke/{video_name}.mp4")
    else:
        ffmpeg_extract_subclip(args.dir, int(smoke_list[len(smoke_list)-1]), video_len, targetname=client_folder + f"/smoke/{video_name}.mp4")
    os.system("python3.6 flow.py --demo --label smoke --video " + client_folder +"/smoke/ & python3.6 rgb.py --demo --label smoke --video " + client_folder + "/smoke/")
    os.system("python3.6 fusion.py --video " + client_folder + "/smoke/ --label smoke")
