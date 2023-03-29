from appium.webdriver.common.appiumby import AppiumBy
from pageobjects.basepage import BasePage
from pageobjects.basepage import WaitCondition
from pageobjects.bc_wallet.credential_on_the_way import CredentialOnTheWayPage


# These classes can inherit from a BasePage to do common setup and functions
class CredentialOfferPage(BasePage):
    """Credential Offer Notification page object"""

    # Locators
    on_this_page_text_locator = "is offering you a credential"
    credential_locator = "offer"
    who_locator = "issuer"
    cred_type_locator = "credential type"
    attribute_locator = "attribute"
    value_locator = "value"
    credential_offer_card_locator = (AppiumBy.ID, "com.ariesbifold:id/CredentialCard")
    accept_locator = (AppiumBy.ID, "com.ariesbifold:id/AcceptCredentialOffer")
    accept_aid_locator = (AppiumBy.ACCESSIBILITY_ID, "Accept")
    decline_locator = (AppiumBy.ID, "com.ariesbifold:id/DeclineCredentialOffer")
    decline_aid_locator = (AppiumBy.ACCESSIBILITY_ID, "Decline")

    def on_this_page(self):
        #return super().on_this_page(self.on_this_page_text_locator, 30)
        if self.current_platform == 'iOS':
            if '14' in self.driver.capabilities['platformVersion']:
                return super().on_this_page(self.on_this_page_text_locator, 30)
        #return super().on_this_page(self.credential_offer_card_locator, 30)
        if self.find_by(self.credential_offer_card_locator, timeout=80, wait_condition=WaitCondition.VISIBILITY_OF_ELEMENT_LOCATED):
            return True
        else:
            return False

    def select_accept(self, scroll=False):
        if self.on_this_page():
            # if the credential has a lot of attributes it could need to scroll
            if scroll == True:
                try:
                    self.scroll_to_element(self.decline_aid_locator[1])
                except:
                    # Sometimes it seems that scrolling may try to access the element by accessibility id before it appears
                    # if we get this failure then just sleep and try again. 
                    sleep(5)
                    self.scroll_to_element(self.decline_aid_locator[1])
                self.find_by(self.accept_locator).click()
            else:
                self.find_by(self.accept_locator).click()
            return CredentialOnTheWayPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def select_decline(self):
        if self.on_this_page():
            self.find_by(self.decline_locator).click()
            # Not sure what is returned here yet
            # return CredentialOfferPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")

    def get_credential_details(self):
        if self.on_this_page():
            who = self.find_by_accessibility_id(self.who_locator).text
            cred_type = self.find_by_accessibility_id(self.cred_type_locator).text
            attribute_elements = self.find_multiple_by_id(self.attribute_locator)
            value_elements = self.find_multiple_by_id(self.values_locator)
            attributes = []
            for attribute in attribute_elements:
                attributes.append(attribute.text)
            values = []
            for value in value_elements:
                values.append(value.text)
            return who, cred_type, attributes, values
        else:
            raise Exception(f"App not on the {type(self)} page")
