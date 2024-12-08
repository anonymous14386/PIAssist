from ollama import chat
from ollama import ChatResponse

import pyaudio
import wave
import speech_recognition as sr
import os

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

import espeak
import pyttsx3

language = 'en'

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second

secondsIn = input("How many seconds of audio?: ")
seconds = int(secondsIn)

filenamein = input("File name?: ")

filename = filenamein + ".wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

# Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

r = sr.Recognizer()

voiceIn=sr.AudioFile(filename)
with voiceIn as source:
    audio = r.record(source)
try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))

response: ChatResponse = chat(model='gemma2:2b', messages=[
        {
                'role': 'user',
                'content': s + "",
        },
])

#ans = response['message']['content'].encode('utf-8')
ans = response['message']['content']

print(ans)

command = "espeak-ng " + str(ans)

print(command)

os.system("espeak-ng " + str("'%s'" % ans))
#speaker = espeak
#speaker.say(response['message']['content'])
