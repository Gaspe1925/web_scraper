from selenium import webdriver

import product
import products
import scraper_costco
import scraper_memex
import scraper_walmart


def parse_domain(url):
    delimiter = "://"
    urlTrimmed = url.split(delimiter, 1)
    delimiter = "/"
    urlTrimmed = urlTrimmed[1].split(delimiter, 1)
    return urlTrimmed[0]


def get(item: product.Product, driver):
    urlParsed = parse_domain(item.url)
    match urlParsed:
        case "www.memoryexpress.com":
            scraper_memex.get(item, driver)
            return
        case "www.walmart.ca":
            scraper_walmart.get(item, driver)
            return
        case "www.costco.ca":
            scraper_costco.get(item, driver)
            return


def scrape():

    driver = webdriver.Chrome()
    # driver.minimize_window()
    driver.maximize_window()
    driver.delete_network_conditions
    driver.delete_all_cookies
    items = products.get_list()

    for item in items:
        get(item, driver)

    driver.close()

    products.print_products(items)
    # products.write_to_file(items)


scrape()
