from selenium.webdriver.common.by import By

import product


def get(product: product.Product, driver):
    driver.delete_all_cookies()
    driver.get(product.url)

    itemTitle = driver.find_element(By.CSS_SELECTOR, "header.c-capr-header h1")
    product.description = itemTitle.text.replace("\n", "").replace(",", " ")

    itemPrice = driver.find_element(
        By.CSS_SELECTOR, "div.c-capr-pricing__grand-total div"
    )
    product.price = float(itemPrice.text.replace("Only$", ""))
