import os
from datetime import date, timedelta

import pandas as pd
from pandas.core.dtypes.dtypes import datetime

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

    if not os.path.exists(globals.RESULTS_CSV):
        with open(globals.RESULTS_CSV, "w") as file:
            file.write("Date,URL,Description,Price,Tag,HasError\n")

    for item in products:
        textToWrite += f"{item.date},{item.url},{item.description},{item.price},{item.tag},{item.hasError} \n"

    with open(globals.RESULTS_CSV, "a") as file:
        file.write(textToWrite)


def print_lowest_price():
    # get lowest price
    data = pd.read_csv(globals.RESULTS_CSV)
    dateToday = date.today()
    dataToday = data.query(f"Date=='{dateToday}'")
    indexMin = dataToday.groupby("Tag")["Price"].idxmin()
    dataLowestPrice = dataToday.loc[indexMin][["Date", "Tag", "Price", "URL"]]
    print(dataLowestPrice)

    # aggregate data
    lessDays = timedelta(days=30)
    dataPastDays = data.query(
        f"Date < '{dateToday}' and Date >= '{dateToday - lessDays}'"
    )

    print(dataPastDays)
