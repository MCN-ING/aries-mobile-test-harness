from bc_wallet.connect import *
from override_steps import overrides
from pageobjects.qc_wallet.biometrics import BiometricsPageQC


@overrides('a PIN has been set up with "{pin}"', "given")
def step_impl(context, pin):
    # context.execute_steps(f'''
    #     Given the User is on the PIN creation screen
    #     When the User enters the first PIN as "{pin}"
    #     And the User re-enters the PIN as "{pin}"
    #     And the User selects Create PIN
    #     And the User selects to use Biometrics
    #     Then the User has successfully created a PIN
    # ''')
    context.execute_steps(
        f"""
        Given the User is on the PIN creation screen
        When the User enters the first PIN as "{pin}"
        And the User re-enters the PIN as "{pin}"
        And the User selects Create PIN
    """
    )
    
@overrides('the Holder scans the QR code sent by the "{agent}"', "when")
def step_impl(context, agent):
    # check the device serivce handler to see if we are on a tablet or phone
    if context.device_service_handler.is_current_device_a_tablet():
        qr_code_border = 80
    else:
        qr_code_border = 40

    if agent == "issuer":
        print("Issuing crendential...")
        qrimage = context.issuer.create_invitation(
            print_qrcode=context.print_qr_code_on_creation,
            save_qrcode=context.save_qr_code_on_creation,
            qr_code_border=qr_code_border,
        )
    elif agent == "verifier":
        print("Proof request...")
        qrimage = context.verifier.create_invitation(
            print_qrcode=context.print_qr_code_on_creation,
            save_qrcode=context.save_qr_code_on_creation,
            qr_code_border=qr_code_border,
        )
    else:
        raise Exception(f"Invalid agent type: {agent}")

    context.device_service_handler.inject_qrcode(qrimage)

    if hasattr(context, "thisNavBar") == False:
        context.thisNavBar = NavBar(context.driver)
    context.thisCameraPrivacyPolicyPageQC = context.thisCredentialsPageQC.add_a_credential_modal.select_scan_qr_code()

    # If this is the first time the user selects scan, then they will get a Camera Privacy Policy that needs to be dismissed
    # TODO only do this if the platorm is iOS. Android is not showing the policy page at present in Sauce Labs becasue we have autoGrantPermissions on.
    # if context.driver.capabilities["platformName"].lower() == "iOS".lower():
    if context.thisCameraPrivacyPolicyPageQC.on_this_page():
        context.thisCameraPrivacyPolicyPageQC.select_continue()
        context.thisCameraPrivacyPolicyPageQC.identiQc_access_camera_permission_modal.select_allow()

        # else:
        #     # soft assert that the camera privacy policy page was not displayed
        #     logging.info(
        #         "Soft Assertion failed. Not on the Camera Privacy Policy Page. MAy cause preceeding connection steps to fail"
        #     )

