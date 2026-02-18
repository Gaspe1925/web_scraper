from datetime import date
from enum import Enum


class Tag(Enum):
    NIL = 0
    IRON_WOLF = 1
    B_580 = 2
    B_580_OC = 3


class Product:
    url = ""
    description = ""
    price = 0
    date = date.today()
    tag: str = Tag.NIL.name
    hasError = False

    def __init__(self, url, tag: Tag) -> None:
        self.url = url
        self.tag = tag.name
