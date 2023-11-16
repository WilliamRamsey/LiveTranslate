from pydub import AudioSegment
from pydub.playback import play
import io

def audio_from_bytes(data, file_type="mp3"):
    sound = AudioSegment.from_file(io.BytesIO(data), format=file_type)
    return sound

# Gets audio from local file and returns pydub AudioSegment object
def audio_from_local(path):
    filetype = path.split(".")[-1]

    if filetype == "mp3":
        sound = AudioSegment.from_mp3(path)
        return sound
    
    elif filetype == "wav":
        sound = AudioSegment.from_wav(path)
        return sound
    
    else:
        print("Only .mp3 and .wav files are currently supported")
        raise Exception("Input valid audio file format to audio.format_audio(file_path=...)")

"""
thing = audio_from_local("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.mp3")
thing.export("C:/Users/willi/OneDrive/Desktop/VirtuallyFree/Sp 3 M1 Audio Test 1.wav", format="wav")
"""