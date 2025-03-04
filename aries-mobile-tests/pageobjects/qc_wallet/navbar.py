from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage
from pageobjects.bc_wallet.connecting import ConnectingPage
from pageobjects.bc_wallet.settings import SettingsPage
from pageobjects.bc_wallet.home import HomePage
from pageobjects.bc_wallet.credentials import CredentialsPage
from pageobjects.qc_wallet.moreoptions import MoreOptionsPageQC
from pageobjects.qc_wallet.notifications import NotificationsPageQC
from pageobjects.qc_wallet.credentials import CredentialsPageQC

class NavBarQC(BasePage):
    """Nav Bar Footer object"""

    # Locators
    moreOptions_locator = (AppiumBy.ID, "com.ariesbifold:id/TabStack.OptionsPlus")
    activities_locator = (AppiumBy.ID, "com.ariesbifold:id/TabStack.Activities")
    credentials_locator = (AppiumBy.ID, "com.ariesbifold:id/TabStack.Credentials")
    home_locator = (AppiumBy.ID, "com.ariesbifold:id/TabStack.Home")
    
    def __init__(self, driver):
        self.driver = driver
    

    def select_home(self):
        self.find_by(self.home_locator).click()
        return HomePageQC(self.driver)
        
    def select_more(self):
        self.find_by(self.moreOptions_locator).click()
        return MoreOptionsPageQC(self.driver)     
    
    def select_activities(self):
            self.find_by(self.activities_locator).click()
            return NotificationsPageQC(self.driver)

    def select_credentials(self):
            self.find_by(self.credentials_locator).click()
            return CredentialsPageQC(self.driver)
