# 🧪 Swag Labs Test Automation Project (Selenium + Python + Pytest)

This is a simple and beginner-friendly Selenium automation framework built using **Python**, **Pytest**, and **Selenium WebDriver** to test key features of the Swag Labs demo website: [https://www.saucedemo.com](https://www.saucedemo.com).

It is designed to help you practice and demonstrate essential QA automation skills using real-world tools and structure.

---

## 📌 Project Overview

This project automates some core user actions on the Swag Labs e-commerce site, such as:

- ✅ Logging in with valid credentials
- ✅ Verifying product list after login
- ✅ Adding products to the cart
- ✅ Validating cart contents
- ✅ Performing a checkout

The tests are written using **Pytest** and follow a basic structure to help with readability and maintainability.

---

## 💡 Key Concepts Covered

This project helps you practice the following automation skills:

| Skill                     | Covered? |
|--------------------------|----------|
| Selenium WebDriver usage | ✅ Yes    |
| Pytest framework         | ✅ Yes    |
| Page Object Model (POM)  | ✅ Yes    |
| Pytest Fixtures (`conftest.py`) | ✅ Yes |
| Assertions and waits     | ✅ Yes    |
| Screenshot on failure    | ✅ Yes    |
| HTML test reports        | ✅ Yes    |
| Clean code structure     | ✅ Yes    |

---

## 🧰 Tools & Technologies

- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **pytest-html** (for reports)
- **WebDriver Manager** (for automatic driver downloads)
- **Git + GitHub** (for version control)

---

## 🧪 How to Run This Project

### 1. Clone the Repository


git clone https://github.com/yourusername/selenium-python-swaglabs.git
cd selenium-python-swaglabs

### 2. Set Up a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

### 3. Install Required Packages

pip install -r requirements.txt

### 4. Run All Tests

pytest tests/

### 5. Run Tests with HTML Report

pytest tests/ --html=reports/test_report.html --self-contained-html
The report will be saved inside the reports/ folder.

### 🧪 Test File Structure

selenium-python-swaglabs/
│
├── tests/                 # Test cases written using Pytest
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── pages/                 # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
│
├── reports/               # HTML reports from pytest-html
├── screenshots/           # Failure screenshots
├── conftest.py            # Pytest fixtures (e.g., driver setup)
├── requirements.txt       # Dependencies
└── README.md              # This file

### 📸 Screenshots on Failure
If any test fails, a screenshot will automatically be saved inside the screenshots/ folder for easy debugging.

### 📈 Future Improvements
Add tests for logout and negative login cases
Store test data in JSON or Excel
Integrate with Jenkins or GitHub Actions for CI/CD
Add logs for better traceability
Dockerize the test setup

### 🙋‍♂️ Author
Fatima Zafar
SQA Engineer
📧 fatima.zafar15398@gmail.com
🔗 https://github.com/FatimaZafar153
🔗 https://www.linkedin.com/in/fatima-zafar-27b392176/