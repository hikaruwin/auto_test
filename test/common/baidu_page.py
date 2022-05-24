from time import sleep

from selenium.webdriver.common.by import By

from test.common.base import Base


class BaiduPage(Base):

    search_loc = (By.ID, 'kw')
    click_loc = (By.ID, 'su')

    def search(self, url, text):
        self.open('https://www.baidu.com')
        self.loc_element_explicitly(BaiduPage.search_loc).send_keys('selenium')
        sleep(2)
        self.click(BaiduPage.click_loc)
        sleep(2)


if __name__ == '__main__':
    BaiduPage().search()
