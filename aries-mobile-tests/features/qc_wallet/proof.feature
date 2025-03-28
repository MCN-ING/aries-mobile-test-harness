@Proof @qc_wallet
Feature: Proof
   In order to easily prove my credential details to a verifier
   As a holder
   I want to be able to review, accept, and decline a proof request

   @T01-Proof @critical @AcceptanceTest @test1
   Scenario: Holder receives and views the contents of a proof request
      Given the user has setup thier wallet     
      And a connection has been successfully made
      And the holder has a Non-Revocable credential
         | issuer_agent_type  | credential_name     |
         | MCNIssuer          | Test Schema         |
      When the Holder scans the QR code sent by the "verifier"
      And the Holder receives a proof request
      And the holder opens the proof request
      Then holder is brought to the proof request
      Then they can view the contents of the proof request

 @T02-Proof @critical @AcceptanceTest
   Scenario: Holder accepts the proof request
      Given the user has setup thier wallet     
      And a connection has been successfully made
      And the holder has a Non-Revocable credential
         | issuer_agent_type | credential_name |
         | MCNIssuer         | Test Schema     |
      And the user has a proof request
      When they select Share
      And the holder is informed that they are sending information securely
      And they are informed that the information sent successfully
      And they select Go back to home on information sent successfully
      Then they are brought Home

   @T03-Proof @critical @AcceptanceTest
   Scenario: Holder declines the proof request
      Given the user has setup thier wallet     
      And a connection has been successfully made
      And the holder has a Non-Revocable credential
         | issuer_agent_type | credential_name |
         | MCNIssuer         | Test Schema     |
      And the user has a proof request
      When they select Decline
      Then they are asked if they are sure they want to decline the Proof
      And they Confirm the decline
      And they are brought home