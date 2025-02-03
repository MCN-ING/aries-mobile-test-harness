from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage

class HistoryPageQC(BasePage):
    """History page object """
    
        # Locators
    en_title_text_locator = "Activities"
    fr_title_text_locator = "Activités"
    en_subtitle_locator = "History"
    fr_subtitle_locator = "Historique"


    def __init__(self, driver):
        super().__init__(driver)
        
    def on_this_page(self):
        return super().on_this_page(self.en_title_text_locator) or super().on_this_page(self.fr_title_text_locator)
