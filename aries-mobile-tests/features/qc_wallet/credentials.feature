@Credential @qc_wallet
Feature: Credentials
   In order have confidence and control of my wallet
   As a holder
   I want to be able to add, review, accept, and decline a credential offer

    @T001-Credential @critical @AcceptanceTest
    Scenario: Holder add his first credential to his wallet
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When the user click on Add my digital Government Authentication Certificate link
        Then the page Request your authentication certificate is displayed
        When the user click on the button Receive my attestation
        Then the website government authentication service opened
        

    @T002-Credential @critical @AcceptanceTest @test1
    Scenario: Holder add his first credential to his wallet by scanning Qr Code
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When user click on Scan a QR code button showed in the pop up
        Then allow camera to use page is displayed
        When the user click continue button
        Then modal “Portefeuille QC” Would Like to Access the Camera appears
        When the user click Allow for the camera access
        Then the camera is opened in the page Scan a QR code