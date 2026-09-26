# SauceDemo Selenium Automation

A Selenium + PyTest automation framework for testing the login functionality of the SauceDemo web application.

## 🚀 Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- Explicit Waits
- PyTest HTML Reports
- Git & GitHub

## 🧪 Test Scenarios

The project currently covers three login scenarios:

### 1. Valid Login

- Username: `standard_user`
- Password: `secret_sauce`
- Verifies successful navigation to the inventory page.

### 2. Invalid Password

- Uses a valid username with an incorrect password.
- Verifies the appropriate login error message.

### 3. Locked-Out User

- Uses the SauceDemo locked-out account.
- Verifies that the user is prevented from logging in.

## 📁 Project Structure

```text
SauceDemo-Automation/
│
├── pages/
│   ├── __init__.py
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/lishagowda183-rgb/SauceDemo-Automation.git
```

Navigate to the project:

```bash
cd SauceDemo-Automation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Tests

Run all tests:

```bash
pytest
```

Generate an HTML test report:

```bash
pytest --html=reports/report.html --self-contained-html
```

## 🏗️ Framework Design

The project follows the Page Object Model (POM).

- `pages/login_page.py` contains page elements and login actions.
- `tests/test_login.py` contains the automated test cases.
- `conftest.py` manages the Selenium WebDriver fixture.
- Explicit waits are used for reliable element interaction.
- PyTest is used for test execution and assertions.

## 📊 Test Coverage

The current automation covers:

- Positive login testing
- Invalid credentials
- Locked-out user validation
- Login error message validation
- Successful page navigation

## 🔮 Future Improvements

- Add inventory page automation
- Add shopping cart test cases
- Add checkout flow automation
- Add failure screenshots
- Add CI/CD using GitHub Actions
- Expand test coverage

## 👩‍💻 Author

Lisha Gowda

GitHub: https://github.com/lishagowda183-rgb
