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

    def test_NA1_customer_id_cannot_be_empty(self):
        # Navigate to the "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Leave it empty and press TAB
        customer_id_field.click()
        customer_id_field.send_keys("")
        customer_id_field.send_keys(Keys.TAB)
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")  # Adjust CSS selector if needed
        self.assertEqual(
            error_message.text,
            "Customer ID is required",
            "Error message for empty Customer ID is incorrect."
        )

    def test_NA2_customer_id_must_be_numeric(self):
        # Navigate to the "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter alphanumeric value
        customer_id_field.send_keys("Acc123")
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")  # Adjust CSS selector if needed
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for non-numeric Customer ID is incorrect."
        )
        customer_id_field.clear()
        # Enter alphanumeric value
        customer_id_field.send_keys("123Acc")
        sleep(1)

        # Verify error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")  # Adjust CSS selector if needed
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "Error message for non-numeric Customer ID is incorrect."
        )

    def test_NA3_customer_id_cannot_have_special_characters(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Customer ID field and enter special characters
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
        special_characters = ["123!@#", "!@#"]
        for special_char in special_characters:
            customer_id_field.clear()
            customer_id_field.send_keys(special_char)
            customer_id_field.send_keys(Keys.TAB)
            sleep(1)
            # Locate and validate the error message
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")
            self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_NA4_customer_id_cannot_have_blank_space(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Customer ID field and enter values with blank spaces
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
        customer_id_field.clear()
        customer_id_field.send_keys("123 12")
        customer_id_field.send_keys(Keys.TAB)
        sleep(1)
        # Locate and validate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_NA5_customer_id_first_character_cannot_be_space(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Customer ID field and enter a value with leading space
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
        customer_id_field.clear()
        customer_id_field.send_keys(" 12345")
        customer_id_field.send_keys(Keys.TAB)
        sleep(1)
        # Locate and validate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NA6_initial_deposit_cannot_be_empty(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Initial Deposit field and leave it empty
        deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")
        deposit_field.click()
        deposit_field.send_keys("")
        deposit_field.send_keys(Keys.TAB)
        sleep(1)

        # Locate and validate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message19")
        self.assertEqual(error_message.text, "Initial Deposit must not be blank")

    def test_NA7_initial_deposit_must_be_numeric(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Test with two non-numeric inputs
        deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")
        non_numeric_inputs = ["1234Acc", "Acc123"]
        for value in non_numeric_inputs:
            deposit_field.clear()
            deposit_field.send_keys(value)
            deposit_field.send_keys(Keys.TAB)
            sleep(1)
            # Locate and validate the error message
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message19")
            self.assertEqual(error_message.text, "Characters are not allowed")

    def test_NA8_initial_deposit_cannot_have_special_characters(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Test with two inputs containing special characters
        deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")
        special_character_inputs = ["123!@#", "!@#"]
        for value in special_character_inputs:
            deposit_field.clear()
            deposit_field.send_keys(value)
            deposit_field.send_keys(Keys.TAB)
            sleep(1)
            # Locate and validate the error message
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message19")
            self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_NA9_initial_deposit_cannot_have_blank_space(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Test with input containing blank spaces
        deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")
        deposit_field.clear()
        deposit_field.send_keys("123 12")
        deposit_field.send_keys(Keys.TAB)
        sleep(1)

        # Locate and validate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message19")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_NA10_initial_deposit_first_character_cannot_be_space(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Test with input starting with a blank space
        deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")
        deposit_field.clear()
        deposit_field.send_keys(" 12345")
        deposit_field.send_keys(Keys.TAB)
        sleep(1)

        # Locate and validate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message19")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NA11_verify_account_type_savings(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Account Type dropdown
        account_type_dropdown = self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/select[1]")

        # Select "Savings" account type
        select = Select(account_type_dropdown)
        select.select_by_visible_text("Savings")
        sleep(1)

        # Verify that "Savings" is selected
        selected_option = select.first_selected_option.text
        self.assertEqual(selected_option, "Savings", "Savings - should be selected")

    def test_NA12_verify_account_type_current(self):
        # Go to "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()

        # Locate the Account Type dropdown
        account_type_dropdown = self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[2]/select[1]")

        # Select "Current" account type
        select = Select(account_type_dropdown)
        select.select_by_visible_text("Current")
        sleep(1)

        # Verify that "Current" is selected
        selected_option = select.first_selected_option.text
        self.assertEqual(selected_option, "Current", "Current - should be selected")

    def test_NA13_reset_button_resets_fields(self):
            # Navigate to the "New Account" page
            self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()
            sleep(2)  # Allow time for the page to load

            # Locate the Customer ID and Initial Deposit fields
            customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
            initial_deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")

            # Enter values into the fields
            customer_id_field.send_keys("qwer")
            initial_deposit_field.send_keys("123456")

            # Click the Reset Button
            reset_button = self.driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[2]")
            reset_button.click()
            sleep(1)

            # Verify that the fields are reset
            self.assertEqual(customer_id_field.get_attribute("value"), "", "Customer ID field was not reset")
            self.assertEqual(initial_deposit_field.get_attribute("value"), "", "Initial Deposit field was not reset")

    def test_NA14_submit_button_with_incorrect_customer_id(self):
        # Navigate to the "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()
        sleep(2)  # Allow page to load

        # Locate the Customer ID and Initial Deposit fields
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
        initial_deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")

        # Enter incorrect Customer ID and a valid initial deposit
        customer_id_field.send_keys("123456")  # Incorrect Customer ID
        initial_deposit_field.send_keys("5000")  # Valid amount

        # Click the Submit button
        self.driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[1]").click()
        sleep(2)

        # Verify the error message
        error_message = self.driver.switch_to.alert.text
        self.assertEqual(error_message, "Customer does not exist!!",
                         "Expected error message not shown for incorrect Customer ID")
        self.driver.switch_to.alert.accept()  # Close the alert

    def test_NA15_submit_button_with_correct_customer_id_and_amount(self):
        # Navigate to the "New Account" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()
        sleep(2)  # Allow page to load

        # Locate the Customer ID and Initial Deposit fields
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
        initial_deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")

        # Enter correct Customer ID and valid initial deposit
        customer_id_field.send_keys("98560")  # Correct Customer ID
        initial_deposit_field.send_keys("5000")  # Valid amount

        # Click the Submit button
        self.driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[1]").click()
        sleep(2)

        # Verify the success message
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Account Generated Successfully')]")
        self.assertEqual(success_message.text, "Account Generated Successfully!!!",
                         "Expected success message not displayed")
    def test_NA16_continue_hyperlink_after_account_creation(self):
     # Navigate to the "New Account" page
     self.driver.find_element(By.XPATH, "//a[contains(text(),'New Account')]").click()
     sleep(2)  # Allow the page to load

     # Enter valid Customer ID and Initial Deposit
     customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
     initial_deposit_field = self.driver.find_element(By.XPATH, "//tbody/tr[4]/td[2]/input[1]")
     customer_id_field.send_keys("98560")  # Valid Customer ID
     initial_deposit_field.send_keys("5000")  # Valid initial deposit

     # Click the Submit button
     self.driver.find_element(By.XPATH, "//tbody/tr[5]/td[2]/input[1]").click()
     sleep(2)

     # Verify success message
     success_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Account Generated Successfully')]")
     self.assertEqual(success_message.text, "Account Generated Successfully!!!",
                      "Expected success message not displayed")
     # Click on the "Continue" hyperlink
     continue_link = self.driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]")
     continue_link.click()
     sleep(2)

     # Verify redirection to the home page by checking for Manager ID
     manager_id_displayed = self.driver.find_element(By.XPATH, "//td[contains(text(),'Manger Id : mngr601595')]").text
     self.assertIn("Manger Id : mngr601595", manager_id_displayed, "Failed to return to the home page after clicking Continue.")

if __name__ == "__main__":
    unittest.main()
