from pydub import AudioSegment

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

# Gets audio from remote address and returs pydub AudioSegment object
def audio_from_remote(url):
    pass