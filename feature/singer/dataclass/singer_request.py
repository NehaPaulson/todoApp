from dataclasses import dataclass


@dataclass
class SingerRequest:
    singer_name: str | None = None
    age: int | None = None
    years_of_experience: int | None = None
