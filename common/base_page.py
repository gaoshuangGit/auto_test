from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logs import logger


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def click(self,loc):
        # #添加日志
        # logger.info(f"点击元素: {loc}")
        # try:
        self.wait.until(EC.element_to_be_clickable(loc)).click()
        #     logger.info(f"点击成功: {loc}")
        # except Exception as  e:
        #     logger.error(f"点击失败: {loc}, 错误: {e}")
        #     raise
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable(loc)
        # )
        # element.click()

    def input(self,loc,text):
       el = self.wait.until(EC.visibility_of_element_located(loc))
       el.clear()
       el.send_keys(text)
