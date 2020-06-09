#-*- coding:utf-8 -*-

import os
import sys

str = (sys.argv[1]).split('.')[0]
print(str)

os.system("aws s3 cp s3://uploadtest-s3/" + sys.argv[1] + " ./")
os.system("mkdir " + str)
os.system("aws s3 cp s3://youhi-project/" + str + " ./" + str+ "  --recursive")
os.system("python3.6 object_detect.py --video " + sys.argv[1])
#os.system("python ../main.py --dir " + sys.argv[1])



