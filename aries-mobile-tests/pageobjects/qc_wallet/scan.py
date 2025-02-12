from appium.webdriver.common.appiumby import AppiumBy
from  pageobjects.bc_wallet.scan import ScanPage

class ScanQRCodePageQC(ScanPage):
    """ Scan QR code Page object  """
    
    #Locators
    back_locator = (AppiumBy.ID, "com.ariesbifold:id/Back")
    scan_locator = (AppiumBy.ID, "com.ariesbifold:id/ScanNow")
    flash_locator = (AppiumBy.ID, "com.ariesbifold:id/ScanTorch")

    def __init__(self, driver):
        super().__init__(driver)
    
    def on_this_page(self):
        return super().on_this_page()