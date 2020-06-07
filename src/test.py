from khaiii import KhaiiiApi
#import sys
#sys.path.append("/home/ubuntu/khaiii/build/package_python/khaiii/")
#from khaiii import KhaiiiApi

api = KhaiiiApi('/usr/local/lib/libkhaiii.so','/usr/local/lib/python3.5/dist-packages/khaiii/share/khaiii')

def filterKhaiii(FILEPATH, DESTINATION):
    f = open(FILEPATH, 'r')
    des = open(DESTINATION, 'a')
    while True:
        line = f.readline()
        for word in api.analyze(line):
            des.write(str(word))
        des.write("\n")

        if line=="":
            break


filterKhaiii('/home/ubuntu/capstone-2020-4/src/textData/write.txt', '/home/ubuntu/capstone-2020-4/src/textData/khaiii.txt')

