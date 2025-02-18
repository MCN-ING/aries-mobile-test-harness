from pageobjects.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class WhatAreContactsPageQC(BasePage):
    """what are contacts page object"""

    # Locators
    on_this_page_text_locator = "What are Contacts?"
    
    def on_this_page(self):
        return super().on_this_page(self.on_this_page_text_locator)
    
    def select_contacts_list(self):
        if self.on_this_page():
            self.find_by(self.contacts_list_locator).click()
        else:
            raise Exception(f"App not on the {type(self)} page")
        