import sys, math, argparse, re
import fasttext
import cs_sim
from cutAudio import mute

model = fasttext.load_model('/home/ubuntu/fastText/mywork/model_test.bin')

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
  swearList = ['시발']
  for token in tokenList:
    for check in swearList:
      similarity = cs_sim.calculate(model.get_word_vector(token), model.get_word_vector(check))
      if (similarity >= 0.7):
       print(similarity)
       stringMatch(token, Line)
       #print(token)

def stringMatch(token,Line):
  f = open('/home/ubuntu/capstone-2020-4/src/textData/result.txt','a')
  #f = open('.\\csv\\result.txt', 'a')
  swearList = ['시발', '씨발', '병신', '좆', '개새끼', '씨발새끼', '새끼', '씨발놈', '씹새끼', '씨부랄', '개씨발']
  for swear in swearList:
    if swear in token:
      f.write(str(Line))
      f.write('\n')
      timeList.append(Line)
      break

def soundFilter(FILE_PATH):
  print(timeList)
  for i in timeList:
    f = open(FILE_PATH, 'r', encoding='utf-8')
    for j, line in enumerate(f):
      if i == (j+1):
        timeLine = line.split('/')
        startT = timeLine[1]
        endT = timeLine[2]
    #mute(".\\voice\\mute.wav",int(startT), int(endT))
    mute("/home/ubuntu/capstone-2020-4/src/voice/mute.wav", int(startT), int(endT))



if __name__ == '__main__':
  count = 0
  timeList = []
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str)
  parser.add_argument('--time', type = str)
  args = parser.parse_args()

  go(args.input)
  soundFilter(args.time)
