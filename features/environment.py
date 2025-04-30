# features/environment.py
from selenium import webdriver

# Import from project root
from utilities import config_reader


def before_scenario(context, scenario):
    browser_name = config_reader.read_configuration("basic info", "browser")

    if browser_name.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name.lower() == "edge":
        context.driver = webdriver.Edge()
    else:
        # Default to Chrome if unknown browser specified
        context.driver = webdriver.Chrome()

    context.driver.maximize_window()
    context.driver.get(config_reader.read_configuration("basic info", "url"))


def after_scenario(context, scenario):
        context.driver.quit()