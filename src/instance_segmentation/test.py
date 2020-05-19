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