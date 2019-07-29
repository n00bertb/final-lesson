import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):

    parser.addoption("--language", action="store", default="en",help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    #опция ниже запускает браузер с нужной локалью
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    #без этих опшенсов ниже не запускается браузер в debian9 в windows можно их не включать
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    ###
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()