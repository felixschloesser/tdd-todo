import unittest
from selenium import webdriver


class NewVisitortest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_doto_list(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title)

        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")
