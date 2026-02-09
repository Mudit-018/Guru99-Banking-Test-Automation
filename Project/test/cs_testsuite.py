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

    def test_CS1_account_number_cannot_be_empty(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Find the Account Number field and leave it empty
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.click()
        account_number_field.send_keys("")  # Leave it empty
        account_number_field.send_keys(Keys.TAB)  # Simulate pressing TAB
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Account Number must not be blank",
            "Error message for empty Account Number is incorrect."
        )

    def test_CS2_account_number_must_be_numeric(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter non-numeric characters in the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("Acc123")
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for non-numeric Account Number is incorrect."
        )

    def test_CS3_account_number_cannot_have_special_characters(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter special characters in the Account Number field
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("123!@#")
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Special characters are not allowed",
            "Error message for special characters in Account Number is incorrect."
        )

    def test_CS4_account_number_cannot_have_blank_space(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter an account number with a blank space
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("123 12")
        account_number_field.send_keys(Keys.TAB)  # Simulate pressing TAB
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for account number with blank space is incorrect."
        )

    def test_CS5_first_character_cannot_be_space(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter an account number starting with a blank space
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys(" 12345")
        account_number_field.send_keys(Keys.TAB)  # Simulate pressing TAB
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message2")
        self.assertEqual(
            error_message.text,
            "First character cannot have space",
            "Error message for account number starting with a space is incorrect."
        )

    def test_CS6_verify_from_date_field(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Click on the From Date field without selecting anything from the calendar
        from_date_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]")
        from_date_field.click()  # Click on the From Date field
        from_date_field.send_keys(Keys.TAB)  # Simulate pressing TAB to leave the field empty
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message26")
        self.assertEqual(
            error_message.text,
            "From Date Field must not be blank",
            "Error message for blank From Date field is incorrect."
        )

    def test_CS7_verify_to_date_field(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Click on the To Date field without selecting anything from the calendar
        to_date_field = self.driver.find_element(By.XPATH,
                                                 "//tbody/tr[8]/td[2]/input[1]")  # Adjust the XPath for "To Date" field
        to_date_field.click()  # Click on the To Date field
        to_date_field.send_keys(Keys.TAB)  # Simulate pressing TAB to leave the field empty
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message27")  # Adjust the CSS selector if necessary
        self.assertEqual(
            error_message.text,
            "To Date Field must not be blank",
            "Error message for blank To Date field is incorrect."
        )

    def test_CS8_verify_minimum_transaction_value_must_be_numeric(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter an invalid numeric value in the Minimum Transaction Value field
        min_transaction_value_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        min_transaction_value_field.send_keys("Acc123")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message12")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for non-numeric Minimum Transaction Value is incorrect."
        )

    def test_CS9_minimum_transaction_value_cannot_have_special_characters(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter special characters in the Minimum Transaction Value field
        min_transaction_value_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        min_transaction_value_field.send_keys("123!@#")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message12")
        self.assertEqual(
            error_message.text,
            "Special characters are not allowed",
            "Error message for special characters in Minimum Transaction Value is incorrect."
        )

    def test_CS10_minimum_transaction_value_cannot_have_blank_space(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter value with blank space in the Minimum Transaction Value field
        min_transaction_value_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        min_transaction_value_field.send_keys("123 12")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message12")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for blank spaces in Minimum Transaction Value is incorrect."
        )

    def test_CS11_first_character_cannot_be_space_in_minimum_transaction_value(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter value with a leading space in the Minimum Transaction Value field
        min_transaction_value_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        min_transaction_value_field.send_keys(" 123456")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message12")
        self.assertEqual(
            error_message.text,
            "First character cannot have space",
            "Error message for leading space in Minimum Transaction Value is incorrect."
        )

    def test_CS12_verify_number_of_transaction_must_be_numeric(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter invalid numeric value in the Number of Transaction field
        number_of_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        number_of_transaction_field.send_keys("Acc123")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message13")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for non-numeric Number of Transaction is incorrect."
        )

    def test_CS13_number_of_transaction_cannot_have_special_characters(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter special characters in the Number of Transaction field
        number_of_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        number_of_transaction_field.send_keys("123!@#")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message13")
        self.assertEqual(
            error_message.text,
            "Special characters are not allowed",
            "Error message for special characters in Number of Transaction is incorrect."
        )

    def test_CS14_number_of_transaction_cannot_have_blank_space(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter value with blank space in the Number of Transaction field
        number_of_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        number_of_transaction_field.send_keys("123 12")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message13")
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for blank spaces in Number of Transaction is incorrect."
        )

    def test_CS15_first_character_cannot_be_space_in_number_of_transaction(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Enter value with a leading space in the Number of Transaction field
        number_of_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        number_of_transaction_field.send_keys(" 123456")  # Invalid value
        sleep(1)

        # Verify the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message13")
        self.assertEqual(
            error_message.text,
            "First character cannot have space",
            "Error message for leading space in Number of Transaction is incorrect."
        )

    def test_CS16_reset_button_resets_all_fields(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Locate all the fields in the form and fill them with sample data
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("123456")

        from_date_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]")
        from_date_field.send_keys("01/01/2024")

        to_date_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        to_date_field.send_keys("01/15/2024")

        minimum_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        minimum_transaction_field.send_keys("100")

        number_of_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        number_of_transaction_field.send_keys("10")

        # Click the Reset Button
        reset_button = self.driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[2]")
        reset_button.click()
        sleep(1)

        # Verify that all fields are reset
        self.assertEqual(account_number_field.get_attribute("value"), "", "Account Number field is not reset.")
        self.assertEqual(from_date_field.get_attribute("value"), "", "From Date field is not reset.")
        self.assertEqual(to_date_field.get_attribute("value"), "", "To Date field is not reset.")
        self.assertEqual(minimum_transaction_field.get_attribute("value"), "",
                         "Minimum Transaction Value field is not reset.")
        self.assertEqual(number_of_transaction_field.get_attribute("value"), "",
                         "Number of Transactions field is not reset.")

    def test_CS17_submit_button_with_blank_to_date_alert(self):
        # Navigate to the Customised Statement page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Customised Statement')]").click()
        sleep(1)

        # Fill the Account Number field with a valid number
        account_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        account_number_field.send_keys("141268")

        # Fill the From Date field with a valid date
        from_date_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]")
        from_date_field.send_keys("2023-01-01")

        # Leave the To Date field blank
        to_date_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        to_date_field.clear()

        # Fill the Minimum Transaction Value field with a valid value
        minimum_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        minimum_transaction_field.send_keys("100")

        # Fill the Number of Transactions field with a valid value
        number_of_transaction_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        number_of_transaction_field.send_keys("5")

        # Click the Submit button
        submit_button = self.driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[1]")
        submit_button.click()
        sleep(1)

        # Handle the alert
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Please fill all fields", "Alert message for blank To Date field is incorrect.")
        alert.accept()  # Close the alert

if __name__ == "__main__":
    unittest.main()
