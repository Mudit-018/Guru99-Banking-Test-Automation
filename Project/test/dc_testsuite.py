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

    def test_DC1_customer_id_cannot_be_empty(self):
        # Click on the "Delete Customer" option
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Leave the Customer ID field empty and press TAB
        customer_id_field.click()
        customer_id_field.send_keys("")  # Leave it empty
        customer_id_field.send_keys(Keys.TAB)  # Simulate pressing TAB to trigger validation
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Customer ID is required",
            "The expected error message for an empty Customer ID was not displayed."
        )

    def test_DC2_customer_id_must_be_numeric(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter character value into the Customer ID field
        customer_id_field.send_keys("Acc123")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "The expected error message for non-numeric Customer ID was not displayed."
        )

    def test_DC3_customer_id_cannot_have_special_characters(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter special characters into the Customer ID field
        customer_id_field.send_keys("123!@#")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Special characters are not allowed",
            "The expected error message for special characters in Customer ID was not displayed."
        )

    def test_DC4_customer_id_cannot_have_blank_space(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter a Customer ID with blank space
        customer_id_field.send_keys("123 12")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "Characters are not allowed",
            "The expected error message for blank space in Customer ID was not displayed."
        )

    def test_DC5_first_character_cannot_be_space(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter a Customer ID with a leading space
        customer_id_field.send_keys(" 12345")
        sleep(1)

        # Locate the error message
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")

        # Verify the error message is correct
        self.assertEqual(
            error_message.text,
            "First character can not have space",
            "The expected error message for leading space in Customer ID was not displayed."
        )

    def test_DC6_incorrect_customer_id(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter an incorrect Customer ID
        customer_id_field.send_keys("123456")
        sleep(1)

        # Click on the Submit button
        self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").click()
        sleep(2)

        # Handle the first alert: "Do you really want to delete this customer?"
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Do you really want to delete this Customer?",
            "The first confirmation alert was not displayed as expected."
        )
        alert.accept()  # Confirm deletion

        # Handle the second alert: "Customer does not exist!!"
        sleep(2)  # Wait for the second alert to appear
        second_alert = self.driver.switch_to.alert
        self.assertEqual(
            second_alert.text,
            "Customer does not exist!!",
            "The second alert for non-existent Customer ID was not displayed as expected."
        )
        second_alert.accept()  # Close the second alert

    def test_DC7_correct_customer_id_with_existing_accounts(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter a correct Customer ID (with existing accounts)
        customer_id_field.send_keys("4665")  # Replace with a valid customer ID for your test case
        sleep(1)

        # Click on the Submit button
        self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]").click()
        sleep(2)

        # Handle the first alert: "Do you really want to delete this customer?"
        alert = self.driver.switch_to.alert
        self.assertEqual(
            alert.text,
            "Do you really want to delete this Customer?",
            "The first confirmation alert was not displayed as expected."
        )
        alert.accept()  # Confirm deletion

        # Handle the second alert: "First delete all accounts of this customer then delete the customer"
        sleep(2)  # Wait for the second alert to appear
        second_alert = self.driver.switch_to.alert
        self.assertEqual(
            second_alert.text,
            "Customer could not be deleted!!. First delete all accounts of this customer then delete the customer",
            "The second alert for existing accounts was not displayed as expected."
        )
        second_alert.accept()  # Close the second alert

    def test_DC8_reset_button_clears_customer_id_field(self):
        # Go to Delete Customer page
        self.driver.find_element(By.XPATH, "//body/div[3]/div[1]/ul[1]/li[4]/a[1]").click()

        # Locate the Customer ID field
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")

        # Enter a value in the Customer ID field
        customer_id_field.send_keys("qwer")  # Enter any value, e.g., alphanumeric
        sleep(1)  # Allow time for input

        # Locate and click the Reset button
        reset_button = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[2]")
        reset_button.click()
        sleep(1)  # Allow time for the field to reset

        # Verify that the Customer ID field is cleared
        self.assertEqual(
            customer_id_field.get_attribute("value"),
            "",
            "The Customer ID field was not reset correctly."
        )

if __name__ == "__main__":
    unittest.main()
