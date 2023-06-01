from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage
from pageobjects.bc_wallet.onboardingstorecredssecurely import OnboardingStoreCredsSecurelyPage
from pageobjects.bc_wallet.termsandconditions import TermsAndConditionsPage
import os

# These classes can inherit from a BasePage to do common setup and functions
class OnboardingWelcomePage(BasePage):
    """Onboarding Welcome Screen page object"""

    # Locators
    # TODO: If Ontario/BC or other wallets are closely alligned and only locators are different, 
    # we could create a locator module that has all the locators. Given a specific app we could load the locators for that app. 
    # not sure this would be a use case that would be common. Leaving locators with the page objects for now.
    on_this_page_text_locator = "Welcome"
    #on_this_page_locator = (AppiumBy.ACCESSIBILITY_ID, "Welcome")
    on_this_page_locator = (AppiumBy.NAME, "Welcome")
    skip_locator = (AppiumBy.ID, "com.ariesbifold:id/Skip")
    # locator changes in 127
    next_locator = (AppiumBy.ID, "com.ariesbifold:id/Next")

    def on_this_page(self):  
        # Sometimes (especially when running with a local emulator ) where the app is not loaded yet.
        # Appium doesn't seem to let this happen when using Sauce Labs. 
        timeout = 10
        if "Local" in os.environ['DEVICE_CLOUD']:
            timeout = 100
        return super().on_this_page(self.on_this_page_locator, timeout)   

    def get_onboarding_text(self):
        if self.on_this_page():
            pass
        else:
            raise Exception(f"App not on the {self.on_this_page_text_locator} page")

    def select_next(self):
        if self.on_this_page():
            try:
                self.find_by(self.next_locator).click()
            except:
                print("Element not found. Waiting 10 seconds and trying again...")
                sleep(10)
                self.find_by(self.next_locator).click()
            return OnboardingStoreCredsSecurelyPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_skip(self):
        if self.on_this_page():
            try:
                self.find_by(self.skip_locator).click()
            except:
                print("Element not found. Waiting 10 seconds and trying again...")
                sleep(10)
                self.find_by(self.skip_locator).click()
            return TermsAndConditionsPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
