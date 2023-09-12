from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_12():
    driver.get("https://www.saucedemo.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "#user-name")
        driver.find_element(By.CSS_SELECTOR, "#password")
        driver.find_element(By.CSS_SELECTOR, "#login-button")
    except NoSuchElementException:
        assert False
    print('Элементы найдены')
