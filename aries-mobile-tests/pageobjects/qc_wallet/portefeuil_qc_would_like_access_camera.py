from pageobjects.basepage import BasePage, WaitCondition
from appium.webdriver.common.appiumby import AppiumBy
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class PortefeuilleQCWouldLikeToAccessCameraModal(BasePage):
        """ PortefeuilleQC Would Like To Access Camera Modal """


        def __init__(self, driver):
            super().__init__(driver)
            self.on_this_page_text_locator = '“Portefeuille QC” Would Like to Access the Camera'
            # self.on_this_page_locator = (AppiumBy.NAME, '“Portefeuille QC” Would Like to Access the Camera')
            self.on_this_page_locator = (AppiumBy.XPATH, "//*[contains(@name, 'Portefeuille QC')]")

        def on_this_page(self):
            
            return super().on_this_page(self.on_this_page_locator)  
               
        def is_displayed(self):
            return self.on_this_page()

        def select_allow(self):
            if self.on_this_page():
                logging.info("Checking for iOS system alert...")
                try:
                    alert = self.driver.switch_to.alert
                    alert_text = alert.text
                    logging.info(f"iOS system alert detected: {alert_text}")

                    alert.accept()  # Accepts the alert (same as clicking "Allow")
                    logging.info("Accepted iOS system alert.")
                    return
                except:
                    logging.info("No iOS system alert detected, proceeding with normal flow.")
            else:
                raise Exception(f"App not on the {type(self)} page")