from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.bc_wallet.welcome_to_bc_wallet import WelcomeToBCWalletModal
from pageobjects.basepage import BasePage, WaitCondition

class WelcomeToQCWalletModal(WelcomeToBCWalletModal):
    """Welcome to BC Wallet Modal page object"""

    on_this_page_text_locator = "Welcome to QC Wallet"
    on_this_page_locator = (AppiumBy.NAME, "Welcome to QC Wallet")
    use_app_guides_button_locator = (AppiumBy.ID, "com.ariesbifold:id/Primary")
    add_and_share_credentials_locator = (AppiumBy.ID, "com.ariesbifold:id/HeaderText")
    next_locator = (AppiumBy.ID, "com.ariesbifold:id/Next")
    skip_locator = (AppiumBy.ID, "com.ariesbifold:id/Back")
    close_locator = (AppiumBy.ID, "com.ariesbifold:id/Close")

    def on_this_page(self):
        language = self.get_app_language()
        if language == "French":
            self.on_this_page_text_locator = "Bienvenue au Portefeuille numérique"
            self.on_this_page_locator = (AppiumBy.NAME, "Bienvenue au Portefeuille numérique")
        return super().on_this_page()
    
    def select_use_app_guides(self):
        self.find_by(
            self.use_app_guides_button_locator,
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE,
        ).click()
        
    def add_and_share_credential_modal(self):
        return self.find_by(
            self.add_and_share_credentials_locator, 
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE
            )
    def select_next(self):
        self.find_by(
            self.next_locator,
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE,
        ).click()
        
    def new_modal(self):
        return self.find_by(
            self.add_and_share_credentials_locator, 
            wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE
            )