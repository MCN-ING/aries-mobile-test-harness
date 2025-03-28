from bc_wallet.proof import *
from override_steps import overrides
from time import sleep
from pageobjects.qc_wallet.navbar import NavBarQC
import logging



@overrides('they can view the contents of the proof request', 'then')
def step_impl(context):
    if not hasattr(context, "thisProofRequestPage") or context.thisProofRequestPage is None:
        context.thisProofRequestPage = ProofRequestPage(context.driver)
    assert context.thisProofRequestPage.on_this_page()
    assert context.thisProofRequestPage.proof_request_details_are_visible()
  
    
@overrides("the holder has a Non-Revocable credential", "given")
def step_impl(context):
    context.execute_steps(
        """
        Given the user has a credential offer
        When they select Accept
        And the holder is informed that their credential is on the way with an indication of loading
        And once the credential arrives they are informed that the Credential is added to your wallet
        And they select Done
        Then they are brought to the list of credentials
        And the credential accepted is at the top of the list
        {table}
    """.format(
            table=table_to_str(context.table)
        )
    )
    if hasattr(context, "thisNavBarQC") == False:
        context.thisNavBarQC= NavBarQC(context.driver)
    context.thisHomePageQC= context.thisNavBarQC.select_home()

@overrides("the Holder receives a proof request", "when")
def step_impl(context, proof=None, interval=None):
    # Make sure the connection is successful first.
    context.execute_steps(
        """
        Then there is a connection between "verifier" and Holder
    """
    )

    if proof is None:
        context.verifier.send_proof_request()
    else:
        # open the proof data file
        try:
            proof_json_file = open("features/data/" + proof.lower() + ".json")
            proof_json = json.load(proof_json_file)
            # check if we are adding a revocation interval to the proof request and add it.
            if interval:
                proof_json["non_revoked"] = create_non_revoke_interval(interval)[
                    "non_revoked"
                ]

            # Add the proof json to the context so we can use it later steps for test verification
            context.proof_json = proof_json

            # send the proof request
            context.verifier.send_proof_request(request_for_proof=proof_json)
        except FileNotFoundError:
            print("FileNotFoundError: features/data/" + proof.lower() + ".json")


@overrides("the holder opens the proof request", "when")
def step_impl(context):
    context.thisProofRequestPage = context.thisHomePageQC.select_open_proof_request()

@overrides("holder is brought to the proof request", "then")
def step_impl(context):
    # Sometimes the proof request comes in a goal code and the user never goes to the Contact Page.
    # In this case check that the ProofRequestPage is in context and if not, create it.
    if not hasattr(context, "thisProofRequestPage") or context.thisProofRequestPage is None:
        context.thisProofRequestPage = ProofRequestPage(context.driver)
    assert context.thisProofRequestPage.on_this_page()
    
    
@overrides("the user has a proof request", "when")
@overrides("the user has a proof request", "given")
def step_impl(context):
    # if the context has a table then use the table to create the proof request
    if context.table:
        proof = context.table[0]["proof"]
        # get the interval for revocation as well, if it doesn't exist in the table then just move on.
        try:
            interval = context.table[0]["interval"]
        except KeyError:
            interval = None

        context.execute_steps(
            f"""
            When the user has a proof request for {proof}
        """
        )
    else:
        context.execute_steps(
            f"""
            When the Holder scans the QR code sent by the "verifier"
            And the Connecting completes successfully
            And the Holder receives a proof request
            And the holder opens the proof request
            Then holder is brought to the proof request
        """
        )
        
    sleep(60)