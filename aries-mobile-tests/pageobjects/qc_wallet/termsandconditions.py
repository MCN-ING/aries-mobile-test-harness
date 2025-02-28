from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from pageobjects.basepage import WaitCondition
from pageobjects.bc_wallet.pinsetup import PINSetupPage
from pageobjects.bc_wallet.termsandconditions import TermsAndConditionsPage
from pageobjects.qc_wallet.pinsetup import PINSetupPageQC
from pageobjects.basepage import BasePage


# These classes can inherit from a BasePage to do commone setup and functions
class TermsAndConditionsPageQC(BasePage):
    """Terms and Conditions QC page object"""

    on_this_page_android_locator = (AppiumBy.XPATH, "//*[@text='Terms & Conditions']")
    on_this_page_locator = (AppiumBy.NAME, "Terms & Conditions")
    back_aid_locator = (AppiumBy.ACCESSIBILITY_ID, "Back")
    terms_and_conditions_accept_locator = (AppiumBy.ID, "com.ariesbifold:id/IAgree")
    continue_button_locator = (AppiumBy.ID, "com.ariesbifold:id/Continue")
    
    
    def on_this_page(self):
        if self.current_platform.lower() == "Android".lower():
            return super().on_this_page(self.on_this_page_android_locator)
        return super().on_this_page(self.on_this_page_locator)

    def select_accept(self):
        if self.on_this_page():
            el_visible = self.is_element_visible(
                self.terms_and_conditions_accept_locator
            )
            timeout = 30
            while not el_visible and timeout > 0:
                self.swipe_down()
                el_visible = self.is_element_visible(
                    self.terms_and_conditions_accept_locator
                )
                timeout -= 1
            self.find_by(self.terms_and_conditions_accept_locator).click()
            return True
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_continue(self):
        el_visible = self.is_element_visible(self.continue_button_locator)
        timeout = 30
        while not el_visible and timeout > 0:
            self.swipe_down()
            el_visible = self.is_element_visible(self.continue_button_locator)
            timeout -= 1
        self.find_by(self.continue_button_locator).click()
        return PINSetupPageQC(self.driver)
