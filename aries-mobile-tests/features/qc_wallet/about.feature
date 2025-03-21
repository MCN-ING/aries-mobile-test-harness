@AboutQC @qc_wallet @normal
Feature: About 
    in order to understand the terms of use of the wallet and the privacy policy and the accessibility, 
    As a holder who is curious about the wallet i can have access to these functionnalities and read it 

    @T001-about @AcceptanceTest 
    Scenario: User open the About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        Then the about page is displayed 

    @T002-about @AcceptanceTest @wip
    Scenario: User open the Accessibility Link in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the holder clicks on Accessibility
        Then Accessibility page is displayed 

    @T003-about @AcceptanceTest @wip
    Scenario: User open the Terms of use Link in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the holder clicks on Terms of Use
        Then Terms of Use page is displayed 

    @T004-about @AcceptanceTest @wip
    Scenario: User check the privacy policy Link in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the Holder clicks on Privacy Policy
        Then Privacy Policy page is displayed 