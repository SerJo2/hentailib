import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Confing:
    API_TOKEN: str
    USER_ID: str
    LOGGING_LEVEL: str

    @classmethod
    def from_env(cls):
        return cls(
        API_TOKEN=os.getenv("HENTAILIB_API_TOKEN"),
        USER_ID=os.getenv("HENTAILIB_USER_ID"),
        LOGGING_LEVEL=os.getenv("LOGGING_LEVEL")
        )