@ActivitiesQC @qc_wallet
Feature: check your Wallet activities


 @T001-Activities @FunctionalTest @normal
  Scenario: User open the activities page to check notifications
    Given the Holder has setup thier Wallet and land on the Home screen
    When the Holder click on Activities
    Then notifications page is displayed

   @T001-Activities @FunctionalTest @normal
  Scenario: User open notifications from the home page
    Given the Holder has setup thier Wallet and land on the Home screen
    When the Holder click on "see all notifications" link 
    Then notifications page is displayed

 @T002-Activities @FunctionalTest @normal
  Scenario: User open the History page 
    Given the Holder has setup thier Wallet and land on the Home screen
    When the Holder click on Activities
    Then notifications page is displayed
    When the Holder click on History
    Then History page is displayed
