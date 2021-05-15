from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement



class BasePage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    HEADER_SG = (By.CSS_SELECTOR, ".input-group:first-child")
    FOOTER = (By.CSS_SELECTOR, "footer")

    def __init__(self, browser):
        self.browser = browser

    def get_by_css_selector_with_waiting(self, css_selector, timeout=2, poll_frequency=0.5) -> WebElement:
        wait = WebDriverWait(self.browser, timeout=timeout, poll_frequency=poll_frequency)
        return wait.until(EC.visibility_of_element_located(css_selector))

    def get_title(self):
        return self.browser.title

    def get_logo(self):
        return self.get_by_css_selector_with_waiting(self.LOGO)

    def _get_search_group_header(self):
        return self.get_by_css_selector_with_waiting(self.HEADER_SG)

    def get_search_input_h(self):
        return self._get_search_group_header().find_element_by_css_selector("[type=text]")

    def get_search_button_h(self):
        return self._get_search_group_header().find_element_by_css_selector("[type=button]")

    def get_footer(self):
        return self.get_by_css_selector_with_waiting(self.FOOTER)

