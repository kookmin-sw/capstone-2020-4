#-*-coding:utf-8-*-
import io
import os
import json
#from cutAudio import cutAudioFile
import wave
from cutAudio import countFile
from makeData import writeCSV
from makeData import writeTXT
from makeData import printTime
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def frame_rate_channel(audio_file_name):
    print(audio_file_name)
    with wave.open(audio_file_name, "r") as wave_file:
        frame_rate = wave_file.getframerate()
        channels = wave_file.getnchannels()
        return frame_rate,channels

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""

    client = speech.SpeechClient()
    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='ko-KR',
        audio_channel_count=2)
    operation = client.long_running_recognize(config, audio)
    print('Waiting for operation to complete...')
    response = operation.result(timeout=90)
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        #print('Confidence: {}'.format(result.alternatives[0].confidence))
        #writeCSV(result.alternatives[0].transcript)  #save csv file

def sample_recognize(local_file_path):
    """
    Transcribe a short audio file using synchronous speech recognition

    Args:
      local_file_path Path to local audio file, e.g. /path/audio.wav
    """

    client = speech.SpeechClient()

    # local_file_path = 'resources/brooklyn_bridge.raw'

    # The language of the supplied audio
    language_code = "ko-KR"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='ko-KR',
        audio_channel_count=2)

    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]

        print(u"Transcript: {}".format(alternative.transcript))
        #writeCSV(result.alternatives[0].transcript)  #save csv file
        writeTXT(result.alternatives[0].transcript)  # save txt file

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client('sunlit-liberty-268205')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


#implicit()
#transcribe_gcs('gs://youtubespeech/theaudio.wav')

#num = countFile('C:\\Users\\01097\\PycharmProjects\\untitled\\voice', '.wav')
num = countFile('/home/ubuntu/capstone-2020-4/src/voice', '.wav')
for i in range(num):
    #printTime(i)
    #sample_recognize('C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile' + str(i) + '.wav')
    sample_recognize('/home/ubuntu/capstone-2020-4/src/voice/cutfile' + str(i) + '.wav')
# sample_recognize('C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile888.wav')
# print(frame_rate_channel('C:\\Users\\01097\\PycharmProjects\\untitled\\voice\\cutfile12.wav'))