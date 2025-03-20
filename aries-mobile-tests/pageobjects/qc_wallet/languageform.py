import logging
from pageobjects.basepage import BasePage
from pageobjects.bc_wallet.languageform import LanguageFormPage
from appium.webdriver.common.appiumby import AppiumBy

# These classes can inherit from a BasePage to do common setup and functions
class LanguageFormPageQC(BasePage):
    """Language Form page object """

    #Locators
    english_title_locator = (AppiumBy.NAME, "Display Language") 
    frensh_title_locator = (AppiumBy.NAME, "Langue d'affichage") 
    english_button_locator = (AppiumBy.ID, "com.ariesbifold:id/en") 
    french_button_locator = (AppiumBy.ID, "com.ariesbifold:id/fr") 

    def get_title(self, language):
        return super().get_title(self, language)

    def on_this_page(self):
        return super().on_this_page(self.english_title_locator) or super().on_this_page(self.french_title_locator)
          
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
            return element.is_displayed()
        except Exception:
            return False
        
    def get_current_language(self):
        logging.info("Checking for the current language...")
        if self.is_displayed(self.frensh_title_locator):
            logging.info("Current language detected: French")
            return "French"
        elif self.is_displayed(self.english_title_locator):
            logging.info("Current language detected: English")
            return "English"
        else:
            raise Exception(f"Unable to determine the current language on the {type(self)} page")