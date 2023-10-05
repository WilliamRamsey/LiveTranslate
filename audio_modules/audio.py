from pydub import AudioSegment
import speech_recognition as sr

# Class holding any audio files to be transcribed or translated
# sound = pydub sound object, there mainly for internal development (optional)
# file_path = 
# lang = 2 letter abreviation for origional language of the clip

class audio:
    def __init__(self, sound=None, file_path=None, lang=None) -> None:
        self.sound = sound
        self.file_path = file_path
        self.lang = lang

    def __call__(self):
        return sr.AudioFile(self.file_path)
    
    def format_audio(self):
            filetype = self.file_path.split(".")[-1]
            name = self.file_path.split(".")[0]

            if filetype == "mp3":
                sound = AudioSegment.from_mp3(self.file_path)
                self.sound = sound
                sound.export(f"{name}.wav", format="wav")
                file_path = f"{name}.wav"
                self.file_path=file_path
            else:
                raise Exception("Input valid audio file format to audio.format_audio(filetype=...)")


clip = audio(file_path="C:/Users/willi/OneDrive - Fulton County Schools/Research Projects/Programming Projets/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
clip.format_audio()
