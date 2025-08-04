from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_google_search():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://www.google.com")
        box = driver.find_element(By.NAME, "q")
        box.send_keys("Selenium Python")
        box.submit()
        assert "Selenium" in driver.title
    finally:
        driver.quit()
