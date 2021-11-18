from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption (
        "--language", action = "store", default = "en", help = "Choose language: ru or zh-cn or fr or pt or es or ko"
    )




@pytest.fixture(scope="function")
def browser(request):
    languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb zh-cn ko"
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nStart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb".format(language))
        pytest.fail("Wrong Language")
        # assert 0
    yield browser
    print("\nQuit browser...")
    browser.quit()

# Альтернативный вариант
# @pytest.fixture(scope="function")
# def browser(request):
#     user_language = request.config.getoption('language')
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome(options=options)        
#     yield browser
#     print("\nquit browser..")
#     browser.quit()    