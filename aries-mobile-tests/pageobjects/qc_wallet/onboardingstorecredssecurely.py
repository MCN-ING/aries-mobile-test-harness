from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage
from pageobjects.qc_wallet.onboardingsharenecessary import \
    OnboardingShareNecessaryPageQC
from pageobjects.qc_wallet.termsandconditions import TermsAndConditionsPageQC


class OnboardingStoreCredsSecurelyPageQC(BasePage):
    """Onboarding Store your Credentials Securely Screen page object"""

    on_this_page_text_locator = "A digital credential"
    on_this_page_locator = (AppiumBy.NAME, "A digital credential, secretly saved")
    skip_locator = (AppiumBy.ID, "com.ariesbifold:id/Skip")
    back_locator = (AppiumBy.ID, "com.ariesbifold:id/Back")
    next_locator = (AppiumBy.ID, "com.ariesbifold:id/Next")

    def on_this_page(self):
        if self.current_platform.lower() == "Android".lower():
            return super().on_this_page(self.on_this_page_text_locator)
        return super().on_this_page(self.on_this_page_locator)

    def get_onboarding_text(self):
        if self.on_this_page():
            pass
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_next(self):
        if self.on_this_page():
            self.find_by(self.next_locator).click()
            return OnboardingShareNecessaryPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_back(self):
        if self.on_this_page():
            self.find_by(self.back_locator).click()
            from pageobjects.qc_wallet.onboardingwelcome import \
                OnboardingWelcomePageQC

            return OnboardingWelcomePageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_skip(self):
        if self.on_this_page():
            self.find_by(self.skip_locator).click()
            return TermsAndConditionsPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
