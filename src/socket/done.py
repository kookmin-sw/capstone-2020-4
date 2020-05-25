import os
import argparse
import socketio

parser = argparse.ArgumentParser(description='Argparse Tutorial')
parser.add_argument('--dir', type=str,
                    help='an integer for printing repeatably')

args = parser.parse_args()

sio = socketio.Client()
sio.connect('http://13.209.93.181:4567')
sio.emit('voice', args.dir)
sio.sleep(1)
sio.disconnect()
