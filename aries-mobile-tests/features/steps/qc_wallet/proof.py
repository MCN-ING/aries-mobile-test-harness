from bc_wallet.proof import *
from override_steps import overrides
from time import sleep
from pageobjects.qc_wallet.navbar import NavBarQC



@overrides('they can view the contents of the proof request', 'then')
def step_impl(context):
    if not hasattr(context, "thisProofRequestPage") or context.thisProofRequestPage is None:
        context.thisProofRequestPage = ProofRequestPage(context.driver)
    assert context.thisProofRequestPage.on_this_page()
    cred_type, attributes, values = get_expected_proof_request_detail(context)
    # # The below doesn't have locators in build 127. Calibrate in the future fixed build
    # (
    #     actual_attributes,
    #     actual_values,
    # ) = context.thisProofRequestPage.get_proof_request_details()
    # assert all(item in attributes for item in actual_attributes)
    # assert all(item in values for item in actual_values)
    
        
def get_expected_proof_request_detail(context):
    verifier_type_in_use = context.verifier.get_issuer_type()
    found = False
    for row in context.table:
            cred_type = row["cred_type"]
            attributes = row["attributes"].split(";")
            values = row["values"].split(";")
            found = True
            # get out of loop at the first found row. Can't see a reason for multiple rows of the same agent type
    if found == False:
        raise Exception(
            f"No credential details in table data for {verifier_type_in_use}"
        )
    return cred_type, attributes, values
  
    
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