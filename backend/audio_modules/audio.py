import io
from pydub import AudioSegment

from get_audio import *

class audio:
    def __init__(self, sound=None, lang=None) -> None:
        self.sound = sound
        self.lang = lang
    
    def to_wav_bytes(self):
        wav_buffer = io.BytesIO()
        self.sound.export(wav_buffer, format="wav")
        return wav_buffer

"""
input_source = audio_from_local("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
audio_sample = audio(sound=input_source)
print(audio_sample.to_wav_bytes())
"""