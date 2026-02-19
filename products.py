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
            "https://www.memoryexpress.com/Products/MX00120891", 1, Tag.IRON_WOLF
        ),
        product.Product(
            "https://www.memoryexpress.com/Products/MX00132129", 1, Tag.B_580_OC
        ),
        product.Product(
            "https://www.memoryexpress.com/Products/MX00132128", 1, Tag.B_580_OC
        ),
        product.Product(
            "https://www.memoryexpress.com/Products/MX00132130", 1, Tag.B_580
        ),
    ]


def print_products(products):
    for item in products:
        print(globals.dash_line())
        print(f"description: {item.description}")
        print(f"price:       {item.price}")
        print("")


def write_to_file(products):

    textToWrite: str = ""

    if not os.path.exists(globals.RESULTS_CSV):
        with open(globals.RESULTS_CSV, "w") as file:
            file.write("Date,URL,Description,Price,Quantity,Price Per,Tag,HasError\n")

    for item in products:
        textToWrite += f"{item.date},{item.url},{item.description},{item.price},{item.quantity},{item.price_per()},{item.tag},{item.hasError} \n"
    with open(globals.RESULTS_CSV, "a") as file:
        file.write(textToWrite)


def print_lowest_price():
    # get lowest price
    print(
        f"""{globals.dash_line()}
        Today's Lowest Prices
{globals.dash_line()}
        """
    )

    data = pd.read_csv(globals.RESULTS_CSV)
    dateToday = date.today()
    dataToday = data.query(f"Date=='{dateToday}'")
    indexMin = dataToday.groupby("Tag")["Price Per"].idxmin()
    dataLowestPrice = dataToday.loc[indexMin][["Date", "Tag", "Price Per", "URL"]]
    print(dataLowestPrice)

    # aggregate past 30 days
    lessDays = timedelta(days=30)
    dataPastDays = data.query(
        f"Date < '{dateToday}' and Date >= '{dateToday - lessDays}'"
    )

    # for index, row in df.iterrows():
    #     print(row["c1"], row["c2"])

    # join data here later
    print(dataPastDays)
