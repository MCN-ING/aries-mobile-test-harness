from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage
import logging
class HistoryPageQC(BasePage):
    """History page object """
    
        # Locators
    en_title_text_locator = "Activities"
    fr_title_text_locator = "Activités"
    en_subtitle_locator = "History"
    fr_subtitle_locator = "Historique"
    history_tab_locator = (AppiumBy.ID, "com.ariesbifold:id/Activities.HistoryTab")
    pin_changed_locator = (AppiumBy.ID, "com.ariesbifold:id/ViewPinChanged") 
    card_accepted_locator = (AppiumBy.ID, "com.ariesbifold:id/ViewCardAccepted") 
    connexion_established_locator = (AppiumBy.ID, "com.ariesbifold:id/ViewConnection") 
    card_declined_locator = (AppiumBy.ID, "com.ariesbifold:id/ViewCardDeclined") 



    def __init__(self, driver):
        super().__init__(driver)
        
    def on_this_page(self):
        return super().on_this_page(self.history_tab_locator)
    
    def wallet_pin_updated(self, timeout=10):
        """Check if the PIN change notification appears in the history"""
        if self.on_this_page():
            logging.info(f"checking if locator exist: {self.pin_changed_locator}")
            return self.find_by(self.pin_changed_locator).is_displayed()
        else:
            raise Exception(f"App not on the {type(self)} page")
                
    def card_accepted(self):
        if self.on_this_page():
            logging.info(f"checking if locator exist: {self.card_accepted_locator}")
            return self.find_by(self.card_accepted_locator).is_displayed()
        else:
            raise Exception(f"App not on the {type(self)} page")
        
    def connexion_established(self):
        if self.on_this_page():
            logging.info(f"checking if locator exist: {self.connexion_established_locator}")
            return self.find_by(self.connexion_established_locator).is_displayed()
        else:
            raise Exception(f"App not on the {type(self)} page")
        
    def card_declined(self):
        if self.on_this_page():
            logging.info(f"checking if locator exist: {self.card_declined_locator}")
            return self.find_by(self.card_declined_locator).is_displayed()
        else:
            raise Exception(f"App not on the {type(self)} page")