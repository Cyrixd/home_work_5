from selenium.webdriver.common.by import By
from .BasePage import BasePage


class MainPage(BasePage):
    SWIPER = (By.CSS_SELECTOR, ".swiper-viewport:first-child")

    def get_swiper(self):
        self.get_by_css_selector_with_waiting(self.SWIPER)
