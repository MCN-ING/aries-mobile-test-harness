# -----------------------------------------------------------
# Behave Step Definitions for an issuer offering a credential to a wallet user
#
# -----------------------------------------------------------

import json
from time import sleep
from override_steps import overrides
import logging

# Local Imports
from agent_controller_client import (agent_controller_GET,
                                     agent_controller_POST,
                                     expected_agent_state,
                                     setup_already_connected)
from agent_test_utils import get_qr_code_from_invitation
from behave import given, step, then, when
from pageobjects.bc_wallet.contact import ContactPage
from pageobjects.bc_wallet.credential_added import CredentialAddedPage

from bc_wallet.credential_offer import *
from pageobjects.qc_wallet.credential_offer import CredentialOfferPageQC
# import Page Objects needed
# from pageobjects.bc_wallet.credential_offer_notification import CredentialOfferNotificationPage
from pageobjects.bc_wallet.credential_offer import CredentialOfferPage
from pageobjects.qc_wallet.credentials import CredentialsPageQC
from pageobjects.bc_wallet.credential_details import CredentialDetailsPage
from pageobjects.qc_wallet.navbar import NavBarQC
from pageobjects.qc_wallet.notifications import NotificationsPageQC
from pageobjects.qc_wallet.credential_details import CredentialDetailsPageQC

@overrides("the Holder receives a Non-Revocable credential offer", "when")
def step_impl(context):
    context.issuer.send_credential()
    
    
@overrides("the holder opens the credential offer", "step")
def step_impl(context):
    # Select the credential offer
    context.thisHomePageQC.select_open_credential_offer()
    
    
    
@overrides("they can view the contents of the credential", "then")
def step_impl(context):
    assert context.thisCredentialOfferPage.on_this_page()

    cred_type, attributes, values = get_expected_credential_detail(context)
    # TODO The below doesn't have locators in build 127. Calibrate in the future fixed build
    # actual_who, actual_cred_type, actual_attributes, actual_values = context.thisCredentialOfferPage.get_credential_details()
    # assert who in actual_who
    # assert cred_type in actual_cred_type
    # assert attributes in actual_attributes
    # assert values in actual_values
    

def get_expected_credential_detail(context):
    issuer_type_in_use = context.issuer.get_issuer_type()
    found = False
    for row in context.table:
            cred_type = row["cred_type"]
            attributes = row["attributes"].split(";")
            values = row["values"].split(";")
            found = True
            # get out of loop at the first found row. Can't see a reason for multiple rows of the same agent type
            break
    if found == False:
        raise Exception(f"No credential details in table data for {issuer_type_in_use}")
    return cred_type, attributes, values


@overrides("the user has a credential offer", "given")
def step_impl(context):
    context.execute_steps(
        f"""
        When the Holder receives a Non-Revocable credential offer
        And the holder opens the credential offer
        Then holder is brought to the credential offer screen
    """
    )
    
    
@when('they select Decline the credential')
def decline_impl(context):
    context.thisDeclineCredentialOffer = context.thisCredentialOfferPage.select_decline(
        scroll=True)
    context.thisHomePage = context.thisDeclineCredentialOffer.select_decline()


########################################################################


@overrides("the credential accepted is at the top of the list", "then")
def step_impl(context, credential_name=None):
    # if the platform is iOS 15+ or android
    if (
        context.driver.capabilities["platformName"]
        and context.driver.capabilities["platformVersion"] >= "15"
    ) or context.driver.capabilities["platformName"].lower() == "Android".lower():
        json_elems = context.thisCredentialsPageQC.get_credentials()
        if credential_name == None:
            credential_name = get_expected_credential_name(context)

        assert credential_name in json_elems["credentials"][0]["text"]
    else:
        if credential_name == None:
            credential_name = get_expected_credential_name(context)
        assert context.thisCredentialsPageQC.credential_exists(credential_name)
        

def get_expected_credential_name(context):
    issuer_type_in_use = context.issuer.get_issuer_type()
    logging.info(f"Issuer type in use: {issuer_type_in_use}")  # Ajout pour debug
    logging.info(f"Available rows in table: {[row['issuer_agent_type'] for row in context.table]}")  # Debug
 
    found = False
    for row in context.table:
        if row["issuer_agent_type"] == issuer_type_in_use:
            cred_name = row["credential_name"]
            found = True
            # get out of loop at the first found row. Can't see a reason for multiple rows of the same agent type
            break
    if found == False:
        raise Exception(f"No credential name in table data for {issuer_type_in_use}")
    return cred_name



@overrides('holder is brought to the credential offer screen', 'then')
def cred_offer_step_impl(context):
    # Workaround for bug 645
    context.execute_steps(f'''
        When the connection takes too long reopen app and select notification
    ''')

    context.thisCredentialOfferPage = CredentialOfferPageQC(context.driver)
    assert context.thisCredentialOfferPage.on_this_page()

@overrides("they are brought to the list of credentials", "then")
def step_impl(context):
     context.thisCredentialsPageQC.on_this_page()
    
@when("the holder delete the credential")
def delete_credential(context):
    context.thisCredentialsPageQC.select_top_credential()
    if hasattr(context, "thisCredentialDetailsPageQC") == False:
        context.thisCredentialDetailsPageQC = CredentialDetailsPageQC(context.driver)
    remove_modal = context.thisCredentialDetailsPageQC.select_remove_from_wallet()
    remove_modal.select_confirm_remove_from_wallet()    

@then("credential deleted and the user is brought to the list of credentials")
def credential_deleted(context):
    assert context.thisCredentialsPageQC.on_this_page()
    
@overrides("they select Done", "then")
@overrides("they select Done", "when")
def step_impl(context):
    # TODO we could be on the home page at this point. Should we fail the last step, fail this one, or try the cred accept again?
    if hasattr(context, "thisCredentialsPageQC") == False:
        # This means we probably went to the Home Page above. Revisit this if the this happens too much.
        context.thisCredentialAddedPage = CredentialAddedPage(context.driver)
    context.thisCredentialsPageQC = context.thisCredentialAddedPage.select_done()
    
@when("the user check the history page")
def go_to_history(context):
    if hasattr(context, "thisNavBarQC") == False:
        context.thisNavBarQC= NavBarQC(context.driver)
    context.thisNavBarQC.select_activities()
    if not hasattr(context, "thisNotificationsPageQC"):
        context.thisNotificationsPageQC = NotificationsPageQC(context.driver)
    context.thisHistoryPageQC= context.thisNotificationsPageQC.select_history()
    sleep(100)
    
@given("the user accepts the credential offer and brought to the list of credentials")
def accept_credential(context):
        context.execute_steps(
        """
        When they select Accept
        And the holder is informed that their credential is on the way with an indication of loading
        And once the credential arrives they are informed that the Credential is added to your wallet
        And they select Done
        Then they are brought to the list of credentials
        """
        )
        
@overrides('holder is brought to the credential offer screen', 'then')
def cred_offer_step_impl(context):
    # Workaround for bug 645
    context.execute_steps(f'''
        When the connection takes too long reopen app and select notification
    ''')

    context.thisCredentialOfferPage = CredentialOfferPageQC(context.driver)
    assert context.thisCredentialOfferPage.on_this_page()

@overrides("a connection has been successfully made", "given")
def connection_step_impl(context):
    context.execute_steps(
        """
        When the Holder scans the QR code sent by the "issuer"
        And the Connecting completes successfully
    """
    )
    
@then("card accepted notification is added to the history page") 
def card_accepted(context):
    assert context.thisHistoryPageQC.card_accepted()
    
    
@then("card declined notification is added to the history page")
def card_declined_notification(context):
    assert context.thisHistoryPageQC.card_declined()