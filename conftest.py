from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption (
        "--language", action = "store", default = "en", help = "Choose language: ru or zh-cn or fr or pt or es or ko"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)        
    yield browser
    print("\nquit browser..")
    browser.quit()