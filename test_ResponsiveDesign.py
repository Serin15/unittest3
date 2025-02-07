import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestResponsiveDesign(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

    def test_ResponsiveDesign(self):
        self.driver.get("https://www.selenium.dev/")

        screen_size = [
            (1920, 1080, "navbar"),   # desktop
            (768, 1024, "navbar"),   # tablet
         ]

        for width, height, menu_selector in screen_size:
            self.driver.set_window_size(width, height)


            menu = WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, menu_selector))
            )
            self.assertTrue(menu.is_displayed())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
