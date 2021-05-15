from selenium.webdriver.common.by import By
from .BasePage import BasePage


class CatalogPage(BasePage):
    PC_CONTAINER = (By.CSS_SELECTOR, ".container#product-category")
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb")
    GROUP_LIST = (By.CSS_SELECTOR, ".list-group")
    PRODUCT_THUMBNAILS = (By.CSS_SELECTOR, ".product-thumb")

    def get_product_category_container(self):
        return self.get_by_css_selector_with_waiting(self.PC_CONTAINER)

    def get_breadcrumb(self):
        return self.get_by_css_selector_with_waiting(self.BREADCRUMB)

    def get_group_list(self):
        return self.get_by_css_selector_with_waiting(self.GROUP_LIST)

    def get_all_product_thumbnails(self):
        return self.get_by_css_selector_with_waiting(self.PRODUCT_THUMBNAILS)
