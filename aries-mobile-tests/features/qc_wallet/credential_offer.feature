@CredentialOffer @qc_wallet
Feature: Offer a Credential
   In order have confidence and control of my wallet
   As a holder, I want to be able to review, accept, and decline a credential offer

   @T01-CredentialOffer @critical @AcceptanceTest 
   Scenario: Holder receives and views the contents of a credential offer
      Given the user has setup thier wallet    
      And a connection has been successfully made
      When the Holder receives a Non-Revocable credential offer
      And the holder opens the credential offer
      Then holder is brought to the credential offer screen
      And they can view the contents of the credential
         | cred_type    | attributes           | values                  |
         | Test Schema. | Attr 1;Attr 2;Attr 3 | value_1;value_2;value_3 |


   @T02-CredentialOffer @critical @AcceptanceTest 
   Scenario: Holder declines the credential offer recieved
      Given the user has setup thier wallet
      And a connection has been successfully made
      And the user has a credential offer
      When they select Decline the credential
      Then they are brought Home


   @T03-CredentialOffer @critical @AcceptanceTest 
   Scenario: Holder accepts the credential offer recieved
      Given the user has setup thier wallet
      And a connection has been successfully made
      And the user has a credential offer
      When they select Accept
      And the holder is informed that their credential is on the way with an indication of loading
      And once the credential arrives they are informed that the Credential is added to your wallet
      And they select Done
      Then they are brought to the list of credentials
      And the credential accepted is at the top of the list
         | issuer_agent_type  | credential_name     |
         | MCNIssuer          | Test Schema         |


   @T04-CredentialOffer @critical @AcceptanceTest
   Scenario: Holder accepts the credential offer recieved Then check notification in the history page
      Given the user has setup thier wallet
      And a connection has been successfully made
      And the user has a credential offer
      And the user accepts the credential offer and brought to the list of credentials
      When the user check the history page
      Then card accepted notification is added to the history page


   @T05-CredentialOffer @critical @AcceptanceTest
   Scenario: Holder decline the credential offer recieved Then check the notification
      Given the user has setup thier wallet
      And a connection has been successfully made
      And the user has a credential offer
      When they select Decline the credential
      Then they are brought Home
      When the user check the history page
      Then card declined notification is added to the history page 

   
   @T06-CredentialOffer @critical @AcceptanceTest
   Scenario: Holder delete the credential  
      Given the user has setup thier wallet
      And a connection has been successfully made
      And the user has a credential offer
      And the user accepts the credential offer and brought to the list of credentials
      When the holder delete the credential
      Then credential deleted and the user is brought to the list of credentials
