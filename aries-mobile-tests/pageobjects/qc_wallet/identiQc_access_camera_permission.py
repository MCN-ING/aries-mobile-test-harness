from pageobjects.basepage import BasePage, WaitCondition
from appium.webdriver.common.appiumby import AppiumBy
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class identiQcAccessCameraPermissionModal(BasePage):
        """ identiQc Access Camera Permission Modal object"""


        def __init__(self, driver):
            super().__init__(driver)
            self.on_this_page_text_locator = '“IdentiQc” Would Like to Access the Camera'
            self.on_this_page_locator = (AppiumBy.XPATH, "//*[contains(@name, 'IdentiQc')]")
            #Android Locators
            self.on_this_page_android_locator = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_message")
            self.on_this_page_android_text_locator = "Allow IdentiQc to take photos and record video?"
            self.deny_android_locator = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")
            self.system_allow_while_using_app =  (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            self.system_only_this_time = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button")


        def on_this_page(self):
            if self.current_platform.lower() == "Android".lower():
                return super().on_this_page(self.on_this_page_android_locator)
            return super().on_this_page(self.on_this_page_locator)  
               
        def is_displayed(self):
            return self.on_this_page()

        def select_allow(self):
            if self.on_this_page():
                if self.current_platform.lower() == "iOS".lower():
                    logging.info("Checking for iOS system alert...")
                    try:
                        alert = self.driver.switch_to.alert
                        alert_text = alert.text
                        logging.info(f"iOS system alert detected: {alert_text}")

                        alert.accept()  # Accepts the alert (same as clicking "Allow")
                        return
                    except:
                        logging.info("No iOS system alert detected, proceeding with normal flow.")
                elif self.current_platform.lower() == "Android".lower():
                    logging.info("select_system_allow_while_using_app.. ")
                    self.find_by(self.system_allow_while_using_app, wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE).click()
            else:
                raise Exception(f"App not on the {type(self)} page")
                    
        def select_only_this_time(self):
            if self.on_this_page():
                logging.info("select_system_allow only this time... ")
                self.find_by(self.system_only_this_time, wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE).click()
            else:
                raise Exception(f"App not on the {type(self)} page")
                    
        def select_deny(self):
            if self.on_this_page():
                logging.info("select_system_allow only this time... ")
                self.find_by(self.deny_android_locator, wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE).click()
            else:
                raise Exception(f"App not on the {type(self)} page")
                    