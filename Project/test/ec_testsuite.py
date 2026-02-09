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

    def test_EC1_customer_id_cannot_be_empty(self):
        # Check that the Customer ID field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.click()
        customer_id_field.send_keys("")
        customer_id_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")
        self.assertEqual(error_message.text, "Customer ID is required")

    def test_EC2_customer_id_must_be_numeric(self):
        # Check that Customer ID must be numeric
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("1234Acc")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_EC3_customer_id_cannot_have_special_characters(self):
        # Check that Customer ID cannot have special characters
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("123!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message14")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_EC4_valid_customer_id(self):
        # Verify valid Customer ID redirects to Edit Customer page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        header = self.driver.find_element(By.XPATH, "//p[@class='heading3']").text
        self.assertEqual(header, "Edit Customer")

    def test_EC5_verify_address_field_cannot_be_empty(self):
        # Verify Address field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        address_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/textarea[1]")
        address_field.clear()
        address_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message3")
        self.assertEqual(error_message.text, "Address Field must not be blank")

    def test_EC6_verify_city_field_cannot_be_empty(self):
        # Verify City field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.clear()
        city_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "City Field must not be blank")

    def test_EC7_city_field_cannot_be_numeric(self):
        # Verify City field cannot accept numeric values
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.send_keys("1234")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "Numbers are not allowed")
        city_field.clear()
        city_field.send_keys("city123")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "Numbers are not allowed")

    def test_EC8_city_field_cannot_have_special_characters(self):
        # Verify City field cannot accept special characters
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.send_keys("City!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_EC9_verify_state_field_cannot_be_empty(self):
        # Verify State field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.clear()
        state_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "State must not be blank")

    def test_EC10_state_field_cannot_be_numeric(self):
        # Verify State field cannot accept numeric values
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.clear()
        state_field.send_keys("1234")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "Numbers are not allowed")
        state_field.clear()
        state_field.send_keys("State123")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "Numbers are not allowed")
    def test_EC11_state_field_cannot_have_special_characters(self):
        # Verify State field cannot accept special characters
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.clear()
        state_field.send_keys("State!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_EC12_pin_field_must_be_numeric(self):
        # Verify PIN field must be numeric
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.clear()
        pin_field.send_keys("1234PIN")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_EC13_pin_field_cannot_be_empty(self):
        # Verify PIN field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.clear()
        pin_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "PIN Code must not be blank")

    def test_EC14_pin_field_must_have_6_digits(self):
        # Verify PIN field must have exactly 6 digits
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.send_keys("123")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "PIN Code must have 6 Digits")
        pin_field.clear()
        pin_field.send_keys("1234567")
        sleep(1)
        self.assertEqual(error_message.text, "PIN Code must have 6 Digits")

    def test_EC15_pin_field_cannot_have_special_characters(self):
        # Verify PIN field cannot accept special characters
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.clear()
        pin_field.send_keys("123!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_EC16_mobile_number_field_cannot_be_empty(self):
        # Verify Mobile Number field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        mobile_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        mobile_number_field.clear()
        mobile_number_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message7")
        self.assertEqual(error_message.text, "Mobile no must not be blank")

    def test_EC17_mobile_number_cannot_have_special_characters(self):
        # Verify Mobile Number cannot have special characters
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        mobile_field = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")

        # List of inputs with special characters
        invalid_mobile_numbers = ["886636!@12", "!@88662682", "88663682!@"]

        for mobile in invalid_mobile_numbers:
            # Clear the field and enter the test input
            mobile_field.clear()
            mobile_field.send_keys(mobile)
            sleep(1)

            # Locate and verify the error message
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message7")
            self.assertEqual(
                error_message.text,
                "Special characters are not allowed",
                f"Failed for input: {mobile}"
            )
    def test_EC18_email_field_cannot_be_empty(self):
        # Verify Email field cannot be empty
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        email_field = self.driver.find_element(By.XPATH, "//tbody/tr[12]/td[2]/input[1]")
        email_field.clear()
        email_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message9")
        self.assertEqual(error_message.text, "Email-ID must not be blank")

    def test_EC19_email_field_must_be_in_correct_format(self):
        # Verify Email field must have a valid format
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)
        email_field = self.driver.find_element(By.XPATH, "//tbody/tr[12]/td[2]/input[1]")
        invalid_emails = ["guru99@gmail", "guru99", "Guru99@", "gurugmail.com"]
        for email in invalid_emails:
            email_field.clear()
            email_field.send_keys(email)
            sleep(1)
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message9")
            self.assertEqual(error_message.text, "Email-ID is not valid", f"Failed for email: {email}")

    def test_EC20_submit_button_after_editing_all_fields(self):
        # Test editing all fields and submitting the form
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Edit Customer')]").click()

        # Enter valid customer ID and submit
        customer_id_field = self.driver.find_element(By.XPATH, "//tbody/tr[6]/td[2]/input[1]")
        customer_id_field.send_keys("98560")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)

        # Edit Address field
        address_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/textarea[1]")
        address_field.clear()
        address_field.send_keys("Updated Address")

        # Edit City field
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.clear()
        city_field.send_keys("UpdatedCity")

        # Edit State field
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.clear()
        state_field.send_keys("UpdatedState")

        # Edit PIN field
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.clear()
        pin_field.send_keys("123456")

        # Edit Mobile Number field
        mobile_number_field = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        mobile_number_field.clear()
        mobile_number_field.send_keys("9876543210")

        # Edit Email field
        email_field = self.driver.find_element(By.XPATH, "//tbody/tr[12]/td[2]/input[1]")
        email_field.clear()
        email_field.send_keys("updatedemail@guru99.com")

        # Submit the form
        self.driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[1]").click()
        sleep(2)

        # Verify success message
        success_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Update done successfully')]")
        self.assertEqual(success_message.text, "Update done successfully")

    @classmethod
    def tearDownClass(cls):
        # Quit the browser after tests
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
