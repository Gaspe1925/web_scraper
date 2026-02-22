from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import product


def get(product: product.Product, driver: webdriver.Chrome):
    # driver.delete_all_cookies()

    try:
        driver.get(product.url)
        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.visibility_of_all_elements_located(
                (
                    By.CSS_SELECTOR,
                    ".product-title-link.line-clamp.line-clamp-2.truncate-title>span",
                )
            )
        )

        itemTitle = driver.find_element(By.ID, "main-title")
        itemPrice = driver.find_element(
            By.CSS_SELECTOR, "div.c-capr-pricing__grand-total div"
        ).text

        product.description = itemTitle.text.replace("\n", "").replace(",", " ")
        product.price = float(itemPrice.replace("Only$", ""))
    except:
        product.hasError = True
