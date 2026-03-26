import time

import pytest

from pages.cart_page import CartPage
from pages.shop_page import ShopPage

@pytest.mark.flaky(reruns=3, reruns_delay=1)
@pytest.mark.run(order=3)
def test_cart(driver):
    shop_page = ShopPage(driver)
    shop_page.shop("John", "Doe", "12345")
    time.sleep(1)
    page = CartPage(driver)


    page.cart()

    assert "Products" in driver.page_source