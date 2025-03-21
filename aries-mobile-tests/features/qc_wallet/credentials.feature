@Credential @qc_wallet
Feature: Credentials
   In order have confidence and control of my wallet
   As a holder
   I want to be able to add, review, accept, and decline a credential offer

    @T001-Credential @critical @AcceptanceTest
    Scenario: Holder open the "government authentication" website to add his first credential to his wallet
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When the user click on Add my digital Government Authentication Certificate link
        Then the page Request your authentication certificate is displayed
        When the user click on the button Receive my attestation
        Then the website government authentication service opened
        

    @T002-Credential @critical @AcceptanceTest 
    Scenario: Holder open camera in order to scan Qr Code 
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When user click on Scan a QR code button showed in the pop up
        Then allow camera use page is displayed
        When the user click continue button
        Then pop up Access the Camera appears
        When the user Allow the camera access
        Then the camera is opened in the page Scan a QR code

    @T004-Credential @critical @AcceptanceTest
    Scenario: Holder open camera in order to scan Qr Code By clicking on Only this time Android
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When user click on Scan a QR code button showed in the pop up
        Then allow camera use page is displayed
        When the user click continue button
        Then pop up Access the Camera appears
        When the user click Only this time in the camera pop up permission access
        Then the camera is opened in the page Scan a QR code


    @T005-Connect @critical @AcceptanceTest @test1
    Scenario:  Scan QR code to recieve a credential offer (connecting with the issuer)
        Given the user has setup thier wallet
        When the user open credentials page
        And the user click on Add your First Credential button
        Then a modal Add a Credential appear
        When the Holder scans the QR code sent by the "issuer"
        And the Holder select back on the scan camera page and go to Home page
        When the Holder click on "see all notifications" link 
        And the Holder click on History
        Then connection established notification
