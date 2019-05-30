from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class ScreenshotMaker:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self):
        return self.driver.get_screenshot_as_png()


class SeleniumContainerException(Exception):
    pass


class SeleniumFacade:
    def __init__(self, driver):
        self.driver = driver

    def _find_deeper_element(self, parent_element, single_selector):
        try:
            result = self.is_xpath(single_selector)
            if result:
                return parent_element.find_element_by_xpath(single_selector)
            else:
                return parent_element.find_element_by_css_selector(single_selector)
        except Exception as ex:
            raise SeleniumContainerException("Timeout waiting for element", single_selector)

    def clear_input(self, selector):
        element = self.get_element(selector)
        element.clear()

    def click_button(self, selector):
        element = self.get_element(selector)
        if not (element.is_enabled()):
            print("Element is disabled: ", selector)
        element.click()

    def click_button_if_visible(self, selector):
        self.element_wait_to_be_visible(selector)
        element = self.get_element(selector)
        if not (element.is_enabled()):
            print("Element is disabled: ", selector)
        element.click()

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def drag_and_drop(self, selector_element, selector_target):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(self.get_element(selector_element), self.get_element(selector_target)).perform()

    def drag_and_drop_by_offset(self, selector, xoffset, yoffset):
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop_by_offset(self.get_element(selector), xoffset, yoffset).perform()

    def element_wait(self, selector, value=30):
        try:
            wait = WebDriverWait(self.driver, value)
            result = self.is_xpath(selector)
            if result:
                wait.until(EC.presence_of_element_located((By.XPATH, selector)))
            else:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        except Exception as ex:
            raise SeleniumContainerException("Timeout waiting for element", selector)

    def element_wait_to_be_clickable(self, selector, value=30):
        try:
            wait = WebDriverWait(self.driver, value)
            result = self.is_xpath(selector)
            if result:
                wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
            else:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        except Exception as ex:
            raise SeleniumContainerException("Timeout waiting for element or element is disabled", selector)

    def element_wait_to_be_visible(self, selector, value=10):
        try:
            wait = WebDriverWait(self.driver, value)
            result = self.is_xpath(selector)
            if result:
                wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
            else:
                wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        except Exception as ex:
            raise SeleniumContainerException("Timeout waiting for element", selector)

    def element_wait_until_not(self, selector, value=30):
        try:
            wait = WebDriverWait(self.driver, value)
            result = self.is_xpath(selector)
            if result:
                wait.until(EC.invisibility_of_element_located((By.XPATH, selector)))
                return True
            else:
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, selector)))
        except Exception as ex:
            return False

    def explicit_wait(self, value):
        time.sleep(value)

    def get_button_state(self, selector):
        element = self.get_element(selector)
        return element.is_enabled()

    def get_checkbox_state(self, selector):
        element = self.get_element(selector)
        return element.is_selected()

    def get_element(self, selector):
        return self._find_deeper_element(self.driver, selector)

    def get_name(self, selector):
        element = self.get_element(selector)
        return element.get_attribute("name")

    def get_page_by_url(self, url):
        self.driver.get(url)

    def get_placehldr(self, selector):
        element = self.get_element(selector)
        return element.get_attribute("placeholder")

    def get_text(self, selector):
        element = self.get_element(selector)
        return element.text

    def get_text_strip(self, selector):
        element = self.get_element(selector)
        return element.text.strip()

    def get_value(self, selector):
        element = self.get_element(selector)
        return element.get_attribute("value")

    def is_element_present(self, selector):
        try:
            result = self.is_xpath(selector)
            if result:
                return self.driver.find_element_by_xpath(selector).is_displayed()
            else:
                return self.driver.find_element_by_css_selector(selector).is_displayed()
        except Exception as ex:
            return False

    def is_xpath(self, selector):
        if (selector[0] == '/') or (selector[0] == '*'):
            return True

    def move_to_element(self, selectorElement):
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.get_element(selectorElement)).perform()

    def refresh_page(self):
        self.driver.refresh()

    def set_checkbox(self, selector, value):
        element = self.get_element(selector)
        if not (element.is_enabled()):
            print("Element is disabled: ", selector)
        if element.is_selected() and not value:
            element.click()
        elif not (element.is_selected()) and value:
            element.click()

    def set_to_input(self, selector, value):
        element = self.get_element(selector)
        element.send_keys(value)

    def stop_driver(self):
        self.driver.close()

    def to_relative_url(self, url, relative_url):
        self.driver.get(url + relative_url)
