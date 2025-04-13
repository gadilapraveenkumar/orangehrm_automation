from typing import Any

from selenium.webdriver.common.by import By

from utils.config_reader import ConfigReader


class Navigation:

    def __init__(self,browser):
        self.browser = browser
        self.config = ConfigReader()
        self.page_xpath = "//span[text()='<<replacePage>>']"

    LOCATORS = {
        'username_field': (By.XPATH, '//*[@name="username"]')
    }

    def navigate_each_page(self,page_name):
        status = False
        try:
            page_xpath_final = self.page_xpath.replace("<<replacePage>>", str(page_name))
            page = self.browser.find_element("xpath", page_xpath_final)
            #page = self.browser.find_element(page_xpath_final)
            page.click()
            status = True
            return status
        except Exception as e:
            print("got exception in navigate to each page method "+e)
