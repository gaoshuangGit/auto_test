
import time

import pytest

from config.config import BASE_URL
from pages.shop_page import ShopPage

from utils.json_reader import read_json

data_list = read_json("data/test_data.json")

@pytest.mark.run(order=2)
@pytest.mark.parametrize("data", data_list)
def test_shop(driver,data):
    driver.get(BASE_URL + "/inventory.html")  # 或产品页的URL
    time.sleep(1)
    page = ShopPage(driver)
    page.shop(
         firstname=data["firstname"],
         lastname=data["lastname"],
         code=data["code"]
     )
    time.sleep(1)
