import speech_recognition as sr

from audio import audio

r = sr.Recognizer()

"""
def transcribe(audio: object):
    if audio.lang != None:
        with audio() as source:
            r.recognize_google(audio_data=r.record(source))
            print(audio.lang)
    else:
        raise Exception("Specify language for inputed audio")
    

clip = audio(file_path="C:/Users/willi/OneDrive - Fulton County Schools/Research Projects/Programming Projets/VirtuallyFree/Sp 3 M1HermanoAudio.mp3", lang="es")
transcribe(clip)
"""

harvard = sr.AudioFile('C:/Users/willi/OneDrive - Fulton County Schools/Research Projects/Programming Projets/VirtuallyFree/Sp 3 M1HermanoAudio.wav')
with harvard as source:
    audio = r.record(source)
    print(r.recognize_google(audio))