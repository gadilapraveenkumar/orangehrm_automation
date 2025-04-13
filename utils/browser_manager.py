from selenium import webdriver
from utils.config_reader import ConfigReader
import os
class BrowserManager:
    _driver = None

    @staticmethod
    def get_browser():
        if BrowserManager._driver is None:
            config = ConfigReader()
            browser_type = config.get('DEFAULT', 'browser_type').lower()

            if browser_type == 'chrome':
                BrowserManager._driver = webdriver.Chrome()
            elif browser_type == 'firefox':
                BrowserManager._driver = webdriver.Firefox()
            elif browser_type == 'edge':
                BrowserManager._driver = webdriver.Edge()
            else:
                raise ValueError(f"Unsupported browser type: {browser_type}")

            BrowserManager._driver.maximize_window()
            BrowserManager._driver.implicitly_wait(20)
        return BrowserManager._driver

    @staticmethod
    def close_browser():
        if BrowserManager._driver is not None:
            BrowserManager._driver.quit()
            BrowserManager._driver = None