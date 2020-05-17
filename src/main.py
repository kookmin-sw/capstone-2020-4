import os
import sys, math, argparse, re
import fasttext
import cs_sim, googleSTT, video2voice, voice_filter, khaiii_filter, makeData, cutAudio


video2voice("0.mp4")
cutting("./voice_raw/0.wav")
os.system("python3 googletSTT.py")
os.system("python3 khaiii_filter.py --input ./textData/write.txt --output ./textData/khaiii.txt")
os.system("python3 voice_filter.py --input ./textData/khaiii.txt --time ./textData/time.txt")