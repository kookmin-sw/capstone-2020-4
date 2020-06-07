# !/usr/bin/env python3
import sys, math, argparse, re
import fasttext
import cs_sim
from cutAudio import mute

model = fasttext.load_model('/home/ubuntu/voice_classification/server/model_skipgram.bin')

def go(tokenized_khaiii_fname):
  count = 0
  with open(tokenized_khaiii_fname, 'r', encoding='utf-8') as f1:
    for line in f1:
      count = count + 1
      tokenList = line.split()
      for i in range(0, len(tokenList)):
        cutPos = tokenList[i].find('/')
        tokenList[i] = tokenList[i][0:cutPos] #tokenList에는 한글 형태소만 들어있음.
      filter(tokenList, count)
      #print(tokenList)

def filter(tokenList, Line):
  swearList = ['씨발']
  for token in tokenList:
    for check in swearList:
      similarity = cs_sim.calculate(model.get_word_vector(token), model.get_word_vector(check))
      if (similarity >= 0.55):
          stringMatch(token, Line)
       #print(token)

def stringMatch(token,Line):
  #f = open('/home/ubuntu/voice_classification/textData/number.txt','a')
  swearList = ['시발', '씨발', '병신', '좆', '개새끼', '씨발새끼', '새끼', '씨발놈', '씹새끼', '씨부랄', '개씨발', '딸치', '따먹다', '따먹', '씨빨', '시발새끼', '존나', '년', '련', '지랄']
  for swear in swearList:
    if swear in token:
      #f.write(str(Line))
      #f.write('\n')
      timeList.append(Line)
      break

def soundFilter(FILE_PATH, OUT_PATH, AUDIO):
  print(timeList)
  f1 = open(OUT_PATH, 'a', encoding='utf-8')
  for i in timeList:
    f2 = open(FILE_PATH, 'r', encoding='utf-8')
    for j, line in enumerate(f2):
      if i == (j+1):
        timeLine = line.split('/')
        sentence = timeLine[0]
        startT = timeLine[1]
        endT = timeLine[2]
        f1.write(str(sentence) + " / " + calc_time(startT, endT))
        f1.write('\n')
        #mute(".\\voice\\mute.wav",int(startT), int(endT))
        mute(AUDIO, int(startT), int(endT))


def calc_time(startT, endT):
    start_min = int((int(startT) / 1000) / 60)
    start_sec = int((int(startT) / 1000) % 60)
    end_min = int((int(endT) / 1000) / 60)
    end_sec = int((int(endT) / 1000) % 60)

    if(start_min >= 0 and start_min <= 9):
        start_min = "0" + str(start_min)
    else:
        start_min = str(start_min)

    if(start_sec >= 0 and start_sec <= 9):
        start_sec = "0" + str(start_sec)
    else:
        start_sec = str(start_sec)

    if(end_min >= 0 and end_min <= 9):
        end_min = "0" + str(end_min)
    else:
        end_min = str(end_min)

    if(end_sec >= 0 and end_sec <=9):
        end_sec = "0" + str(end_sec)
    else:
        end_sec = str(end_sec)

    return start_min + ":" + start_sec + "~" + end_min + ":" + end_sec

if __name__ == '__main__':
  count = 0
  timeList = []
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str)
  parser.add_argument('--time', type = str)
  parser.add_argument('--filter', type=str)
  parser.add_argument('--audio', type=str)
  args = parser.parse_args()

  go(args.input)
  soundFilter(args.time, args.filter, args.audio)
