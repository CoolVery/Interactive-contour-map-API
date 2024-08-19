from typing import List

from pydantic import BaseModel

class City(BaseModel):
    city_name: str
    coordinates: str
    isSpecial: bool


class Event_Areas(BaseModel):
    _id: str
    id_event: int
    name_event: str
    cities: List[City]
