from audio import *
from get_audio import *
import speech_recognition as sr

def text_from_wav_bytes(wav_bytes, lang):
    detection = sr.AudioFile(wav_bytes)
    r = sr.Recognizer()

    with detection as source:
        output = r.record(source)
        return r.recognize_google(output, language=f'{lang}-in')

def text_from_wav_file(path, lang):
    r = sr.Recognizer()

    with path as source:
        span_audio = r.record(source)
        return r.recognize_google(span_audio, language=f"{lang}-in")





# Returns pydub audiosegment
input_source = audio_from_local("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
# Initialized audio class
audio_sample = audio(sound=input_source)
audio_bytes = audio_sample.to_wav_bytes()
detection = sr.AudioFile(audio_bytes)
    
r = sr.Recognizer()
with detection as source:
    output = r.record(source)

word = r.recognize_google(output, language='es-in')
print(word)

"""
speech_reconizer_audio = sr.AudioData(frame_data=audio_bytes, sample_rate=audio_sample.sound.frame_rate, sample_width=audio_sample.sound.sample_width)
print(type(audio_bytes))
"""

"""
with open("test.wav", "w+") as f:
    f.write(str(speech_reconizer_audio.get_wav_data()))
    f.close()
"""

"""
r = sr.Recognizer()
print(speech_reconizer_audio)
# print(r.recognize_google(speech_reconizer_audio, language=f"es-in"))
"""

