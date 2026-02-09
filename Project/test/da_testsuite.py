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

    def test_DA1_account_number_cannot_be_empty(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Locate the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Leave the field empty and press TAB
        account_number_field.click()
        account_number_field.send_keys("")  # Leave it empty
        account_number_field.send_keys(Keys.TAB)  # Press TAB
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2").text
        self.assertEqual(
            error_message,
            "Account Number must not be blank",
            "Error message for empty Account Number is incorrect."
        )

    def test_DA2_account_number_must_be_numeric(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Enter character values in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.clear()
        account_number_field.send_keys("Acc123")
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2").text
        self.assertEqual(
            error_message,
            "Characters are not allowed",
            "Error message for non-numeric Account Number is incorrect."
        )

    def test_DA3_account_number_cannot_have_special_characters(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Enter special characters in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.clear()
        account_number_field.send_keys("123!@#")
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2").text
        self.assertEqual(
            error_message,
            "Special characters are not allowed",
            "Error message for special characters in Account Number is incorrect."
        )

    def test_DA4_account_number_cannot_have_blank_space(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Enter value with blank space in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.clear()
        account_number_field.send_keys("123 12")
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2").text
        self.assertEqual(
            error_message,
            "Characters are not allowed",
            "Error message for Account Number with blank space is incorrect."
        )

    def test_DA5_first_character_cannot_be_space(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Enter value with first character as space in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.clear()
        account_number_field.send_keys(" 12345")
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2").text
        self.assertEqual(
            error_message,
            "First character cannot have space",
            "Error message for Account Number with leading space is incorrect."
        )

    def test_DA6_valid_account_number_deletion(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Enter a valid Account Number
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("141268")  # Valid account number
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  # Click Submit
        sleep(2)

        # Handle alert for confirmation
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Do you really want to delete this Account?",
            "Unexpected alert message for valid Account Number."
        )
        alert.accept()  # Press OK on alert
        sleep(2)

        # Verify success message
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Account deleted successfully')]")
        self.assertEqual(
            success_message.text,
            "Account deleted successfully",
            "The success message is not as expected for a valid Account Number."
        )

    def test_DA7_invalid_account_number_deletion(self):
        # Go to Delete Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
        sleep(1)

        # Enter an invalid Account Number
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("12345")  # Invalid account number
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  # Click Submit
        sleep(2)

        # Handle alert for confirmation
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Do you really want to delete this Account?",
            "Unexpected alert message for invalid Account Number."
        )
        alert.accept()  # Press OK on alert
        sleep(2)

        # Verify the error message after confirming deletion
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Account does not exist",
            "Unexpected alert message for invalid Account Number."
        )
        alert.accept()  # Press OK on alert
        sleep(2)

if __name__ == "__main__":
    unittest.main()
