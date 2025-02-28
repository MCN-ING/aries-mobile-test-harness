from pageobjects.bc_wallet.pin import PINPage
from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage, WaitCondition
class PINPageQC(BasePage):
    """PIN QC Entry page object"""
    
    #Locators
    enter_pin_locator = (AppiumBy.ID, "com.ariesbifold:id/EnterPIN")
    enter_button_locator = (AppiumBy.ID, " com.ariesbifold:id/Enter")

    def __init__(self, driver):
        super().__init__(driver)
        
    def on_this_page(self):
        return super().on_this_page(self.enter_pin_locator)

    def select_enter(self):
        if self.on_this_page():
            self.find_by(self.enter_button_locator).click()
            # return the wallet initialization page
            # return InitializationPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
        
    def enter_pin(self, pin):
        if self.on_this_page():
            self.find_by(self.enter_pin_locator).send_keys(pin)
            return True
        else:
            raise Exception(f"App not on the {type(self)} page")
