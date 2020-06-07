import requests
import argparse

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()

try:
    url = 'your-instance-url/upload.php'
    files = {'myfile': open(args.dir, 'rb')}
    r = requests.post(url, files=files)
except:
    print("")
