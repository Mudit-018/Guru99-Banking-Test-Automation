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
        # Log in to the Guru99 application
        self.driver.get("https://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("YOUR_ID")
        self.driver.find_element(By.NAME, "password").send_keys("YOUR_PASSWORD")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

    def test_MS1_account_number_cannot_be_empty(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Leave the Account Number field empty and press TAB
        account_number_field.click()
        account_number_field.send_keys("")  # Leave it empty
        account_number_field.send_keys(Keys.TAB)  # Press TAB to trigger validation
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Account Number must not be blank",
            "The expected error message for an empty Account Number was not displayed."
        )

    def test_MS2_account_number_must_be_numeric(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter a non-numeric value in the Account Number field
        account_number_field.send_keys("Acc123")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "The expected error message for non-numeric Account Number was not displayed."
        )

    def test_MS3_account_number_cannot_have_special_characters(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter special characters in the Account Number field
        account_number_field.send_keys("123!@#")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Special characters are not allowed",
            "The expected error message for special characters in Account Number was not displayed."
        )

    def test_MS4_account_number_cannot_have_blank_space(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter a value with blank space in the Account Number field
        account_number_field.send_keys("123 12")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "The expected error message for blank spaces in Account Number was not displayed."
        )

    def test_MS5_account_number_cannot_have_leading_space(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter a value with leading space in the Account Number field
        account_number_field.send_keys(" 12345")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "First character cannot have space",
            "The expected error message for leading space in Account Number was not displayed."
        )
    def test_MS6_valid_account_number_submit(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter a valid Account Number
        account_number_field.send_keys("141268")  # Replace with your valid Account Number
        sleep(1)

        # Click the Submit button
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        sleep(2)

        # Verify the Mini Statement table is displayed
        table = self.driver.find_element(By.XPATH, "//table[contains(@class, 'layout')]")
        self.assertTrue(
            table.is_displayed(),
            "The table showing the Mini Statement should be displayed."
        )

    def test_MS7_invalid_account_number_submit(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter an invalid Account Number
        account_number_field.send_keys("12345")
        sleep(1)

        # Click the Submit button
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()
        sleep(1)

        # Verify the error message for invalid Account Number
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Account does not exist",
            "The expected error message for an invalid Account Number was not displayed."
        )
        alert.accept()  # Close the alert

    def test_MS8_reset_button_clears_account_number_field(self):
        # Go to the "Mini Statement" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Mini Statement')]").click()

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Enter some values into the Account Number field
        account_number_field.send_keys("qwer")
        sleep(1)

        # Click the Reset button
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]").click()
        sleep(1)

        # Verify the Account Number field is cleared
        self.assertEqual(
            account_number_field.get_attribute("value"),
            "",
            "The Account No field was not reset properly."
        )

    @classmethod
    def tearDownClass(cls):
        # Close the WebDriver
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
