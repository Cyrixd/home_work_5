from selenium.webdriver.common.by import By
from .BasePage import BasePage



class ProductPage(BasePage):
    PP_CONTAINER = (By.CSS_SELECTOR, "#product-product")
    PRODUCT_THUMBNAILS = (By.CSS_SELECTOR, ".thumbnails .thumbnail")
    TAB_CONTENT = (By.CSS_SELECTOR, ".tab-content")
    RATING = (By.CSS_SELECTOR, ".rating")
    ADD_TO_CART = (By.CSS_SELECTOR, "#button-cart")

    def _get_product_container(self):
        return self.get_by_css_selector_with_waiting(self.PP_CONTAINER)

    def get_all_product_thumbnails(self):
        return self.get_by_css_selector_with_waiting(self.PRODUCT_THUMBNAILS)

    def get_content_tab(self):
        return self.get_by_css_selector_with_waiting(self.TAB_CONTENT)

    def get_rating_area(self):
        return self.get_by_css_selector_with_waiting(self.RATING)

    def get_add_to_cart_button(self):
        return self.get_by_css_selector_with_waiting(self.ADD_TO_CART)




