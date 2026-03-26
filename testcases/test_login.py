import pytest

from pages.login_page import LoginPage

@pytest.mark.run(order=1)
# @allure.title("管理员登录成功")
def test_login(driver):
    # page = LoginPage(driver)
    # page.login()
    # driver.quit()

    assert "Swag Labs" in driver.title