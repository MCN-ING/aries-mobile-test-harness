from behave import given, then, when
from pageobjects.qc_wallet.request_authentication_attestation import RequestAuthenticationAttestationQC
from pageobjects.qc_wallet.camera_privacy_policy import CameraPrivacyPolicyPageQC
from pageobjects.qc_wallet.scan import ScanQRCodePageQC

import logging

@when("the user open credentials page")
def cred_page_step_impl(context):
    context.thisCredentialsPageQC = context.thisHomePageQC.select_credentials()
    
@when("the user click on Add your First Credential button")
def cred_add_step_impl(context):
    context.thisCredentialsPageQC.add_a_credential_modal = context.thisCredentialsPageQC.select_add_your_firs_credential()   
    
@then("a modal Add a Credential appear")
def cred_add_modal_impl(context):
    assert context.thisCredentialsPageQC.add_a_credential_modal.is_displayed()
    
@when("the user click on Add my digital Government Authentication Certificate link")
def link_digital_certificate_impl(context):
    context.thisRequestAuthenticationAttestationQC = context.thisCredentialsPageQC.add_a_credential_modal.select_add_digital_certificate()
         
@then("the page Request your authentication certificate is displayed")
def request_certificate_impl(context):
    context.thisRequestAuthenticationAttestationQC = RequestAuthenticationAttestationQC(context.driver)
    print(f"Valeur de context.thisRequestAuthenticationAttestationQC: {context.thisRequestAuthenticationAttestationQC}")
    assert context.thisRequestAuthenticationAttestationQC.on_this_page()
        
@when("the user click on the button Receive my attestation")
def receive_my_attestation_impl(context):
    context.thisRequestAuthenticationAttestationQC.select_receive_my_attestation()
    
@then("the website government authentication service opened")
def government_site_impl(context):
    assert context.thisRequestAuthenticationAttestationQC.verify_website_opened("auth-dev-integration.dev.authentification.si.gouv.qc.ca")
    
@when("user click on Scan a QR code button showed in the pop up")
def scan_qr_code_impl(context):
    context.thisCameraPrivacyPolicyPageQC = context.thisCredentialsPageQC.add_a_credential_modal.select_scan_qr_code()
    
@then("allow camera to use page is displayed")
def allow_camera_step_impl(context):
    assert context.thisCameraPrivacyPolicyPageQC.on_this_page()
    
@when("the user click continue button")
def continue_step_impl(context):
    context.thisCameraPrivacyPolicyPageQC.select_continue()
    
@then("modal “Portefeuille QC” Would Like to Access the Camera appears")
def modal_step_impl(context):
    logging.info(f"Is Modal displayed: {context.thisCameraPrivacyPolicyPageQC.portefeuil_qc_would_like_access_camera_modal.is_displayed()}")
    assert context.thisCameraPrivacyPolicyPageQC.portefeuil_qc_would_like_access_camera_modal.is_displayed()
   
@when("the user click Allow for the camera access")
def click_allow_step_impl(context):
    if context.thisCameraPrivacyPolicyPageQC.portefeuil_qc_would_like_access_camera_modal.is_displayed():
        context.thisCameraPrivacyPolicyPageQC.portefeuil_qc_would_like_access_camera_modal.select_allow()
    else:
         print("portefeuil_qc_would_like_access_camera_modal is Not displayed")
    
@then("the camera is opened in the page Scan a QR code")
def camera_step_impl(context):
    if not hasattr(context, 'thisScanQRCodePageQC'):
        context.thisScanQRCodePageQC = ScanQRCodePageQC(context.driver)
    assert context.thisScanQRCodePageQC.on_this_page()