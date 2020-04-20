#dddddsfasdf
from khaiii import KhaiiiApi

api = KhaiiiApi("", "")

def filterKhaiii(FILEPATH, DESTINATION):
    f = open('FILEPATH', 'r')
    des = open('DESTINATION', 'a')
    while True:
        line = f.readline()
        for word in api.analyze(line):
            f.write(word)
        f.write("\n")

        if line=="":
            break




