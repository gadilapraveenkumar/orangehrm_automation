from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader
import os

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.config = ConfigReader()
        self.URL = self.config.get('DEFAULT', 'base_url')

    LOCATORS = {
        'username_field': (By.XPATH, '//*[@name="username"]'),
        'password_field': (By.XPATH, '//*[@name="password"]'),
        'login_button': (By.XPATH, '//button[@type="submit"]'),
        'invalid_credentials': (By.ID, 'spanMessage'),
        # Example XPath locators (can be used as alternatives)
        'username_xpath': (By.XPATH, "//input[@id='txtUsername']"),
        'password_xpath': (By.XPATH, "//input[@id='txtPassword']"),
        'login_button_xpath': (By.XPATH, "//input[@id='btnLogin']"),
        'error_message_xpath': (By.XPATH, "//span[@id='spanMessage']")
    }

    def load(self):
        self.browser.get(self.URL)

    def enter_username(self, username):
        username_field = self.browser.find_element(*self.LOCATORS['username_field'])
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.browser.find_element(*self.LOCATORS['password_field'])
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.browser.find_element(*self.LOCATORS['login_button'])
        login_button.click()

    def get_error_message(self):
        error_element = self.browser.find_element(*self.LOCATORS['invalid_credentials'])
        return error_element.text