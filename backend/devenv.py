from audio_modules.audio import audio
from audio_modules.get_audio import audio_from_local
from translation.translator import translator

# Transcribe an audio file
audio_file = audio_from_local("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
speaking_clip = audio(sound=audio_file, lang="es")
speaking_clip.to_sr()
text = speaking_clip.transcribe()


# Translate text to english
juan = translator(lang_in="es", lang_out="en")

print(text)
print(juan.translate_text(text))

