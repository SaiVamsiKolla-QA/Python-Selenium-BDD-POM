# features/environment.py
from selenium import webdriver

# Import from project root
from utilities.generating_logs import generate_logs
from utilities.capture_screenshots import capture_screenshot

def before_all(context):
    # Set up the logger
    context.logger = generate_logs()
    context.logger.info("Starting test execution")


def before_scenario(context, scenario):
    # Log the start of scenario
    context.logger.info(f"Starting scenario: {scenario.name}")

    # Launch Chrome browser
    context.driver = webdriver.Chrome()

    # Maximize window and navigate to application
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")

    context.logger.info("Chrome browser launched and navigated to Swag Labs")


def after_scenario(context, scenario):
    # Log scenario completion
    if scenario.status == "passed":
        context.logger.info(f"Scenario passed: {scenario.name}")
    else:
        context.logger.error(f"Scenario failed: {scenario.name}")

    # Quit the browser
    context.driver.quit()
    context.logger.info("Browser closed")
