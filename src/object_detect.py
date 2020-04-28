import argparse
import os
from detecto.core import Model
from detecto import utils, visualize

from torchvision import transforms
parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()
print(args.dir)
file_list = os.listdir(args.dir)

model = Model.load('model_weights7.pth', ['smoke', 'knife', 'gun'])
video_list = []
game_list = []

for file in file_list:
    path = args.dir + file
    image = utils.read_image(path)
    prediction = model.predict(image)
    labels, boxes, scores = prediction
    if labels:
        print(file, labels[0], scores[0])
        if labels[0] == "smoke" or labels[0] == "knife":
            if scores[0] > 0.6:
                video_list.append(path)

print(video_list)

