import sys, math, argparse, re, os, io
import fasttext
import cs_sim
from google.cloud import vision
from khaiii import KhaiiiApi

model = fasttext.load_model('/home/ubuntu/voice_classification/server/model_skipgram.bin')

def detect_text(path):
    """Detects text in the file."""


    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts[0].description
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

def run_detect(TEXT_FILE, FILE_PATH):
    f = open(TEXT_FILE, "w", encoding="UTF-8")
    list = os.listdir(FILE_PATH)      #"subtitle/"

    for file in list:
        filename = FILE_PATH + file
        #f.write(filename + "\n")
        f.write(str(detect_text(filename)))

    khaiii_tokenize(TEXT_FILE, "/home/ubuntu/voice_classification/khaiii_sub.txt")

def khaiii_tokenize(corpus_fname, output_fname):
    api = KhaiiiApi()

    with open(corpus_fname, 'r', encoding = 'utf-8') as f1, \
            open(output_fname, 'w', encoding = 'utf-8') as f2:
        for line in f1:
            sentence = line.replace('\n', '').strip()
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
      #filter(tokenList, count)
      print(tokenList)

if __name__ == "__main__":

  run_detect("./result.txt", "./subtitle/")