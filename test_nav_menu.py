import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestNavigation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://www.selenium.dev")

    def test_navigation_links(self):

        navigation_links = {
            "Documentation": "https://www.selenium.dev/documentation/",
            "Projects": "https://www.selenium.dev/projects/",
            "Support": "https://www.selenium.dev/support/",
            "Blog": "https://www.selenium.dev/blog/"
        }

        for text_link, expected_url in navigation_links.items():
            with self.subTest(link=text_link):
                nav_link = self.driver.find_element(By.LINK_TEXT, text_link)
                nav_link.click()
                self.assertEqual(self.driver.current_url, expected_url, f"{text_link} URL is incorrect")
                self.driver.back()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

