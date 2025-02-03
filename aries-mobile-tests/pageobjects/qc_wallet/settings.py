from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.bc_wallet.settings import SettingsPage
from pageobjects.qc_wallet.change_pin import ChangePINPageQC
from pageobjects.qc_wallet.languageform import LanguageFormPageQC

class SettingsPageQC(SettingsPage):
    """Settings page object"""

    # Locators
    display_language_button = (AppiumBy.ID, "com.ariesbifold:id/Language")
    change_pin_locator = (AppiumBy.ID, "com.ariesbifold:id/MyPin")
    back_locator = (AppiumBy.NAME, "com.ariesbifold:id/Back")
                        
    def on_this_page(self):
        language = self.get_app_language()
        if language == "French":
            self.on_this_page_text_locator = "Paramètres de l'application"
            self.on_this_page_locator = (AppiumBy.NAME, "Paramètres de l'application")
        return super().on_this_page()

    def select_my_pin(self):
        self.find_by(self.change_pin_locator).click()

        return ChangePINPageQC(self.driver)

    def select_back(self):
        # Don't check if on this page becasue android (unless you scroll back to the top) can't see the App Settings accessibility ID
        # if self.on_this_page():
        self.find_by(self.back_locator).click()
        from pageobjects.qc_wallet.home import HomePageQC

        return HomePageQC(self.driver)
        # else:
        #     raise Exception(f"App not on the {type(self)} page")

    def select_language(self):
        if self.on_this_page():
            self.find_by(self.display_language_button).click()
            return LanguageFormPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
