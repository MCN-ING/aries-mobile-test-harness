from bc_wallet.terms import *
from override_steps import overrides
from pageobjects.qc_wallet.termsandconditions import TermsAndConditionsPageQC
from pageobjects.qc_wallet.pinsetup import PINSetupPageQC
from pageobjects.qc_wallet.initialization import InitializationPageQC



@overrides("the users accepts the Terms and Conditions", "given")
@overrides("the users accepts the Terms and Conditions", "when")
def accept_terms_step_impl(context):
    context.thisTermsAndConditionsPageQC.select_accept()

@overrides('the User is on the Terms and Conditions screen', "given")
@then("the User is on the Terms and Conditions screen")
def step_impl(context):
        context.thisTermsAndConditionsPageQC = TermsAndConditionsPageQC(context.driver)
        assert context.thisTermsAndConditionsPageQC.on_this_page()

@overrides('the user clicks continue', "given")
@overrides('the user clicks continue', "when")
def step_impl(context):
    context.thisTermsAndConditionsPageQC.select_continue()


@overrides('the User is on the PIN creation screen', "given")
@overrides('the user transitions to the PIN creation screen', "then")
def step_impl(context):
    context.thisPINSetupPageQC = PINSetupPageQC(context.driver)
    context.thisPINSetupPageQC.on_this_page()

@when("the user clicks continue without accepting the Terms and Conditions")
def step_impl(context):
    context.thisTermsAndConditionsPageQC.select_continue()


@given("the user has setup the wallet")
def wallet_setup_step_impl(context):
    context.execute_steps(
        f"""
            Given the User has accepted the Terms and Conditions
            And a PIN has been set up with "369369"
            Then the User transitions to biometric screen
            When the user click continue on the biometrics screen 
        """
    )
@given("the user land on the Home screen and the modal welcome to QC Wallet is displayed")
def step_impl(context):
    context.thisInitializationPageQC = InitializationPageQC(context.driver)
    context.thisHomePageQC = context.thisInitializationPageQC.wait_until_initialized()
    # assert context.thisHomePageQC.on_this_page()
    if context.thisHomePageQC.welcome_to_qc_wallet_modal.is_displayed():
        print("Modal welcome to QC Wallet is displayed")
        assert True
    else:
        assert context.thisHomePageQC.on_this_page()
    if context.thisHomePageQC.on_this_page() == False:
        sleep(5)
    assert context.thisHomePageQC.on_this_page()

      
@when("the user chooses to use app guides")
def app_guides_step_impl(context):
    context.thisHomePageQC.welcome_to_qc_wallet_modal.select_use_app_guides()
    
@then("the add and share credentials modal appears")
def add_and_share_step_impl(context):
    assert context.thisHomePageQC.welcome_to_qc_wallet_modal.add_and_share_credential_modal()
    
@when("the user click next")
@when("the user click done button")
def next_step_impl(context):
    context.thisHomePageQC.welcome_to_qc_wallet_modal.select_next()
    
@then("the notifications modal appears")
def notifications_modal_step_impl(context):
    assert context.thisHomePageQC.welcome_to_qc_wallet_modal.new_modal()

@then("your credentials modal appears")
def notifications_modal_step_impl(context):
    assert context.thisHomePageQC.welcome_to_qc_wallet_modal.new_modal()
    
@then("the user land on the Home screen after using app guides")
def home_screen_step_impl(context):
        assert context.thisHomePageQC.on_this_page()