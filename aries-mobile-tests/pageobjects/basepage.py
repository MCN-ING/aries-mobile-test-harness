import xml.etree.ElementTree as ET
from enum import Enum
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WaitCondition(Enum):
    ELEMENT_TO_BE_CLICKABLE = EC.element_to_be_clickable
    PRESENCE_OF_ELEMENT_LOCATED = EC.presence_of_element_located
    VISIBILITY_OF_ELEMENT_LOCATED = EC.visibility_of_element_located
    INVISIBILITY_OF_ELEMENT_LOCATED = EC.invisibility_of_element_located


# BasePage to do common setup and functions
class BasePage(object):
    """A base page object to do things common to all page objects"""

    def back(self, context):
        pass

    def set_device(self, context):
        self.driver = context.driver

    def on_this_page(self, locator, timeout=10):
        if type(locator) is tuple:
            try:
                self.find_by(locator, timeout)
                return True
            except:
                return False
            # if self.find_by(locator, timeout):
            #     return True
            # else:
            #     return False
        else:
            found_locator = False
            i = 0
            while found_locator == False and i < timeout:
                if locator in self.get_page_source():
                    found_locator = True
                else:
                    found_locator = False
                i = i + 1
            return found_locator

    # Initialize and define the type of driver as WebDriver

    def __init__(self, driver):
        self.driver = driver
        self.current_platform = str(driver.capabilities["platformName"])

    def get_app_language(self):
        language = "English"
        if self.current_platform.lower() == "Android".lower():
            language = (
                "English" if self.driver.capabilities["language"] == "en" else "French"
            )
        else:
            args_list = self.driver.capabilities["processArguments"]["args"]
            appleLanguagesIndex = args_list.index("-AppleLanguages")
            if (
                appleLanguagesIndex + 1 < len(args_list)
                and args_list[appleLanguagesIndex + 1] == "(en)"
            ):
                language = "English"
            else:
                language = "French"
        return language

    def find_by(
        self,
        locator_tpl: tuple,
        timeout=20,
        wait_condition: WaitCondition = WaitCondition.PRESENCE_OF_ELEMENT_LOCATED,
    ):
        if locator_tpl[0] == AppiumBy.ACCESSIBILITY_ID:
            return self.find_by_accessibility_id(
                locator_tpl[1], timeout, wait_condition
            )
        elif locator_tpl[0] == AppiumBy.ID:
            return self.find_by_element_id(locator_tpl[1], timeout, wait_condition)
        else:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    wait_condition((locator_tpl[0], locator_tpl[1]))
                )
            except:
                raise Exception(
                    f"Could not find element {locator_tpl[0]} with Locator {locator_tpl[1]}"
                )

    def find_multiple_by(self, locator_tpl: tuple, timeout=20):
        if locator_tpl[0] == AppiumBy.ACCESSIBILITY_ID:
            return self.find_multiple_by_accessibility_id(locator_tpl[1], timeout)
        elif locator_tpl[0] == AppiumBy.ID:
            # It may be that Android will return none when looking for multiple
            # so if we get an empty element array here try find_by instead.
            elems = self.find_multiple_by_id(locator_tpl[1], timeout)
            if len(elems) == 0:
                elem = self.find_by_element_id(locator_tpl[1], timeout)
                elems.append(elem)
            return elems
            # return self.find_multiple_by_id(locator_tpl[1], timeout)

    # Locate by Accessibility id
    def find_by_accessibility_id(
        self,
        locator,
        timeout=20,
        wait_condition: WaitCondition = WaitCondition.PRESENCE_OF_ELEMENT_LOCATED,
    ):
        try:
            # The location of a single element gets the location of a single element
            return WebDriverWait(self.driver, timeout).until(
                wait_condition((AppiumBy.ACCESSIBILITY_ID, locator))
            )
        except:
            # try:
            #     # If there is a problem with the accessibility id, try doing it by name.
            #     # return WebDriverWait(self.driver, 20).until(
            #     #     EC.presence_of_element_located((MobileBy.NAME, locator))
            #     # )
            #     return self.driver.find_element_by_name(locator)
            # except:
            raise Exception(
                f"Could not find element by Accessibility id Locator {locator}"
            )

    # Locate multiple elements by Accessibility id.
    # this is a workaround for when iOS may have translated the labels down into text and input fields.
    # we shouldn't be calling this very much, and when we have to, we should log an issue with the wallet for unique accessibilituy IDs
    def find_multiple_by_accessibility_id(self, locator, timeout=20):
        try:
            # The location of a single element gets the location of a single element
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(
                    (AppiumBy.ACCESSIBILITY_ID, locator)
                )
            )
        except:
            raise Exception(f"Could not find elements by Accessibility id {locator}")

    # Locate multiple elements by id.
    def find_multiple_by_id(self, locator, timeout=20):
        try:
            # The location of a single element gets the location of a single element
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, locator))
            )
        except:
            raise Exception(f"Could not find elements by id {locator}")

    # Locate by id
    def find_by_element_id(
        self,
        locator,
        timeout=20,
        wait_condition: WaitCondition = WaitCondition.PRESENCE_OF_ELEMENT_LOCATED,
    ):
        try:
            # The location of a single element gets the location of a single element
            return WebDriverWait(self.driver, timeout).until(
                wait_condition((AppiumBy.ID, locator))
            )
        except TimeoutException:
            raise
        except:
            raise Exception(f"Could not find element by element id Locator {locator}")

    def get_page_source(self):
        return self.driver.page_source

    # Positioning according to xpath
    def find_by_xpath(self, locator):
        try:
            # The location of a single element gets the location of a single element
            return self.driver.find_element_by_xpath(locator)
        except:
            # To locate multiple same xpath elements, you can get a list. You can use the list query for the location of a specific element (xpath is the only location, generally it is not necessary to use this method)
            return self.driver.find_elements(locator)

    # Positioning according to classname
    def find_by_classname(self, *locator):
        # classname location is rarely used. It is generally used when id location and xpath location cannot be used. What you get is a list. You can use the list to query the location of a specific element
        return self.driver.find_elements_by_class_name(*locator)

    # def scroll_to_element(self, locator, incremental_scroll_amount=500, timeout=20, find_by=MobileBy.ACCESSIBILITY_ID):
    #     """ deprecated """
    #     element = None
    #     i = 0
    #     while element == None and i < timeout:
    #         try:
    #             if find_by == MobileBy.ACCESSIBILITY_ID:
    #                 element = self.find_by_accessibility_id(locator)
    #             else:
    #                 element = self.find_by_element_id(locator)
    #             self.driver.swipe(500, incremental_scroll_amount, 500, 100)
    #         except:
    #             # not found try again
    #             i = i + 1
    #     if element:
    #         return True
    #     else:
    #         return False

    def scroll_to_element(self, locator: str, direction="down"):
        """Scroll to the element based on the accessibility id given."""
        """ The locator MUST be an accessibility id. """
        """ Can give a direction and the direction only applies to iOS. Default is down. """

        # Works great for Android, but iOS has different parameters
        if self.current_platform.lower() == "Android".lower():
            self.driver.execute_script(
                "mobile: scroll", {"strategy": "accessibility id", "selector": locator}
            )
        else:
            # Message: Mobile scroll supports the following strategies: name, direction, predicateString, and toVisible. Specify one of these
            # iOS
            el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, locator)
            self.driver.execute_script(
                "mobile: scroll", {"direction": direction, "element": el}
            )

    def scroll_to_bottom(self):
        # Get the screen size
        screen_size = self.driver.get_window_size()
        screen_height = screen_size["height"]

        before_source_ios = self.driver.page_source

        # Scroll down the page until the bottom is reached
        while True:
            if self.current_platform.lower() == "iOS".lower():
                before_root = ET.fromstring(before_source_ios.encode("utf-8"))
                self.driver.execute_script("mobile: scroll", {"direction": "down"})
            else:
                # Scroll for android takes an accessibility id, however it will scroll to the bottom looking for that id and if it doesn't exist,
                # will throw and error. If we give it a non-existent accessibility id, and catch the error and continue we should be at the bottom.
                try:
                    self.scroll_to_element(
                        "this element doesn't exist, it is here to make android scroll to the bottom"
                    )
                except:
                    pass

            # Get the current scroll position
            if self.current_platform == "iOS":
                after_source_ios = self.driver.page_source
                # Parse the hierarchies using an XML parser
                after_root = ET.fromstring(after_source_ios.encode("utf-8"))

                before_last_element = self.get_last_ios_element_on_page(before_root)
                after_last_element = self.get_last_ios_element_on_page(after_root)

                # Compare the tag_name of the last iOS elements to determine if we have reached the bottom
                if before_last_element is not None and after_last_element is not None:
                    if before_last_element.tag == after_last_element.tag:
                        break

                # Update the page source for the next iteration
                before_source_ios = after_source_ios

            else:
                window_rect = self.driver.get_window_rect()
                current_scroll_position = window_rect["y"] + screen_height

                # Check if the bottom of the page has been reached
                if current_scroll_position >= screen_size["height"]:
                    break

    def is_element_visible(self, locator, timeout=2):
        try:
            self.find_by(locator, timeout=timeout)
            return True
        except:
            return False

    # def swipe_down(self):
    #     screen_size = self.driver.get_window_size()
    #     x = int(int(screen_size["width"]) * 0.5)
    #     y_start = int(int(screen_size["height"]) * 0.8)
    #     y_end = int(int(screen_size["height"]) * 0.2)
    #     touch_action = TouchAction(self.driver)
    #     touch_action.press(x=x, y=y_start).wait(500).move_to(
    #         x=x, y=y_end
    #     ).release().perform()
    
    def swipe_down(self):
        """
        Swipes down on the screen to scroll content.
        This method should work for both iOS and Android.
        """
        screen_size = self.driver.get_window_size()
        width = screen_size["width"]
        height = screen_size["height"]
        
        # Calculate swipe coordinates
        start_x = int(width * 0.5)  # Middle of screen
        start_y = int(height * 0.8)  # Near bottom
        end_x = int(width * 0.5)    # Middle of screen
        end_y = int(height * 0.2)   # Near top
        
        if self.current_platform.lower() == "android":
            try:
                # Android specific implementation
                touch_action = TouchAction(self.driver)
                touch_action.press(x=start_x, y=start_y) \
                        .wait(500) \
                        .move_to(x=end_x, y=end_y) \
                        .release() \
                        .perform()
            except Exception as e:
                # Alternative method for Android if TouchAction fails
                self.driver.swipe(start_x, start_y, end_x, end_y, 500)
        else:
            # iOS implementation - keep your existing approach
            touch_action = TouchAction(self.driver)
            touch_action.press(x=start_x, y=start_y) \
                    .wait(500) \
                    .move_to(x=end_x, y=end_y) \
                    .release() \
                    .perform()
        
        # Give the UI time to update after the swipe
        sleep(0.5)

    def scroll_to_top(self):
        # Get the initial page source
        if self.current_platform == "iOS":
            before_source_ios = self.driver.page_source

        # Scroll up the page until the top is reached
        while True:
            if self.current_platform == "iOS":
                self.driver.execute_script("mobile: scroll", {"direction": "up"})
                after_source_ios = self.driver.page_source
                # Parse the hierarchies using an XML parser
                before_root = ET.fromstring(before_source_ios.encode("utf-8"))
                after_root = ET.fromstring(after_source_ios.encode("utf-8"))

                before_first_element = self.get_first_ios_element_on_page(before_root)
                after_first_element = self.get_first_ios_element_on_page(after_root)

                # Compare the tag_name of the first iOS elements to determine if we have reached the top
                if before_first_element is not None and after_first_element is not None:
                    if before_first_element.tag == after_first_element.tag:
                        break

                # Update the page source for the next iteration
                before_source_ios = after_source_ios

            else:
                # Scroll for Android takes an accessibility id, however, it will scroll to the top
                # looking for that id and if it doesn't exist, it will throw an error.
                # If we give it a non-existent accessibility id, and catch the error and continue,
                # we should be at the top.
                try:
                    self.scroll_to_element(
                        "this element doesn't exist, it is here to make Android scroll to the top"
                    )
                except:
                    pass

                # Check if the top of the page has been reached
                window_rect = self.driver.get_window_rect()
                current_scroll_position = window_rect["y"]

                if current_scroll_position <= 0:
                    break

    def get_last_ios_element_on_page(self, root):
        # Helper function to get the last iOS element that is not XCUIElementTypeOther from an XML hierarchy
        last_ios_element = None
        for element in root.iter():
            if (
                self.current_platform == "iOS"
                and element.tag != "XCUIElementTypeOther"
                and element.tag != "XCUIElementTypeWindow"
            ):
                last_ios_element = element
        return last_ios_element

    def get_first_ios_element_on_page(self, root):
        # Helper function to get the first iOS element that is not XCUIElementTypeOther from an XML hierarchy
        first_ios_element = None
        for element in root.iter():
            if (
                self.current_platform == "iOS"
                and element.tag != "XCUIElementTypeOther"
                and element.tag != "XCUIElementTypeWindow"
            ):
                first_ios_element = element
                break  # Exit the loop after finding the first iOS element
        return first_ios_element
