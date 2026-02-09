import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
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

    def test_EA1_account_number_cannot_be_empty(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Locate Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")

        # Leave Account Number field empty and press TAB
        account_number_field.click()
        account_number_field.send_keys(Keys.TAB)
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(error_message.text, "Account Number must not be blank",
                         "Error message for empty Account Number is incorrect.")

    def test_EA2_account_number_must_be_numeric(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Test with character values in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        invalid_inputs = ["1234Acc", "Acc123"]
        for input_value in invalid_inputs:
            account_number_field.clear()
            account_number_field.send_keys(input_value)
            sleep(1)
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
            self.assertEqual(error_message.text, "Characters are not allowed",
                             f"Error not shown for input: {input_value}")

    def test_EA3_account_number_cannot_have_special_characters(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Test with special characters in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        invalid_inputs = ["123!@#", "!@#"]
        for input_value in invalid_inputs:
            account_number_field.clear()
            account_number_field.send_keys(input_value)
            sleep(1)
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
            self.assertEqual(error_message.text, "Special characters are not allowed",
                             f"Error not shown for input: {input_value}")

    def test_EA4_account_number_cannot_have_blank_space(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Test with blank spaces in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.clear()
        account_number_field.send_keys("123 12")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(error_message.text, "Characters are not allowed",
                         "Error message for blank spaces in Account Number is incorrect.")

    def test_EA5_account_number_first_character_cannot_be_space(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Test with leading space in Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.clear()
        account_number_field.send_keys(" 123456")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(error_message.text, "First character cannot have space",
                         "Error message for leading space in Account Number is incorrect.")

    def test_EA6_submit_valid_account_number(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Enter valid Account Number and submit
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("141162")  # Valid Account Number
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  # Click Submit
        sleep(2)

        # Verify redirection to Edit Account Form
        header = self.driver.find_element(By.XPATH, "//p[@class='heading3']").text
        self.assertEqual(
            header,
            "Edit Account Entry Form",
            "Did not redirect to Edit Account Form after entering a valid Account Number."
        )

    def test_EA7_submit_invalid_account_number(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Enter invalid Account Number and submit
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("12345")  # Invalid Account Number
        self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]").click()  # Click Submit
        sleep(2)

        # Verify error message
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Account does not exist",
            "Incorrect error message for an invalid Account Number."
        )
        alert.accept()  # Close the alert

    def test_EA8_reset_button(self):
        # Go to Edit Account page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Account')]").click()
        sleep(1)

        # Enter values in the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        inputs = ["qwer", "123456"]
        for value in inputs:
            account_number_field.clear()
            account_number_field.send_keys(value)
            sleep(1)

            # Click the Reset Button
            self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[2]").click()
            sleep(1)

            # Verify if the field is reset
            self.assertEqual(
                account_number_field.get_attribute("value"),
                "",
                f"Account Number field was not reset after entering value: {value}"
            )

if __name__ == "__main__":
    unittest.main()
