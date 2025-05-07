import os
from datetime import datetime

import allure


def capture_screenshot(driver, test_name=None):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = f"{test_name}_{timestamp}" if test_name else f"screenshot_{timestamp}"
    screenshot_dir = os.path.join(os.getcwd(), "Test-artifacts", "Screenshots")
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    # -------------------------------
    # Capture and save the screenshot
    # -------------------------------
    screenshot = os.path.join(screenshot_dir, f"{name}.png")
    driver.save_screenshot(screenshot)
    print(f"Screenshot saved to: {screenshot}")
    # Attach screenshot to Allure report
    with open(screenshot, "rb") as file:
        allure.attach(
            file.read(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    # Return the Screeshot
    return screenshot
