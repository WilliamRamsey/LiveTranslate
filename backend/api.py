from flask import Flask
from flask import request

from audio_modules.audio import audio
from audio_modules.get_audio import audio_from_local
from translation.translator import translator


app = Flask(__name__)


# Text to text
@app.route('/api/translation/text', methods=['POST', 'GET'])
def text_to_text():
    # Gets languages from URL parameters if specified in request
    lang_in = request.args.get("lang_in")
    lang_out = request.args.get("lang_out")

    # If parameters are not specified sets them to NoneType
    if lang_in == "none":
        lang_in = None
    if lang_out == "none":
        lang_out = None
    
    # Gets text to translate
    text = request.data
    text = text.decode('utf-8')

    # Translating the text
    juan = translator(lang_in=lang_in, lang_out=lang_out)
    translation = juan.translate_text(text)

    return translation



# Speach to text
@app.route('/api/translation/audio')
def audio_to_text():
    pass

app.run(port=5500)

