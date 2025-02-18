@TContactsQC @qc_wallet @normal
Feature: Contacts

    @T001-contacts @AcceptanceTest
    Scenario: User open contacts page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open contacts page
        Then the contacts page is displayed 

    @T002-contacts @AcceptanceTest
    Scenario: User check what are contacts link
        Given the Holder is on the contacts page and the wallet is empty
        When the Holder click on What are Contacts link
        Then What are Contacts page is displayed 

    @T003-contacts @AcceptanceTest @test01
    Scenario: User check contacts list when the list is empty
        Given the Holder is on the contacts page and the wallet is empty
        When the Holder click on What are Contacts link
        Then What are Contacts page is displayed 
        When the user click on contact list link
        Then the contacts page is displayed  