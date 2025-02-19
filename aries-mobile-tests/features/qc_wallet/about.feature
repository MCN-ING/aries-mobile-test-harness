@AboutQC @qc_wallet @normal
Feature: About 

    @T001-about @AcceptanceTest
    Scenario: User open the About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        Then the about page is displayed 

    @T002-about @AcceptanceTest
    Scenario: User open the Accessibility in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the clicks on Accessibility
        Then Accessibility page is displayed 

    @T003-about @AcceptanceTest
    Scenario: User open the Terms of use from the About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the clicks on the Terms of use
        Then the about page is displayed 

    @T004-about @AcceptanceTest
    Scenario: User check the privacy policy the About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the Holder clicks on privacy policy
        Then the about page is displayed 