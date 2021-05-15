from selenium.webdriver.common.by import By
from .BasePage import BasePage
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):
    LOGIN_CONTAINER = (By.CSS_SELECTOR, "#account-login")
    CUSTOMER_AREAS = ".col-sm-9 .col-sm-6"
    REGISTER = ".btn.btn-primary"
    EMAIL = "#input-email"
    PASSWORD = "#input-password"
    LOGIN = ".btn.btn-primary[value=Login]"

    def __init__(self, browser):
        self.browser = browser
        self.login_container = self.get_login_container()

    def get_login_container(self) -> WebElement:
        return self.get_by_css_selector_with_waiting(self.LOGIN_CONTAINER)

    def _get_areas(self):
        return self.login_container.find_elements_by_css_selector(self.CUSTOMER_AREAS)

    def get_new_customer_area(self):
        return self._get_areas()[0]

    def get_returning_customer_area(self):
        return self._get_areas()[1]

    def get_register_account_button(self):
        return self.get_new_customer_area().find_element_by_css_selector(self.REGISTER)

    def get_email_input(self):
        return self.get_returning_customer_area().find_element_by_css_selector(self.EMAIL)

    def get_password_input(self):
        return self.get_returning_customer_area().find_element_by_css_selector(self.PASSWORD)

    def get_login_button(self):
        return self.get_returning_customer_area().find_element_by_css_selector(self.LOGIN)
