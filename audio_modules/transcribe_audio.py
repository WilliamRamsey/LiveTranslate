import speech_recognition as sr

from audio import audio

r = sr.Recognizer()


def transcribe(audio_in: object):
    if audio_in.lang != None:
        with audio_in() as source:
            try:
                span_audio = r.record(source)
                return r.recognize_google(span_audio, language=f"{audio_in.lang}-in")
            except Exception as e:
                return e
    else:
        raise Exception("Specify language for inputed audio")
    
"""
clip = audio(file_path="C:/Users/willi/OneDrive - Fulton County Schools/Research Projects/Programming Projets/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3", lang="es")
clip.format_audio()
print(transcribe(clip))
"""