from audio import *
from pysondb import db


class audioDatabase:
    def __init__(self) -> None:
        self.path = "backend/data/audio"
        self.format_que = db.getDb("backend/data/audio/format_que.json")
        self.transcribe_que = db.getDb("backend/data/audio/transcribe_que.json")

    def add_to_format_que(self):
        pass

    def add_to_transcribe_que(self):
        pass

audioDatabase()