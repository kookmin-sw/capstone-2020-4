import sys, math, argparse, re, os, io
import fasttext
import cs_sim
from google.cloud import vision
from khaiii import KhaiiiApi
import natsort

model = fasttext.load_model('/home/ubuntu/voice_classification/server/model_skipgram.bin')

def detect_text(path):
    """Detects text in the file."""


    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description.replace("\n", " ")
    #
    # for text in texts:
    #     print("{}".format(text.description))

        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        #
        # print('bounds: {}'.format(','.join(vertices)))
        # print(vertices[0])

    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))
    
def detect_bound(path, BOUND_PATH):
    """Detects text in the file."""
   
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #return vertex[0].replace("\n", " ")
    
    for text in texts:
         #f.write("{}".format(text.description))
         #f.write(text.description) 

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                 for vertex in text.bounding_poly.vertices])
        f.write(text.description.replace("\n", " ") + "+")
#         print(text.properties)
        f.write('{}/'.format(','.join(vertices)))
         #print(vertices[0])
    f.write("\n")
    if response.error.message:
         raise Exception(
             '{}\nFor more info on error messages, check: '
             'https://cloud.google.com/apis/design/errors'.format(
                 response.error.message))    
    


def run_detect(TEXT_FILE, FILE_PATH, BOUND_PATH):
    f = open(TEXT_FILE, "w", encoding="UTF-8")
    list = os.listdir(FILE_PATH)      #"subtitle/"
    list = natsort.natsorted(list)    

    for file in list:
        if file.endswitch("jpg"):
            filename = FILE_PATH + file
            print(filename + "\n")
            try:
              f.write(str(detect_text(filename))+ "\n")
              detect_bound(filename, BOUND_PATH)
            except IsADirectoryError:
              print("directory Except")

    #khaiii_tokenize("./result.txt", "./khaiii_sub.txt")

def khaiii_tokenize(corpus_fname, output_fname):
    api = KhaiiiApi()
    print("ll")

    with open(corpus_fname, 'r', encoding = 'utf-8') as f1, \
            open(output_fname, 'w', encoding = 'utf-8') as f2:
        for line in f1:
            sentence = line.replace('\n', '').strip()
            print(sentence)
            tokens = api.analyze(sentence)
            tokenized_sent = ''
            for token in tokens:
                tokenized_sent += ' '.join([str(m) for m in token.morphs]) + ' '
            f2.writelines(tokenized_sent.strip() + '\n')

    go(output_fname)

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
  swearList = ['새끼']
  for token in tokenList:
    for check in swearList:
      similarity = cs_sim.calculate(model.get_word_vector(token), model.get_word_vector(check))
      if (similarity >= 0.6):
       print(similarity)
       stringMatch(token, Line)

def stringMatch(token,Line):
  #f = open('/home/ubuntu/voice_classification/textData/number.txt','a')
  swearList = ['시발', '씨발', '병신', '좆', '개새끼', '씨발새끼', '새끼', '씨발놈', '씹새끼', '씨부랄', '개씨발', '딸치']
  for swear in swearList:
    if swear in token:
      #f.write(str(Line))
      #f.write('\n')
      print(token)
      timeList.append(str(Line) +'/'+ token)
      break

def checkBound(BOUND_PATH, OUT_PATH):
    f2 = open(OUT_PATH, 'w', encoding = 'utf-8')
  #for i in range(len(timeList))
    for i in timeList:
        f3 = open(BOUND_PATH, 'r', encoding = 'utf-8')
        boundPoint = i.split('/')
        imgNum = boundPoint[0]
        word = boundPoint[1]
        for x in range(int(imgNum) - 1):
            temp = f3.readline()
        line = f3.readline()
        lines = line.split("/")
        lines.remove('\n')
        for components in lines:
            component = components.split("+")
            if component[0] in word and components != lines[0]:
                print(imgNum + "/" + component[1])
                f2.write(imgNum + "/" + component[1] + "\n")
      
        


if __name__ == "__main__":
    timeList = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type = str)
    parser.add_argument('--image', type = str)
    parser.add_argument('--bound', type = str)
    parser.add_arguemnt('--khaiii', type = str)
    parser.add_arguemnt('--position', type = str)
    f = open(args.bound, 'w', encoding = 'utf-8')
    run_detect(args.text, args.image, args.bound)
    f.close()
    khaiii_tokenize(args.text, args.khaiii)
    checkBound(args.bound, args.position)
