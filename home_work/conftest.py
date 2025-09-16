import pytest
from pygments.styles.dracula import yellow
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)

def browser_managment():
    browser.config.base_url='https://demoqa.com/automation-practice-form'
    browser.config.timeout = 2.0
    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless')
    browser.config.driver_options=driver_options

    yield

    browser.quit()