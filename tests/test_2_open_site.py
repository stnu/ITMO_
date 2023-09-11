from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_12():
    driver.get("https://demoqa.com/")

    try:
        driver.find_element(By.CSS_SELECTOR, "Header > a > img")
    except NoSuchElementException:
        assert False
    assert True
