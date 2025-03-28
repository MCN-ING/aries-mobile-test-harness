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
         | cred_name    | attributes           | values                  |
         | Test Schema  | Attr 1;Attr 2;Attr 3 | value_1;value_2;value_3 |


   @T02-CredentialOffer @critical @AcceptanceTest @test1
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


  @T07-Credential @critical @AcceptanceTest
    Scenario: Holder try to add his digital Government Authentication Certificate to the wallet
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When the user click on Add my digital Government Authentication Certificate link
        Then the page Request your authentication certificate is displayed
        When the user click on the button Receive my attestation
        Then the website government authentication service opened
        

    @T08-Connect @critical @AcceptanceTest
    Scenario:  Scan QR code in order to recieve a credential offer (connecting with the issuer)
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When the Holder scans the QR code sent by the "issuer"
        And the Holder select back on the scan camera page and go to Home page
        When the Holder click on "see all notifications" link 
        And the Holder click on History
        Then connection established notification is added to the history page 

