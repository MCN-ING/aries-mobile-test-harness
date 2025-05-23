@HelpCenterQC @qc_wallet
Feature: Help Center

    @T01-helpCenter @AcceptanceTest 
    Scenario: User open help center page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open help center page
        Then Help Center page is displayed 

    @T02-helpCenter @AcceptanceTest
    Scenario: User open what is a PIN info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on PIN
        Then What is a PIN info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed 

    @T03-helpCenter @AcceptanceTest
    Scenario: User open what is Biometrics info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on Biometrics
        Then what is Biometrics info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed 

    @T04-helpCenter @AcceptanceTest 
    Scenario: User open what is a history info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on activities in the help module
        Then what is a history info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed 

    @T05-helpCenter @AcceptanceTest 
    Scenario: User open the what is PNG info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on PNG
        Then what is png info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed 

    @T06-helpCenter @AcceptanceTest 
    Scenario: User open receive presentation request info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on Receive presentation request
        Then Receive a presentation request info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed

    @T07-helpCenter @AcceptanceTest 
    Scenario: User open receive a certificate offer info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on Receive a Certificate Offer
        Then receive a certificate offer info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed

    @T08-helpCenter @AcceptanceTest 
    Scenario: User open delete a certificate info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on Delete a certificate
        Then delete a certificate info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed

    @T09-helpCenter @AcceptanceTest
    Scenario: User open scan a QR code info page in the help center module
        Given the Holder is on the help center page
        When the Holder click on Scan a QR code
        Then scan a QR code info page is displayed
        When the Holder click on return to Help Center button
        Then Help Center page is displayed