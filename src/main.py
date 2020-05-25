import os
import sys, math, argparse, re
#import fasttext
import cs_sim, googleSTT, video2voice, voice_filter, khaiii_filter, makeData, cutAudio
import socketio

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()
print(args.dir)
#os.system("export GOOGLE_APPLICATION_CREDENTIALS=\"/home/ubuntu/voice_classification/capstone.json\"")

num = args.dir.split(".")[0]

os.system("mkdir " + "/home/ubuntu/voice_classification/" + str(num)) 
os.system("mkdir " + "/home/ubuntu/voice_classification/" + str(num) + "/textData")
os.system("mkdir " + "/home/ubuntu/voice_classification/" + str(num) + "/voice_raw")
os.system("mkdir " + "/home/ubuntu/voice_classification/" + str(num) + "/voice")
os.system("mkdir " + "/home/ubuntu/voice_classification/" + str(num) + "/video")

os.system("cp /home/ubuntu/voice_classification/server/" + args.dir +" /home/ubuntu/voice_classification/" + str(num) + "/video")
#os.system("cp /home/ubuntu/voice_classification/" + args.dir + " /home/ubuntu/voice_classification/" + str(num) + "/video")

os.system("python /home/ubuntu/voice_classification/video2voice.py --input /home/ubuntu/voice_classification/" + str(num) + "/video/" + args.dir + " --output /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/0.wav & python /home/ubuntu/voice_classification/image2text.py --text /home/ubuntu/voice_classification/" + str(num) + "/textData/result.txt --image /home/ubuntu/voice_classification/server/" + str(num) + "/" + " --bound /home/ubuntu/voice_classification/" + str(num) + "/textData/bound.txt --khaiii /home/ubuntu/voice_classification/" + str(num) + "/textData/khaiii_sub.txt --position /home/ubuntu/voice_classification/" + str(num) + "/textData/" + str(num) + "_subtitle_result.txt")
os.system("python /home/ubuntu/voice_classification/cutAudio.py --input /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/0.wav --output /home/ubuntu/voice_classification/" + str(num) +"/voice")
os.system("python3 /home/ubuntu/voice_classification/googleSTT.py --input /home/ubuntu/voice_classification/" + str(num) + "/voice --time /home/ubuntu/voice_classification/" + str(num) + "/textData/time.txt --text /home/ubuntu/voice_classification/" + str(num) + "/textData/write.txt --count /home/ubuntu/voice_classification/" + str(num) + "/voice")
os.system("python3 /home/ubuntu/voice_classification/khaiii_filter.py --input /home/ubuntu/voice_classification/" + str(num) + "/textData/write.txt --output /home/ubuntu/voice_classification/" + str(num) + "/textData/khaiii.txt")

os.system("mv /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/0.wav /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/mute.wav")

os.system("python3 /home/ubuntu/voice_classification/voice_filter.py --input /home/ubuntu/voice_classification/" + str(num) + "/textData/khaiii.txt --time /home/ubuntu/voice_classification/" + str(num) + "/textData/time.txt --filter /home/ubuntu/voice_classification/" + str(num) + "/textData/filter.txt --audio /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/mute.wav")


      
os.system("python /home/ubuntu/voice_classification/server/upload.py --dir /home/ubuntu/voice_classification/" + str(num) + "/textData/" + str(num) + "_subtitle_result.txt")
os.system("python /home/ubuntu/voice_classification/server/upload.py --dir /home/ubuntu/voice_classification/" + str(num) + "/textData/filter.txt")
os.system("python /home/ubuntu/voice_classification/server/upload.py --dir /home/ubuntu/voice_classification/" + str(num) + "/voice_raw/mute.wav")

sio = socketio.Client()
sio.connect('http://13.209.93.181:4567')
sio.emit('voice', args.dir)
sio.sleep(1)
sio.disconnect()

