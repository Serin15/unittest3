import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginFunctionality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        login_input = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        username_input.clear()
        password_input.clear()
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_input.click()

    def test_login(self):
        self.login("tomsmith", "SuperSecretPassword!")
        success_message = self.driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", success_message)


    def test_invalid_password(self):
        self.login("tomsmith", "wrongpass")
        invalid_message = self.driver.find_element(By.ID, "flash").text
        self.assertIn("Your password is invalid!", invalid_message)

    def test_empty_field(self):
        self.login(" ", " ")
        error_message = self.driver.find_element(By.ID, "flash").text
        self.assertIn("Your username is invalid!", error_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
