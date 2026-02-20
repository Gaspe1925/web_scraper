from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import product


def get(product: product.Product, driver):
    # driver.delete_all_cookies()

    try:
        driver.get(product.url)
        # wait = WebDriverWait(driver, 20)
        # wait.until(
        #     EC.visibility_of_all_elements_located(
        #         (
        #             By.CSS_SELECTOR,
        #             ".product-title-link.line-clamp.line-clamp-2.truncate-title>span",
        #         )
        #     )
        # )

        itemTitle = driver.find_element(By.ID, "main-title")
        # itemPrice = driver.find_element(
        #     By.CSS_SELECTOR, "div.c-capr-pricing__grand-total div"
        # )

        product.description = itemTitle.text.replace("\n", "").replace(",", " ")
        # product.price = itemPrice.text.replace("Only$", "")
    except:
        product.hasError = True
