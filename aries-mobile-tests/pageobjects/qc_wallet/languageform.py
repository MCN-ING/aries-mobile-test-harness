import logging
from pageobjects.basepage import BasePage
from pageobjects.bc_wallet.languageform import LanguageFormPage
from appium.webdriver.common.appiumby import AppiumBy

# These classes can inherit from a BasePage to do common setup and functions
class LanguageFormPageQC(BasePage):
    """Language Form page object """

    #Locators
    english_button_locator = (AppiumBy.ID, "com.ariesbifold:id/en") 
    french_button_locator = (AppiumBy.ID, "com.ariesbifold:id/fr") 
    android_title_en_locator = (AppiumBy.XPATH, "//*[contains(@text, 'Display Language')]")
    ios_title_en_locator = (AppiumBy.NAME, "Display Language") 
    ios_title_fr_locator = (AppiumBy.NAME, "Langue d'affichage") 
    android_title_fr_locator = (AppiumBy.XPATH, "//*[contains(@text, \"Langue d’affichage\")]")



    def get_title(self, language):
        return super().get_title(self, language)
    
    def on_this_page(self):
        if self.current_platform.lower() == "iOS".lower():
            return super().on_this_page(self.ios_title_en_locator) or super().on_this_page(self.ios_title_fr_locator)
        else: 
            return super().on_this_page(self.android_title_en_locator) or super().on_this_page(self.android_title_fr_locator)


    def select_language(self, language):
        if self.on_this_page():
            if language == 'English':
                self.find_by(self.english_button_locator).click()
            elif language == 'French':
                self.find_by(self.french_button_locator).click()
        else:
            raise Exception(f"App not on the {type(self)} page")
                
    def is_displayed(self, locator):
        try:
            element = self.find_by(locator)
            logging.info(f"Locator visible: {locator}")
            return element.is_displayed()
        except Exception:
            return False
        
    def get_current_language(self):
        if self.is_displayed(self.ios_title_fr_locator) or self.is_displayed(self.android_title_fr_locator):
            return "French"
        elif self.is_displayed(self.ios_title_en_locator) or self.is_displayed(self.android_title_en_locator):
            return "English"
        else:
            raise Exception(f"Unable to determine the current language on the {type(self)} page")