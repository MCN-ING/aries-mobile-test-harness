from pageobjects.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class ReceiveACertificateOfferInfoPageQC(BasePage):
    """How i add the certificate to my PNG Info page object"""

    # Locators
    return_to_help_center_button_locator = (AppiumBy.ID, "com.ariesbifold:id/StartProcess")
    en_title_text_locator = "Receive a Certificate Offer"
    fr_title_text_locator = "Recevoir une Offre d'attestation"

    
    def on_this_page(self):
        return super().on_this_page(self.en_title_text_locator) or super().on_this_page(self.fr_title_text_locator)
    
    def select_return(self):
        from pageobjects.qc_wallet.help import HelpPageQC 
        if self.on_this_page():
            self.find_by(self.return_to_help_center_button_locator).click()
            return HelpPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")