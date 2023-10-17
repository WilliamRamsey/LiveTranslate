

def format_audio_file(path):
    pass


class audio:
    def __init__(self, id = None, lang = None, path = None, local_addr = None, remote_addr = None) -> None:
        self.id = id
        self.lang = lang
        self.path = path
        self.local_addr = local_addr
        self.remote_addr = remote_addr

        # If id is specified:
        # For calling data from database
        if self.id is not None:
            # Adds all the known info in the class to pysondb
            # Populates class from pyson db
            # Breaks and runs the other stuff
            pass
        
        # if path is specified ()
        if path is not None and lang is not None:
            pass

        # If remote address is specified
        elif self.remote_addr is not None:
            # Runs function to pull audio from canvas

            # Formats audio as .wav and saves to database
            # Updates path variable and pysondb
            
            # if there is a language specified
            if self.lang is not None:
                # update pysondb with lang
                pass
            
            # if no language specified
            else:
                # sets lang to auto
                # self.lang = "auto"
                pass
            pass
        
        # if local filepath specified
        elif self.local_addr is not None:
            # Formats audio as .wav and saves to database
            # Updates path variable and pyson db

            if self.lang is not None:
                # update pysondb with lang
                pass
            
            # if no language specified
            else:
                # sets lang to auto
                # self.lang = "auto"
                pass
            pass

        else:
            raise Exception("Please specify an id, local_address, path, or remote_address")
        

        