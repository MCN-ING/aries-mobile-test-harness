from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.bc_wallet.toast_notification import ToastNotification

class NoInternetConnectionToastNotification(ToastNotification):
    """No Internet Connection toast notification page object"""

    # Locators
    on_this_page_text_locator = "No internet connection"
    notification_locator = (AppiumBy.ID, "com.ariesbifold:id/ToastTitle")


