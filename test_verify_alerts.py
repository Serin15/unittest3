import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlertsJava(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)


    def test_js_alert(self):
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']").click()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "I am a JS Alert")
        alert.accept()

    def test_js_confirm(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']").click()
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "I am a JS Confirm")
        alert.accept()

    def test_js_prompt(self):
        self.driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
        alert = self.driver.switch_to.alert
        alert.send_keys("hello")
        alert.accept()

        result_text = self.driver.find_element(By.ID, "result").text

        self.assertIn("hello", result_text)

    @classmethod
    def tearDownClass(cls):
            cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
