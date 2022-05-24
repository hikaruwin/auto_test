
import time
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from utils.config import REPORT_PATH


TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'edge': webdriver.Edge}


class UnSupportBrowserTypeError(Exception):
    pass


class Base:

    def __init__(self, browser_type='chrome'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
            self.driver = self.browser()
        else:
            raise UnSupportBrowserTypeError(f'仅支持{",".join(TYPES.keys())}!')

    # def __init__(self, driver):
    #     self.driver = driver

    def open(self, url, maximize_window=True, implicitly_wait=30):
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        if implicitly_wait != 0:
            self.driver.implicitly_wait(implicitly_wait)
            return self
        return self

    def loc_element(self, loc):
        return self.driver.find_element(*loc)

    def loc_elements(self, loc):
        return self.driver.find_elements(*loc)

    def loc_element_explicitly(self, loc):
        try:
            element = WebDriverWait(self.driver, 10).until(lambda x: self.loc_element(loc))
            return element
        except Exception as e:
            raise e

    def loc_elements_explicitly(self, loc):
        try:
            elements = WebDriverWait(self.driver, 10).until(lambda x: self.loc_elements(loc))
            return elements
        except Exception as e:
            raise e

    def input(self, loc, value):
        element = self.loc_element(loc)
        element.clear()
        element.send_keys(value)

    def click(self, loc):
        self.loc_element(loc).click()

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + f'/screenshot_{day}'
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + f'/{name}_{tm}.png')
        return screenshot

    def switch_frame(self, value):
        self.driver.switch_to.frame(value)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    b = Base().open('https://www.baidu.com')
    # b.save_screen_shot('test_baidu')
    b.loc_element((By.ID, 'kw')).send_keys('111111')
    # b.input('2222', By.ID, 'kw')
    time.sleep(3)
    b.quit()