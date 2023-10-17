import io
from pydub import AudioSegment
import speech_recognition as sr

"""from get_audio import *"""

class audio:
    def __init__(self, sound=None, lang=None) -> None:
        self.sound = sound
        self.lang = lang
        self.sr_sound = None
    
    """
    really needs to be an outside function.
    """
    def to_sr(self):
        # Buffer object to hold the bytes
        wav_buffer = io.BytesIO()
        # Takee the pydub sound object and turns it into .wav bytes
        self.sound.export(wav_buffer, format="wav")
        # Eats .wav bytes and shits out soundreconition audio file object
        self.sr_sound = sr.AudioFile(wav_buffer)
        # Closes buffer to prevent ram blackwhole.
        # wav_buffer.close()
    
    def transcribe(self):
        # If to_sr hasn't already been run
        if self.sr_sound is None:
            self.to_sr()
        
        r = sr.Recognizer()
        with self.sr_sound as source:
            output = r.record(source)
            return r.recognize_google(output, language=f'{self.lang}-in')
        
    def to_wav_bytes(self):
        wav_buffer = io.BytesIO()
        self.sound.export(wav_buffer, format="wav")
        return wav_buffer

"""
input_source = audio_from_local("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
audio_sample = audio(sound=input_source)
print(audio_sample.to_wav_bytes())
"""