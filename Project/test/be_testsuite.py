import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Guru99Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up the WebDriver
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("YOUR_ID")
        self.driver.find_element(By.NAME, "password").send_keys("YOUR_PASSWORD")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

    def test_BE1_account_number_cannot_be_empty(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Leave the Account Number field empty and press TAB
        account_number_field.click()
        account_number_field.send_keys("")  # Leave empty
        account_number_field.send_keys(Keys.TAB)
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Account Number must not be blank",
            "The error message for an empty Account Number was not displayed correctly."
        )

    def test_BE2_account_number_must_be_numeric(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter non-numeric values
        account_number_field.send_keys("1234Acc")
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "The error message for non-numeric input was not displayed correctly."
        )

    def test_BE3_account_number_cannot_have_special_characters(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter special characters
        account_number_field.send_keys("123!@#")
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Special characters are not allowed",
            "The error message for special characters was not displayed correctly."
        )

    def test_BE4_first_character_cannot_be_space(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter an Account Number with a leading space
        account_number_field.send_keys(" 123456")
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "First character cannot have space",
            "The error message for a leading space was not displayed correctly."
        )

    def test_BE5_valid_account_number(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter a valid account number
        account_number_field.send_keys("141268")  # Replace with your valid Account Number
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  # Click Submit
        sleep(2)

        # Verify that the balance table is displayed
        balance_table = self.driver.find_element(By.XPATH, "//table[contains(@id, 'balanceTable')]")  # Adjust if needed
        self.assertTrue(balance_table.is_displayed(), "The balance table was not displayed for a valid account number.")

    def test_BE6_invalid_account_number(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter an invalid account number
        account_number_field.send_keys("12345")  # Example of an invalid Account Number
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  # Click Submit
        sleep(2)

        # Handle alert
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        self.assertIn("Account does not exist", alert_text,
                      "The error message was not displayed correctly for an invalid account number.")
        alert.accept()  # Close the alert

    def test_BE7_reset_button(self):
        # Navigate to the "Balance Enquiry" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Balance Enquiry')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter values into the Account Number field
        account_number_field.send_keys("qwer")
        sleep(1)

        # Click the Reset button
        reset_button = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]")
        reset_button.click()
        sleep(1)

        # Verify that the field is reset
        self.assertEqual(
            account_number_field.get_attribute("value"),
            "",
            "The Account Number field was not reset."
        )

if __name__ == "__main__":
    unittest.main()
