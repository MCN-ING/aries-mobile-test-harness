from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.bc_wallet.welcome_to_bc_wallet import WelcomeToBCWalletModal
from pageobjects.basepage import BasePage, WaitCondition
from pageobjects.qc_wallet.camera_privacy_policy import CameraPrivacyPolicyPageQC


class RemoveCredentialModal(BasePage):
    """Remove credential Modal page object"""

    # Locators
    confirm_remove_locator = (AppiumBy.NAME, "com.ariesbifold:id/ConfirmRemoveButton")
 
    def __init__(self, driver):
        super().__init__(driver)
        self.on_this_page_text_locator = "Remove credential from your wallet"
        self.on_this_page_locator = (AppiumBy.NAME, "Remove credential from your wallet")
    
    def on_this_page(self):
        return super().on_this_page(self.on_this_page_locator)
    
    def is_displayed(self):
        return self.on_this_page()
    
    def select_confirm_remove_from_wallet(self):
        self.find_by(self.confirm_remove_locator).click()
