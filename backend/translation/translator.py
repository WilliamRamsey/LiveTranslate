from deep_translator import GoogleTranslator
from audio_modules import *

class translator:
    def __init__(self, lang_in =  None, lang_out = None) -> None:
        self.lang_in = lang_in
        self.lang_out = lang_out

        if self.lang_in is None:
            self.lang_in = "auto"
        if self.lang_out is None:
            self.lang_out = "en"
        
    def translate_text(self, string_in: str):
        return GoogleTranslator(source=self.lang_in, target=self.lang_out).translate(string_in)
    
    def translate_audio(self, audio_in: object):
        pass


"""
output = Translator(lang_in="en", lang_out="es").translate_text("Hello World")
print(output)
"""