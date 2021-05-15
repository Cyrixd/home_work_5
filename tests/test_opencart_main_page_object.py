from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.MainPage import MainPage
from page_objects.CatalogPage import CatalogPage
from page_objects.ProductPage import ProductPage
from page_objects.LoginPage import LoginPage


def test_main_page_title(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url"))
    main_page = MainPage(browser)
    assert main_page.get_title() == "Your Store"


def test_main_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url"))
    main_page = MainPage(browser)
    main_page.get_logo()
    main_page.get_search_input_h()
    main_page.get_search_button_h()
    main_page.get_swiper()


def test_catalog_desktops(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/index.php?route=product/category&path=20")
    desktops = CatalogPage(browser)

    desktops.get_product_category_container()
    desktops.get_breadcrumb()
    desktops.get_group_list()
    desktops.get_all_product_thumbnails()
    desktops.get_footer()


def test_product_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/index.php?route=product/product&path=57&product_id=49")
    product_page = ProductPage(browser)
    product_page._get_product_container()
    product_page.get_all_product_thumbnails()
    product_page.get_rating_area()
    product_page.get_add_to_cart_button()


def test_customer_login_page(browser, pytestconfig):
    browser.get(pytestconfig.getoption("base_url") + "/index.php?route=account/login")
    login_page = LoginPage(browser)

    login_page.get_new_customer_area()
    login_page.get_returning_customer_area()
    login_page.get_register_account_button()
    login_page.get_email_input()
    login_page.get_password_input()
    login_page.get_login_button()
