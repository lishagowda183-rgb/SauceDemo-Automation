from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    checkout_button = (
        By.ID,
        "checkout"
    )

    first_name = (
        By.ID,
        "first-name"
    )

    last_name = (
        By.ID,
        "last-name"
    )

    postal_code = (
        By.ID,
        "postal-code"
    )

    continue_button = (
        By.ID,
        "continue"
    )

    overview_title = (
        By.CLASS_NAME,
        "title"
    )

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

        self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

        self.wait.until(
            EC.visibility_of_element_located(self.postal_code)
        ).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def get_overview_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.overview_title)
        ).text