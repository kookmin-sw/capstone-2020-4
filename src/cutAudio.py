### https://github.com/jiaaro/pydub ###
import os
import librosa
import numpy as np
import wave, array
import math
from pydub import AudioSegment



def cutAudioFile(AUDIO_FILE):
    wav = AUDIO_FILE
    SAMPLE_RATE = 44100
    (file_dir, file_id) = os.path.split(wav)

    y, sr = librosa.load(wav, sr=SAMPLE_RATE)
    time = np.linspace(0, len(y)/sr, len(y)) #time axis
    duration = round(len(y) / float(sr))
    print("duration:", duration)

    time = 5
    tmp =[]
    cut_time = duration
    while (cut_time>5):

        tmp.append(time)
        time+=5
        cut_time-=5
    tmp.append(duration)

    half = len(y) / 2
    y2 = y[:round(half)]
    numOfFile = len(tmp)


    # for i in range(numOfFile):
    #     librosa.output.write_wav('C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile'+str(i)+'.wav',
    #                              y[tmp[i-1]*SAMPLE_RATE:tmp[i]*SAMPLE_RATE], sr)
    librosa.output.write_wav('C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile12.wav',y2, sr, False)


def make_stereo(file1, output):
    ifile = wave.open(file1)
    print(ifile.getparams())
    # (1, 2, 44100, 2013900, 'NONE', 'not compressed')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = ifile.getparams()
    assert comptype == 'NONE' # Compressed not supported yet
    array_type = {1:'B', 2: 'h', 4: 'l'}[sampwidth]
    left_channel = array.array(array_type, ifile.readframes(nframes))[::nchannels]
    ifile.close()

    stereo = 2 * left_channel
    stereo[0::2] = stereo[1::2] = left_channel

    ofile = wave.open(output, 'w')
    ofile.setparams((2, sampwidth, framerate, nframes, comptype, compname))
    ofile.writeframes(stereo.tostring())
    ofile.close()


def cutting(AUDIO_FILE):
    wav = AudioSegment.from_wav(AUDIO_FILE)
    lenOfWav = wav.duration_seconds

    ten_seconds = 10 * 1000
    five_seconds = 5 * 1000
    fifty_seconds = ten_seconds * 5
    one_min = ten_seconds * 6

    first_10_seconds = wav[:ten_seconds*2]
    first_5_seconds = wav[0:five_seconds]
    middle = wav[ten_seconds:ten_seconds*2]
    last_5_seconds = wav[-5000:]
    beginning = first_5_seconds


    #print(math.trunc(lenOfWav/50))
    for i in range(math.trunc(lenOfWav/50)+1):
        print(i)
        #section = wav[five_seconds*i:five_seconds*(i+1)]
        section = wav[fifty_seconds*i:fifty_seconds*(i+1)]
        section.export("C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile"+str(i)+".wav", format = 'wav')
        #section.export("/home/ubuntu/capstone-2020-4/src/voice/cutfile" + str(i) + ".wav", format='wav')

    # beginning.export("C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile888.wav", format = 'wav')


def countFile(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1

  return count


#make_stereo("C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile2.wav", "stereo.wav")
# cutAudioFile("test07.wav")
#cutting("sin.wav")

#countFile("C:\\Users\\01097\\PycharmProjects\\untitled\\voice", ".wav")