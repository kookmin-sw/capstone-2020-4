import sys, math, argparse, re, os, io
import fasttext
import cs_sim
from google.cloud import vision
from khaiii import KhaiiiApi
import natsort
import re, math
from collections import Counter

Word = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = Word.findall(text)
     return Counter(words)


model = fasttext.load_model('/home/ubuntu/voice_classification/server/model_skipgram.bin')

sentence = ""

def detect_text(path, BOUND_PATH, name):
    """Detects text in the file."""

    global sentence
       

    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
#     text1 = 'This is a foo bar sentence .'
#     text2 = 'This sentence is similar to a foo bar sentence .'


    if len(texts) != 0:
        vector1 = text_to_vector(sentence)
        vector2 = text_to_vector(texts[0].description)
        cosine = get_cosine(vector1, vector2)
        
        print(cosine)
        if cosine < 0.6:
            sentence = texts[0].description
            f.write(texts[0].description.replace("\n", " ") + "\n")
            boundfile.write(name + "/")
            for text in texts:
                vertices = (['({},{})'.format(vertex.x, vertex.y)
                         for vertex in text.bounding_poly.vertices])
                boundfile.write(text.description.replace("\n", " ") + "+")
        #         print(text.properties)
                boundfile.write('{}/'.format(' '.join(vertices)))
                 #print(vertices[0])
                print('bounds: {}'.format(','.join(vertices)))
                print(vertices[0])
            boundfile.write("\n")

    
# def detect_bound(path, BOUND_PATH):
#     """Detects text in the file."""
   
#     client = vision.ImageAnnotatorClient()

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     #return vertex[0].replace("\n", " ")
    
#     for text in texts:
#          #f.write("{}".format(text.description))
#          #f.write(text.description) 

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                  for vertex in text.bounding_poly.vertices])
#         f.write(text.description.replace("\n", " ") + "+")
# #         print(text.properties)
#         f.write('{}/'.format(' '.join(vertices)))
#          #print(vertices[0])
#     f.write("\n")
#     if response.error.message:
#          raise Exception(
#              '{}\nFor more info on error messages, check: '
#              'https://cloud.google.com/apis/design/errors'.format(
#                  response.error.message))    
    


def run_detect(TEXT_FILE, FILE_PATH, BOUND_PATH):
    list = os.listdir(FILE_PATH)      #"subtitle/"
    list = natsort.natsorted(list)    

    for file in list:
        if file.endswith("jpg"):
            filename = FILE_PATH + file
            print(filename + "\n")
            try:
              detect_text(filename, BOUND_PATH, file)
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
                f2.write(lines[0] + "/" + component[1] + "\n")
      
        


if __name__ == "__main__":
    timeList = []
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type = str)
    parser.add_argument('--image', type = str)
    parser.add_argument('--bound', type = str)
    parser.add_argument('--khaiii', type = str)
    parser.add_argument('--position', type = str)
    args = parser.parse_args()
#     f = open(args.bound, 'w', encoding = 'utf-8')

    f = open(args.text, "w", encoding="UTF-8")
    boundfile = open(args.bound, "w", encoding="UTF-8")
    run_detect(args.text, args.image, args.bound)
    f.close()
    boundfile.close()
    khaiii_tokenize(args.text, args.khaiii)
    checkBound(args.bound, args.position)
