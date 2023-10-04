from pydub import AudioSegment

def format_audio(file_path):
    filetype = file_path.split(".")[-1]
    print(filetype)
    if filetype == "mp3":
        sound = AudioSegment.from_mp3(file_path)
    else:
        raise Exception("Input valid audio type")

