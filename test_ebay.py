import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class SearchWithFilters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()


    def test_search_with_filters(self):
        driver = self.driver
        driver.get("https://www.ebay.com/")

        search_button = driver.find_element(By.ID, "gh-ac")
        search_button.send_keys("laptop")
        search_button.send_keys(Keys.RETURN)

        items = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".s-item"))
        )

        try:
            category_filter = WebDriverWait(driver,5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Laptops & Netbooks']"))
            )
            category_filter.click()
        except:
            print("Cannot find the filter")

        min_price = driver.find_element(By.XPATH, "//input[@aria-label='Minimum Value in $']")
        max_price = driver.find_element(By.XPATH, "//input[@aria-label='Maximum Value in $']")
        button_click = driver.find_element(By.XPATH, "//button[@aria-label='Submit price range']")

        min_price.send_keys("200")
        max_price.send_keys("1000")
        button_click.click()

        items = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".s-item"))
        )

        items = driver.find_elements(By.CSS_SELECTOR, ".s-item")
        self.assertGreater(len(items),0, "no products were found after applying the filters")


        for item in items:
            try:
                price_element = item.find_element(By.CSS_SELECTOR, ".s-item__price")
                price_text = price_element.text.strip()

                if not price_text:
                    print("⚠️ Warning: the price is empty, jump this product!")
                    continue

                price_numbers = re.findall(r'\d+\.\d+|\d+', price_text)

                if price_numbers:
                    price = float(price_numbers[0])
                    print(f"✔ Extra price: {price}")
                    self.assertTrue(200 <= price <= 1000, f"Product priced out of range: {price}")
                else:
                    print(f"⚠️ A valid price could not be extracted: {price_text}")
            except Exception as e:
                print(f"❌ Price verification error: {e}")

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()
