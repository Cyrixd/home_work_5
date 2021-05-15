import os
import pytest
from selenium import webdriver

DRIVERS_PATH = os.path.expanduser("~/Webdrivers/")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--base_url", action="store", default="http://192.168.1.48")


def driver_maker(browser):
    common_caps = {"pageLoadStrategy": "eager"}

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS_PATH}/chromedriver",
                                  desired_capabilities=common_caps)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS_PATH}/geckodriver",
                                   desired_capabilities=common_caps)
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS_PATH}/operadriver",
                                 desired_capabilities=common_caps)
    else:
        raise Exception(f"There is no webdriver for: {browser}")
    return driver


@pytest.fixture
def browser(request):
    driver = driver_maker(request.config.getoption("--browser"))
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


