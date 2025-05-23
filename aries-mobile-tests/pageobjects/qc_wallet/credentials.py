import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from pageobjects.bc_wallet.credentials import CredentialsPage
from pageobjects.qc_wallet.add_a_credential import AddACredentialModal
from pageobjects.basepage import BasePage


class CredentialsPageQC(BasePage):
    """Credentials page QC object"""

    # Locators
    on_this_page_text_locator = (AppiumBy.ACCESSIBILITY_ID, "Credentials")
    add_your_first_credential_locator = (AppiumBy.ID, "com.ariesbifold:id/AddFirstCredential")
    android_title_locator = (AppiumBy.XPATH, "//*[@text='Credentials']")
    ios_title_locator = (AppiumBy.ACCESSIBILITY_ID, "Credentials")


    # Modal add a credential 
    add_a_credential_modal = AddACredentialModal
    def __init__(self, driver):
        super().__init__(driver)
        self.add_a_credential_modal = AddACredentialModal(driver) 
         
    def on_this_page(self):
        language = self.get_app_language()
        if language == "French":
            self.on_this_page_text_locator = "Attestations"
            self.on_this_page_locator = (AppiumBy.NAME, "Attestations")
        if self.driver.capabilities["platformName"].lower() == "iOS".lower():
            return super().on_this_page(self.ios_title_locator)
        else:
            return super().on_this_page(self.android_title_locator)
    
    def select_add_your_firs_credential(self):
        if self.on_this_page():
            self.find_by(self.add_your_first_credential_locator).click()
            return AddACredentialModal(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")