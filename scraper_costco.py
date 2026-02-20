from time import sleep

from selenium.webdriver.common.by import By

import product


def get(product: product.Product, driver):
    driver.delete_all_cookies()
    driver.get(product.url)

    sleep(10)

    itemTitle = driver.find_element(
        By.CSS_SELECTOR, "div.MuiTypography-root.MuiTypography-t1.mui-kzj5f"
    )

    itemPrice: str = ""
    hasError = False
    try:
        tempPrice = driver.find_elements(
            By.CSS_SELECTOR, "div.MuiBox-root.mui-zs1y8t span"
        )
        for item in tempPrice:
            itemPrice += item.text
        itemPrice = itemPrice.replace("\n", "").split("$", 2)[1]
        length: int = len(itemPrice) - (len(itemPrice) - itemPrice.rfind("."))
        itemPrice = itemPrice[:length]

    except:
        hasError = True

    product.description = itemTitle.text.replace("\n", "").replace(",", " ")
    product.price = float(itemPrice)


# try:
# except:
#     print("ran into issue with: " + product.url)
