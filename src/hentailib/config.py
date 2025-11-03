#import os
#from dataclasses import dataclass
#from dotenv import load_dotenv

#load_dotenv()


#@dataclass
#class Confing:
    #LOGGING_LEVEL: str

    #@classmethod
    #def from_env(cls):
        #return cls(
        #LOGGING_LEVEL=os.getenv("LOGGING_LEVEL")
        #)