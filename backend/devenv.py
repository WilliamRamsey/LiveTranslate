from audio_modules.audio import *
from audio_modules.get_audio import *

audio_file = audio_from_local("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
speaking_clip = audio(sound=audio_file)
speaking_clip.to_sr()
print(speaking_clip.transcribe())


