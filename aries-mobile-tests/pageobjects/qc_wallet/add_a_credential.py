from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.bc_wallet.welcome_to_bc_wallet import WelcomeToBCWalletModal
from pageobjects.basepage import BasePage, WaitCondition
from pageobjects.qc_wallet.camera_privacy_policy import CameraPrivacyPolicyPageQC


class AddACredentialModal(WelcomeToBCWalletModal):
    """Add a credential Modal page object"""

    # Locators
    add_certificate_button_locator = (AppiumBy.NAME, "com.ariesbifold:id/AddMyDigitalGovernmentAuthenticationCertificate")
    sqan_qr_code_locator = (AppiumBy.NAME, "com.ariesbifold:id/ScanAQRCode")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.on_this_page_text_locator = "Add a Credential"
        self.on_this_page_locator = (AppiumBy.NAME, "Add a Credential")
    
    def on_this_page(self):
        language = self.get_app_language()
        if language == "French":
            self.on_this_page_text_locator = "Add a credential"
            self.on_this_page_locator = (AppiumBy.NAME, "Add a credential")
        return super().on_this_page()
    
    def is_displayed(self):
        return self.on_this_page()
    
    def select_add_digital_certificate(self):
        self.find_by(
            self.add_certificate_button_locator,
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE,
        ).click()
        
    def select_scan_qr_code(self):
        self.find_by(
            self.sqan_qr_code_locator,
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE,
        ).click()
        return CameraPrivacyPolicyPageQC(self.driver)