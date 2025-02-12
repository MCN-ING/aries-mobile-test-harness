
from pageobjects.bc_wallet.camera_privacy_policy import CameraPrivacyPolicyPage
from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.qc_wallet.portefeuil_qc_would_like_access_camera import PortefeuilleQCWouldLikeToAccessCameraModal
import logging

class CameraPrivacyPolicyPageQC(CameraPrivacyPolicyPage):
    """Camera Privacy Policy page QC object"""
    
    #Locators
    en_title_text_locator = "Allow camera use"
    on_this_page_locator = (AppiumBy.ID, "com.ariesbifold:id/AllowCameraUse")
    fr_title_text_locator = "Autoriser l'utilisation de l'appareil photo"
    modal_allow_camera_locator = '“Portefeuille QC” Would Like to Access the Camera'

    # Modal add a credential 
    portefeuil_qc_would_like_access_camera_modal = PortefeuilleQCWouldLikeToAccessCameraModal
    
    def __init__(self, driver):
        super().__init__(driver)
        self.portefeuil_qc_would_like_access_camera_modal = PortefeuilleQCWouldLikeToAccessCameraModal(driver)
        
    def on_this_page(self):
        return super().on_this_page()
    
    def is_camera_permission_modal_displayed(self):
        """Vérifie si le modale 'Portefeuille QC Would Like to Access the Camera' est affiché"""
        try:
            return self.portefeuil_qc_would_like_access_camera_modal.on_this_page()
        except NoSuchElementException:
            logging.info("Le modale d'autorisation de la caméra n'est pas affiché")
            return False