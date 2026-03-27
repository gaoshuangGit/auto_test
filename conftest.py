# import os.path
# import time
#
# import pytest
# from selenium import webdriver
#
#
#
# from config.config import BASE_URL
# from pages.login_page import LoginPage
#
# @pytest.fixture(scope = "function")
# def driver():
#     # driver1 = Options()
#     print("\n===== 启动浏览器 =====")
#     driver = webdriver.Chrome()
#     driver.get(BASE_URL)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#
#     login = LoginPage(driver)
#     login.login()
#
#     yield driver
#     print("===== 关闭浏览器 =====")
#     driver.quit()


# @pytest.fixture(autouse=True)
# def setup_test(driver):
#     """每个用例前打开页面并登录"""
#     driver.get(BASE_URL)  # ✅ 先打开页面
#
#     login = LoginPage(driver)
#     login.login()
#
#     yield

    # 可选：用例后的清理
    # pass
# @pytest.fixture(autouse=True)
# def reset_test_status(driver):
#     driver.get(BASE_URL)
#     yield
#     driver.refresh()


# # --------------- 失败自动截图（正确版，不报错）---------------
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         if "driver" in item.funcargs:
#             driver = item.funcargs["driver"]
#             try:
#                 # 重点：这里直接保存到 screenshots 文件夹
#                 img_path = os.path.join("screenshots", f"fail_{item.name}.png")
#                 driver.save_screenshot(img_path)
#                 print(f"\n✅ 成功截图 -> {img_path}")
#             except Exception as e:
#                 print(f"\n❌ 截图失败：{e}")


# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.config import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    """浏览器 fixture"""

    # 配置 Chrome 选项
    chrome_options = Options()

    # GitHub 环境需要开启无头模式
    if os.getenv("CI"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

    # 自动下载 ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(BASE_URL)
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 登录
    login = LoginPage(driver)
    login.login()

    yield driver

    driver.quit()