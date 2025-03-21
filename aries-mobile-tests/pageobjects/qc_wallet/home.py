from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage, WaitCondition
from pageobjects.bc_wallet.credential_details import CredentialDetailsPage
from pageobjects.bc_wallet.home import HomePage
from pageobjects.qc_wallet.welcome_to_qc_wallet import WelcomeToQCWalletModal
from pageobjects.qc_wallet.notifications import NotificationsPageQC
from pageobjects.qc_wallet.camera_privacy_policy import CameraPrivacyPolicyPageQC

class HomePageQC(HomePage):
    """Home page object"""

    # Locators
    on_this_page_text_locator = "Home"
    on_this_page_locator = (AppiumBy.NAME, "Home")
    see_all_notifications_link_locator = (AppiumBy.NAME, "See all notifications")
    scan_qr_code_locator = (AppiumBy.ID, "com.ariesbifold:id/ScanQrCode")
    new_credential_offer_locator = (AppiumBy.ID, "com.ariesbifold:id/ViewOffer")

    # Modals and Alerts for Home page
    welcome_to_qc_wallet_modal = WelcomeToQCWalletModal

    def __init__(self, driver):
        super().__init__(driver)
        self.welcome_to_qc_wallet_modal = WelcomeToQCWalletModal(driver)

    def on_this_page(self):
        language = self.get_app_language()
        if language == "French":
            self.on_this_page_text_locator = "Accueil"
            self.on_this_page_locator = (AppiumBy.NAME, "Accueil")
        return super().on_this_page()

    def select_dismiss(self):
        self.find_by(
            self.dismiss_button_locator,
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE,
        ).click()        
        
    def select_see_all_notifications_link(self):
        if self.on_this_page():
            self.find_by(self.see_all_notifications_link_locator).click()
            return NotificationsPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
        
    def select_scan_qr_code(self):
        if self.on_this_page():
            self.find_by(self.scan_qr_code_locator).click()
            return CameraPrivacyPolicyPageQC (self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
        
        
    def select_open_credential_offer(self):
        if self.on_this_page():
            self.find_by(self.new_credential_offer_locator, wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE).click()
            # return CredentialOfferPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)}")
        