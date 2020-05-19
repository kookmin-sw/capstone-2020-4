import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()
import os
import argparse
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

## client ID 얻어오기
parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str)
args = parser.parse_args()

## 고유번호마다 폴더를 생성, 라벨 폴더 생성.
os.system("mkdir " + args.dir + "/smoke")
os.system("mkdir " + args.dir + "/Knife")

## predictor 생성
cfg = get_cfg()
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 5
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml"))
cfg.MODEL.WEIGHTS = "/content/drive/My Drive/detectron_model/model_00025_710.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5   # set the testing threshold for this model
cfg.DATASETS.TEST = ("test",)
predictor = DefaultPredictor(cfg)