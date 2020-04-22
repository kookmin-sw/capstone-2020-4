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

def filter(tokenList):
  swearList = ['시발', '씨발', '병신', '좆']
  #model = fasttext.load_model('./model_skipgram.bin')
  for token in tokenList:
    for check in swearList:
      similarity = cs_sim.calculate(model.get_word_vector(token), model.get_word_vector(check)))
      if (similarity >= 0.7):
        stringMatch(token, swearList)

def stringMatch(token, swearList):
  for swear in swearList:
    if swear in token:
      print("Swear detected!")
      sys.exit()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str)
  args = parser.parse_args()

  go(args.input)
