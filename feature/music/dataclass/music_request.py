from dataclasses import dataclass
from typing import Optional


@dataclass
class MusicRequest:
    song_name: Optional[str] = None
    description: Optional[str] = None
    singer: Optional[str] = None

