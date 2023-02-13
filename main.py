"""
This file was automatically generated of service
https://automatic-fox.ru/service/generator/web-scraper.
"""
# Enable logging
import logging

logging.basicConfig(
    format="%(asctime)s : %(lineno)d : %(name)s : %(levelname)s : %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)
import requests
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass

HEADERS = {
    "User-agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
}

goods = []


@dataclass
class GoodItem:
    url: str
    category: str
    title: str
    price: str
    description: str
    attribute: dict


def dump_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f)


def good(url, category):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    categories = soup.select("div.form-group")

    attr = dict()

    for attr_key in categories:
        key = attr_key.select("label")[0].text
        # for attr_value in
        breakpoint()



    good_item = GoodItem(
        url=url,
        category=category,
        title=soup.h1.text,
        price_basic=soup.select("span.autocalc-product-special")[0].text,
        description=soup.select_one("#tab-description p").text,
        # attribute=


    )


def next_page(url):
    response_categories = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response_categories.text, 'lxml')

    for category in soup.select("div.sidemenu ul li a"):
        category_url = category['href']
        cat = category.find("img")["alt"]

        response_goods = requests.get(category_url, headers=HEADERS)
        soup_goods = BeautifulSoup(response_goods.text, "lxml")
        for good_item in soup_goods.select("div.image a"):
            # good_url = good_item["href"]
            good_url = "https://postelka37.com/ivanovskaya_byaz/sladkaya_parochka_tt"
            good(good_url, cat)


def main():
    logger.info("Work start")
    next_page("https://postelka37.com/")
    response = requests.get("https://stackoverflow.com", headers=HEADERS)
    assert response.status_code == 200

    logger.info(response)
    logger.info("Work end")


if __name__ == '__main__':
    main()
