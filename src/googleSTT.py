#-*-coding:utf-8-*-
import io
import os
import json
import sys, math, argparse, re
#from cutAudio import cutAudioFile
import wave
from cutAudio import countFile
from makeData import writeCSV
from makeData import writeTXT
from makeData import stampTime
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.cloud import speech_v1

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

def sample_long_running_recognize(local_file_path, time_path, text_path, num):
        """
        Print start and end time of each word spoken in audio file from Cloud Storage

        Args:
          storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
        """

        client = speech_v1.SpeechClient()
        

        # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.flac'

        # When enabled, the first result returned by the API will include a list
        # of words and the start and end time offsets (timestamps) for those words.
        enable_word_time_offsets = True

        # The language of the supplied audio
        language_code = "ko-KR"
        config = types.RecognitionConfig(
            enable_word_time_offsets = True,
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='ko-KR',
            audio_channel_count=2

        )
        with io.open(local_file_path, "rb") as f:
            content = f.read()
        audio = {"content": content}

        operation = client.long_running_recognize(config, audio)

        print(u"Waiting for operation to complete...")
        response = operation.result()
        
        for result in response.results:
            # The first result includes start and end time word offsets
            #result = response.results[0]
            # First alternative is the most probable result
            alternative = result.alternatives[0]
            print(u"Transcript: {}".format(alternative.transcript))
            # Print the start and end time of each word
            for word in alternative.words:
                print(u"Word: {}".format(word.word))
                print(
                    u"Start time: {} seconds {} nanos".format(
                        word.start_time.seconds, word.start_time.nanos
                    )
                )
                print(
                    u"End time: {} seconds {} nanos".format(
                        word.end_time.seconds, word.end_time.nanos
                    )
                )
            for word in alternative.words:
                stampTime(time_path, word.word, word.start_time.seconds, word.start_time.nanos, word.end_time.seconds, word.end_time.nanos, num)
                writeTXT(word.word, text_path)


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


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--input', type=str)
  parser.add_argument('--time', type = str)
  parser.add_argument('--text', type = str)
  parser.add_argument('--count', type = str)
  args = parser.parse_args()

  num = countFile(args.count, '.wav')
  for i in range(num):
      sample_long_running_recognize(args.input +"/cutfile"+ str(i) + '.wav', args.time, args.text, i)

  print("finished Speech To Text")
