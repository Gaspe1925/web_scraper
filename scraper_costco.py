from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from product import Product


def get(product: Product, driver: webdriver.Chrome):
    driver.delete_all_cookies()
    driver.get(product.url)
    sleep(10)

    # title portion
    hasTitleError = False
    itemTitle: str = ""

    try:
        itemTitle = driver.find_element(
            By.CSS_SELECTOR, "div.MuiTypography-root.MuiTypography-t1.mui-kzj5f"
        ).text
    except:
        hasTitleError = True

    if hasTitleError:
        # try:
        itemTitle = driver.find_element(By.CSS_SELECTOR, "h1").text
        # except:
        #     product.hasError = True
        #     return

    product.description = itemTitle.replace("\n", "").replace(",", " ")

    # price portion
    itemPrice: str = ""
    hasPriceError = False

    try:
        priceElements: list[WebElement] = driver.find_elements(
            By.CSS_SELECTOR, "div.MuiBox-root.mui-zs1y8t span"
        )

        for item in priceElements:
            itemPrice += item.text
        itemPrice = itemPrice.replace("\n", "").split("$", 2)[1]
        length: int = len(itemPrice) - (len(itemPrice) - itemPrice.rfind("."))
        itemPrice = itemPrice[:length]

    except:
        hasPriceError = True

    if hasPriceError:
        # try:
        itemPrice = driver.find_element(
            By.CSS_SELECTOR, "span.value.canada-currency-size"
        ).text

        print(itemPrice)
        itemPrice = itemPrice.replace("\n", "").replace("$", "")
        hasPriceError = False
        # except:
        product.hasError = True

    if hasPriceError:
        return

    product.price = float(itemPrice)
