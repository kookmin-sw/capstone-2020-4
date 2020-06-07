import requests
import argparse

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()

try:
    url = 'http://ec2-13-209-93-181.ap-northeast-2.compute.amazonaws.com/YouHi-Wep/upload.php'
    files = {'myfile': open(args.dir, 'rb')}
    r = requests.post(url, files=files)
except:
    print("")
