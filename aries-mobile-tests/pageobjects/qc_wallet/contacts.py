import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.bc_wallet.contacts import ContactsPage
from pageobjects.bc_wallet.contact import ContactPage
from pageobjects.qc_wallet.what_are_contacts import WhatAreContactsPageQC

class ContactsPageQC(ContactsPage):
    """Contacts page object"""

    # Locators
    on_this_page_text_locator = "Contacts"
    contact_locator = (AppiumBy.ID, "com.ariesbifold:id/Contact")
    what_are_contacts_locator = (AppiumBy.ID, "com.ariesbifold:id/WhatAreContacts?")


    def on_this_page(self):     
        return super().on_this_page() 

    def select_contact(self, name:str):
        if self.on_this_page():
            contacts = self.find_multiple_by(self.contact_locator)
            # click the first contact for now since the UI will get reworked and will get the contact.text at that time.
            contacts[0].click()
            # for contact in contacts:
            #     if contact.text == name:
            #         contact.click()
            # return a new page object for the Contacts page
            return ContactPage(self.driver)
            #         return True
            # raise Exception(f"Contact {name} not found")
        else:
            raise Exception(f"App not on the {type(self)}") 

    def is_contact_present(self, name) -> bool:
        if self.on_this_page():
            if name in self.driver.page_source:
                return True
            else:
                return False
        else:
            raise Exception(f"App not on the {type(self)}")

    def select_what_are_contacts_link(self):
        if self.on_this_page():
            self.find_by(self.what_are_contacts_locator).click()
            return WhatAreContactsPageQC(self.driver)
        else:
            raise Exception(f"App not on the {type(self)} page")
