from selenium import webdriver

import memex_scraper
import product
import products


def parse_domain(url):
    delimiter = "://"
    urlTrimmed = url.split(delimiter, 1)
    delimiter = "/"
    urlTrimmed = urlTrimmed[1].split(delimiter, 1)
    return urlTrimmed[0]


def scrape(item: product.Product, driver):
    urlParsed = parse_domain(item.url)
    match urlParsed:
        case "www.memoryexpress.com":
            memex_scraper.get(item, driver)
            return


def main():

    driver = webdriver.Chrome()
    driver.minimize_window()
    items = products.get_list()

    for item in items:
        scrape(item, driver)

    driver.close()

    products.print_products(items)
    products.write_to_file(items)


main()
