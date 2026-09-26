from pages.login_page import LoginPage
import time


def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    time.sleep(10)

    assert "inventory" in driver.current_url


def test_invalid_password(driver):

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    error = login_page.get_error_message()

    assert "Username and password do not match" in error


def test_locked_out_user(driver):

    login_page = LoginPage(driver)

    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    error = login_page.get_error_message()

    assert "Sorry, this user has been locked out." in error