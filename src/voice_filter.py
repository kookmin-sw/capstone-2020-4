import sys, math, argparse, re
import fasttext
import cs_sim

def go(tokenized_khaiii_fname):
  with open(tokenized_khaiii_fname, 'r', encoding='utf-8') as f1:
    for line in f1:
      tokenList = line.split()
      for i in range(0, len(tokenList)):
        cutPos = tokenList[i].find('/')
        tokenList[i] = tokenList[i][0:cutPos] #tokenList에는 한글 형태소만 들어있음.
      filter(tokenList)
      #print(tokenList)

def filter(tokenList):
  swearList = ['시발', '씨발', '병신', '좆','개새끼','씨발새끼','새끼','씨발놈','씹새끼','씨부랄','개씨발']
  model = fasttext.load_model('/home/ubuntu/fastText/mywork/model_test.bin')
  for token in tokenList:
    for check in swearList:
      similarity = cs_sim.calculate(model.get_word_vector(token), model.get_word_vector(check))
      if (similarity >= 0.7):
       stringMatch(token, swearList)
       #print(token)

def stringMatch(token,swearList):
  f = open('/home/ubuntu/capstone-2020-4/src/textData/result.txt','a')
  for swear in swearList:
    if swear in token:
      print(swear)
      f.write(swear)
      f.write('\n')
      #sys.exit()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str)
  args = parser.parse_args()

  go(args.input)
