import os
from datetime import date, timedelta

import pandas as pd

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
        product.Product(
            "https://www.walmart.ca/en/ip/Huggies-Little-Movers-HuggFit-360-Baby-Diapers-with-360-Waistband-Size-3-7-Count-136-70/6000208734927",
            100,
            Tag.DIAPER_SIZE_5,
        ),
        product.Product(
            "https://www.costco.ca/p/-/huggies-little-movers-plus-diapers-sizes-3-7/4000359823?storeId=10302&contractId=120950&contractId=120551&contractId=120552&contractId=120769&contractId=120771&contractId=120768&contractId=120773&contractId=120772&contractId=120770&contractId=120774&contractId=120554&contractId=4000000000000101007&contractId=120952&contractId=120553&contractId=81322&contractId=4000000000000001004&partNumber=4000359823&langId=-24&catalogId=11201",
            156,
            Tag.DIAPER_SIZE_5,
        ),
    ]


def print_products(products):
    result: str = ""
    for item in products:
        result += globals.dash_line() + "\n"

        if item.hasError == True:
            result += f"Issue with: {item.url}\n\n"
            continue

        result += item.url + "\n"
        result += f"description: {item.description}\n"
        result += f"price:       {item.price}\n"
        result += f"price per:   {item.price_per()}\n\n"
    print(result)
    return


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
