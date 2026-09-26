from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    backpack_add_button = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    cart_link = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    cart_badge = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    def add_backpack_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.backpack_add_button)
        ).click()

    def click_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.cart_badge)
        ).text