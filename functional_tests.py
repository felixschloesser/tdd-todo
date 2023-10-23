from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import unittest


class NewVisitortest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element(By.ID, "item_list")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_doto_list(self):
        # Edith has heard about a cool new online to-do app.
        # She decides to check out its home page
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "new_item")
        self.assertEqual(
            inputbox.get_attribute("placeholder"), "What do you want to do?"
        )

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do lists
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_table("1: Buy peacock feathers")

        # The is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        inputbox = self.browser.find_element(By.ID, "new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shwos both items on her list
        self.check_for_row_in_table("1: Buy peacock feathers")
        self.check_for_row_in_table("2: Use peacock feathers to make a fly")

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main(warnings="ignore")
