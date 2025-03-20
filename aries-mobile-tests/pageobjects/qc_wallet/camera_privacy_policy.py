
from pageobjects.bc_wallet.camera_privacy_policy import CameraPrivacyPolicyPage
from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.qc_wallet.identiQc_access_camera_permission import identiQcAccessCameraPermissionModal
import logging
from pageobjects.basepage import BasePage
from pageobjects.basepage import WaitCondition


class CameraPrivacyPolicyPageQC(BasePage):
    """Camera Privacy Policy page QC object"""
    
    #Locators
    en_title_text_locator = "Allow camera use"
    on_this_page_locator = (AppiumBy.ID, "com.ariesbifold:id/AllowCameraUse")
    fr_title_text_locator = "Autoriser l'utilisation de l'appareil photo"
    modal_allow_camera_locator = '“Portefeuille QC” Would Like to Access the Camera'
    continue_button_locator = (AppiumBy.ID, "com.ariesbifold:id/Continue")


    # Modal add a credential 
    identiQc_access_camera_permission_modal = identiQcAccessCameraPermissionModal
    
    def __init__(self, driver):
        super().__init__(driver)
        self.identiQc_access_camera_permission_modal = identiQcAccessCameraPermissionModal(driver)
        
    def on_this_page(self):
        return super().on_this_page(self.on_this_page_locator) 
    
    # def is_camera_permission_modal_displayed(self):
    #     """Vérifie si le modale 'Portefeuille QC Would Like to Access the Camera' est affiché"""
    #     try:
    #         return self.portefeuil_qc_would_like_access_camera_modal.on_this_page()
    #     except NoSuchElementException:
    #         logging.info("Le modale d'autorisation de la caméra n'est pas affiché")
    #         return False
    
    def select_continue(self):
        self.find_by(self.continue_button_locator, wait_condition=WaitCondition.PRESENCE_OF_ELEMENT_LOCATED).click()
        # 28 sec
        #self.find_by(self.allow_button_locator, wait_condition=WaitCondition.VISIBILITY_OF_ELEMENT_LOCATED).click()
        # 22 sec
        #self.find_by((AppiumBy.ACCESSIBILITY_ID, "Allow"), wait_condition=WaitCondition.PRESENCE_OF_ELEMENT_LOCATED).click()
        
        # if self.driver.capabilities['platformName'] == 'Android':
        #     self.select_system_allow_while_using_app()
        return True
    
    def select_system_allow_while_using_app(self):
        self.find_by(self.system_allow_while_using_app, wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE).click()
