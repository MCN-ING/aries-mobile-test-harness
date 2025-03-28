@pageAccess @qc_wallet
Feature: wallet pages access 
    in order to understand how to use the wallet 
    As a curious holder,
    first thing after installing the application, i'll open all the differect pages of the wallet

    @T01-pageAcess @notifications @FunctionalTest 
    Scenario: User open page activities and check notifications
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder click on Activities
        Then notifications page is displayed

    @T02-pageAcess @notifications @FunctionalTest
    Scenario: User open notifications link on the home page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder click on "see all notifications" link 
        Then notifications page is displayed

    @T03-pageAcess @history @FunctionalTest
    Scenario: User open page History 
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder click on Activities
        Then notifications page is displayed
        When the Holder click on History
        Then History page is displayed

    @T04-pageAcess @contacts @AcceptanceTest 
    Scenario: User open page contacts
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open contacts page
        Then the contacts page is displayed 

    @T05-pageAcess @AcceptanceTest 
    Scenario: User check what are contacts link
        Given the Holder is on the contacts page and the wallet is empty
        When the Holder click on What are Contacts link
        Then What are Contacts page is displayed 


    @T06-pageAcess @AcceptanceTest
    Scenario: User open the About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        Then the about page is displayed 

    @T07-pageAcess @AcceptanceTest @wip
    Scenario: User open the Accessibility Link in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the holder clicks on Accessibility
        Then Accessibility page is displayed 

    @T08-pageAcess @AcceptanceTest @wip
    Scenario: User open the Terms of use Link in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the holder clicks on Terms of Use
        Then Terms of Use page is displayed 

    @T09-pageAcess @AcceptanceTest @wip
    Scenario: User check the privacy policy Link in About page
        Given the Holder has setup thier Wallet and land on the Home screen
        When the Holder opens more options page
        And the Holder open the about page
        And the Holder clicks on Privacy Policy
        Then Privacy Policy page is displayed 

    @T10-@pageAccess @credential @AcceptanceTest
    Scenario: Holder open credentials page 
        Given the user has setup thier wallet
        When the user open credentials page
        Then credential page appears