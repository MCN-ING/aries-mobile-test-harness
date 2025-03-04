from appium.webdriver.common.appiumby import AppiumBy
from  pageobjects.bc_wallet.scan import ScanPage

class ScanQRCodePageQC(ScanPage):
    """ Scan QR code Page object  """
    
    #Locators
    scan_locator = (AppiumBy.ID, "com.ariesbifold:id/ScanNow")
    flash_locator = (AppiumBy.ID, "com.ariesbifold:id/ScanTorch")
    back_locator = (AppiumBy.ID, "com.ariesbifold:id/Back")


    def __init__(self, driver):
        super().__init__(driver)
    
    def on_this_page(self):
        return super().on_this_page()
    
    def select_back(self):
        if self.on_this_page():
            self.find_by(self.back_locator).click()
        else:
            raise Exception(f"App not on the {type(self)} page")

        