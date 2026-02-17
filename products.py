import globals
import product
from product import Tag


def get_list():
    return [
        product.Product(
            "https://www.memoryexpress.com/Products/MX00120891", Tag.IRON_WOLF
        ),
        product.Product(
            "https://www.memoryexpress.com/Products/MX00132129", Tag.B_580_OC
        ),
        product.Product(
            "https://www.memoryexpress.com/Products/MX00132128", Tag.B_580_OC
        ),
        product.Product("https://www.memoryexpress.com/Products/MX00132130", Tag.B_580),
    ]


def print_products(products):
    for item in products:
        print(globals.DASH_LINE)
        print(f"description: {item.description}")
        print(f"price:       {item.price}")
        print("")


def write_to_file(products):
    textToWrite: str = ""

    for item in products:
        textToWrite += f"{item.date},{item.description},{item.price},{item.tag} \n"

    with open("/home/jamie/Projects/python/web_scraper/results.csv", "a") as file:
        file.write(textToWrite)
