from selenium.webdriver.common.by import By
from utils.config_reader import ConfigReader

class LHN_name_list:

    def __init__(self,browser):
        self.browser = browser
        self.config = ConfigReader()

    LOCATORS = {
        'lhn_menu_field': (By.XPATH, '//*[@class="oxd-main-menu-item"]/span'),
    }

    def get_all_lhn_menu_list(self,test_case_name):
        print("we are in get all lhn menu list ")
        lhn_list  = self.browser.find_elements(*self.LOCATORS['lhn_menu_field'])
        size = len(lhn_list)
        lhn_list_text = []
        print(" lhn menu count is : ")
        print(size)
        for i in lhn_list:
            lhn_list_text.append(i.text)
        return lhn_list_text




