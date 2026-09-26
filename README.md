# SauceDemo Selenium Automation

A Selenium + PyTest automation framework for testing the SauceDemo web application.

The project demonstrates UI automation using the Page Object Model (POM), explicit waits, reusable WebDriver fixtures, positive and negative test scenarios, failure screenshots, and HTML test reporting.

## 🚀 Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Explicit Waits
- PyTest HTML Reports
- Git & GitHub

## 🧪 Automated Test Scenarios

The project currently includes 5 automated test scenarios:

### 1. Valid Login

- Logs in using a valid standard user.
- Verifies successful navigation to the inventory page.

### 2. Invalid Password

- Uses a valid username with an incorrect password.
- Verifies the login error message.

### 3. Locked-Out User

- Attempts to log in using a locked-out user.
- Verifies that the user is prevented from logging in.

### 4. Add Product to Cart

- Logs in as a standard user.
- Adds the Sauce Labs Backpack to the cart.
- Navigates to the cart.
- Verifies the product name.

### 5. Checkout Flow

- Logs in as a standard user.
- Adds a product to the cart.
- Opens the cart and starts checkout.
- Enters customer information.
- Verifies the Checkout Overview page.

## 📁 Project Structure

```text
SauceDemo-Automation/
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   └── test_login.py
│
├── screenshots/
├── reports/
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Setup

Clone the repository:

git clone https://github.com/lishagowda183-rgb/SauceDemo-Automation.git

Navigate to the project:

cd SauceDemo-Automation

Install the dependencies:

pip install -r requirements.txt
▶️ Run Tests

Run all tests:

pytest

Generate an HTML test report:

pytest --html=reports/report.html --self-contained-html
🏗️ Framework Design

The project follows the Page Object Model (POM).

login_page.py handles login elements and actions.
inventory_page.py handles product and cart interactions.
cart_page.py handles cart validation.
checkout_page.py handles checkout actions and validation.
test_login.py contains the automated test scenarios.
conftest.py manages the Selenium WebDriver fixture.
Explicit waits are used for reliable element interaction.
Assertions are used to validate expected application behavior.
📸 Failure Screenshots

The framework automatically captures a screenshot when a test fails.

Screenshots are stored in:

screenshots/

The screenshots directory is excluded from Git using .gitignore.

📊 Test Coverage

Current automation covers:

Positive login testing
Invalid credentials
Locked-out user validation
Product selection
Cart validation
Checkout flow
Checkout overview validation
Failure screenshot capture
HTML test reporting
🔮 Future Improvements
Add checkout completion validation
Expand product and cart test coverage
Add more negative checkout scenarios
Add CI/CD using GitHub Actions
Expand automated reporting
👩‍💻 Author

Lisha Gowda

GitHub: https://github.com/lishagowda183-rgb