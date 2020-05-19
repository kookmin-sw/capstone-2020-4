import moviepy.editor as mp
import sys, math, argparse, re

def video2voice(IN_PATH, OUT_PATH):
    #clip = mp.VideoFileClip("C:\\Users\\01097\\PycharmProjects\\untitled\\video\\"+VIDEO_FILE)
    #clip.audio.write_audiofile("C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\test10.wav")

    clip = mp.VideoFileClip(IN_PATH)
    clip.audio.write_audiofile(OUT_PATH)

    print("finished extract voice")

if __name__ == '__main__':
  count = 0
  timeList = []
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str)
  parser.add_argument('--output', type = str)
  args = parser.parse_args()

  video2voice(args.input, args.output)



