from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage
from pageobjects.qc_wallet.history import HistoryPageQC

class NotificationsPageQC(BasePage):
    """Notifications page object """
    
    # Locators
    en_title_text_locator = "Activities"
    fr_title_text_locator = "Activités"
    on_this_page_text_locator = "Notifications"
    history_locator = (AppiumBy.ID, "com.ariesbifold:id/Activities.HistoryTab")

    def __init__(self, driver):
        super().__init__(driver)
        
    def on_this_page(self):
        return super().on_this_page(self.en_title_text_locator) or super().on_this_page(self.fr_title_text_locator)
    
    def select_history(self):
        if self.on_this_page():
            self.find_by(self.history_locator).click()
            return HistoryPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
