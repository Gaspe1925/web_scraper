from datetime import date
from enum import Enum


class Tag(Enum):
    NIL = 0
    MACBOOK_PRO = 1
    IRON_WOLF = 2
    B_580 = 3
    B_580_OC = 4
    DIAPER_SIZE_5 = 5


class Product:
    url: str = ""
    description: str = ""
    price: float = 0
    quantity: float = 0
    date = date.today()
    tag: str = Tag.NIL.name
    hasError = False

    def __init__(self, url, quantity, tag: Tag) -> None:
        self.url = url
        self.quantity = quantity
        self.tag = tag.name

    def price_per(self):
        result = self.price / self.quantity
        return result
