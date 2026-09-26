import os
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    yield driver

    # Take screenshot if the test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_name = request.node.name + ".png"
        screenshot_path = os.path.join("screenshots", screenshot_name)

        driver.save_screenshot(screenshot_path)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)