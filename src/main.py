import os
import sys, math, argparse, re
import fasttext
import cs_sim, googleSTT, video2voice, voice_filter, khaiii_filter, makeData, cutAudio


os.system("python video2voice.py --input ./video/0.mp4 --output ./voice_raw/0.wav")
cutting("./voice_raw/0.wav")
os.system("python3 googletSTT.py --input ./voice/ --time ./textData/time.txt --text ./textData/write.txt --count ./voice")
os.system("python3 khaiii_filter.py --input ./textData/write.txt --output ./textData/khaiii.txt")
os.system("python3 voice_filter.py --input ./textData/khaiii.txt --time ./textData/time.txt")