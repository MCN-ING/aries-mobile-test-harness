from pageobjects.basepage import BasePage, WaitCondition
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import re
import unicodedata

class RequestAuthenticationAttestationQC(BasePage):
    """ Request Authentication Attestation page Object """
    
    #Locators
    en_title_text_locator = "Request your Authentication Attestation"
    fr_title_text_locator = "Demander son Attestation d’authentification"
    receive_my_attestation = (AppiumBy.ID, "com.ariesbifold:id/StartProcess")
    tab_bar_locator = (AppiumBy.NAME, "TabBarItemTitle")
    
    def __init__(self, driver):
        super().__init__(driver)

    def on_this_page(self):
        return super().on_this_page(self.en_title_text_locator) or super().on_this_page(self.fr_title_text_locator)
    
    def select_receive_my_attestation(self):
        if self.on_this_page():
            self.find_by(self.receive_my_attestation).click()
        else:
            raise Exception(f"App not on the {type(self)} page")

    def clean_url(self, url):
        """ Nettoie une URL en supprimant les caractères invisibles et les parties non pertinentes """
        url = unicodedata.normalize("NFKC", url)  
        url = url.strip()  
        url = re.sub(r'[^\x20-\x7E]', '', url)  
        url = url.split(',')[0]  
        return url

    def verify_website_opened(self, url):
        """ Vérifie que le site web attendu est bien ouvert dans Safari """
        try:
            url_element = self.find_by(self.tab_bar_locator)
            current_url = url_element.text
            logging.info(f"URL actuelle détectée dans Safari - current_url: {current_url}")

            if not current_url:
                logging.error("Aucun élément URL trouvé dans Safari.")
                return False
            raw_url = current_url.strip()
            # Appliquer le nettoyage de l'URL
            cleaned_url = self.clean_url(raw_url)
            logging.info(f"URL nettoyée détectée dans Safari : {cleaned_url}")
            if cleaned_url == url:
                logging.info("✅ Le site attendu est bien ouvert.")
                return True
            else:
                logging.warning(f"Mauvaise URL ! Attendu : {url}  Actuel : {cleaned_url}")
                return False

        except Exception as e:
            logging.error(f"Impossible de récupérer l'URL dans Safari : {str(e)}")
            return False