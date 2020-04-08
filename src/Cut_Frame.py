from moviepy.tools import subprocess_call
from moviepy.config import get_setting
import os
from moviepy.editor import VideoFileClip
import math

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

clip = VideoFileClip("./sin.mp4")

f = open("filename.txt", "r")
if f.mode == "r":
    content = (f.read())

content_list = content.split("\n")
print(content_list)

for time in content_list:
    t = int(time)
    ffmpeg_extract_subclip("./sin.mp4", t, t+4, targetname=f"{t}.mp4")
