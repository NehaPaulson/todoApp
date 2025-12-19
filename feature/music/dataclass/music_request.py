from dataclasses import dataclass

@dataclass
class MusicRequest:
    song_name: str
    description: str | None = None
    singer: str | None = None
