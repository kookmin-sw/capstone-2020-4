import os
import sys, math, argparse, re
import fasttext
import cs_sim, googleSTT, video2voice, voice_filter, khaiii_filter, makeData, cutAudio


#os.system("export GOOGLE_APPLICATION_CREDENTIALS=\"/home/ubuntu/voice_classification/capstone.json\"")

num = 2

os.system("mkdir " + str(num)) 
os.system("mkdir " + "./" + str(num) + "/textData")
os.system("mkdir " + "./" + str(num) + "/voice_raw")
os.system("mkdir " + "./" + str(num) + "/voice")
os.system("mkdir " + "./" + str(num) + "/video")

os.system("cp /home/ubuntu/voice_classification/video/0.mp4 /home/ubuntu/voice_classification/" + str(num) + "/video")

os.system("python video2voice.py --input ./" + str(num) + "/video/0.mp4 --output ./" + str(num) + "/voice_raw/0.wav")
os.system("python cutAudio.py --input ./" + str(num) + "/voice_raw/0.wav --output ./" + str(num) +"/voice")
os.system("python3 googleSTT.py --input ./" + str(num) + "/voice --time ./" + str(num) + "/textData/time.txt --text ./" + str(num) + "/textData/write.txt --count ./" + str(num) + "/voice")
os.system("python3 khaiii_filter.py --input ./" + str(num) + "/textData/write.txt --output ./" + str(num) + "/textData/khaiii.txt")

os.system("mv /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/0.wav /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/mute.wav")

os.system("python3 voice_filter.py --input ./" + str(num) + "/textData/khaiii.txt --time ./" + str(num) + "/textData/time.txt --filter ./" + str(num) + "/textData/filter.txt --audio ./" + str(num) + "/voice_raw/mute.wav")
