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
                video_list.append(file)

print(video_list)

def ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ Makes a new video file playing video file ``filename`` between
    the times ``t1`` and ``t2``. """
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

for video in video_list:
    video_name = video.split(".")[0]
    ffmpeg_extract_subclip("./smoke.avi", int(video_name), int(video_name) + 3, targetname=f"./smoke/{video_name}.mp4")


