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
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("https://demo.guru99.com/V4/")
        self.driver.find_element(By.NAME, "uid").send_keys("YOUR_ID")
        self.driver.find_element(By.NAME, "password").send_keys("YOUR_PASSWORD")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

    def test_NC1(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        customer_name_field = self.driver.find_element(By.CSS_SELECTOR, "table.layout:nth-child(8) table:nth-child(1) tbody:nth-child(1) tr:nth-child(4) td:nth-child(2) > input:nth-child(1)")
        customer_name_field.click()
        customer_name_field.send_keys(Keys.TAB)

    def test_NC2_invalid_name_field(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        customer_name_field = self.driver.find_element(By.CSS_SELECTOR, "table.layout:nth-child(8) table:nth-child(1) tbody:nth-child(1) tr:nth-child(4) td:nth-child(2) > input:nth-child(1)")
        customer_name_field.send_keys("1234")
        sleep(1)
        error_message = self.driver.find_element(By.ID, "message")
        self.assertEqual(error_message.text, "Numbers are not allowed")

    def test_NC3_special_characters_name_field(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        customer_name_field = self.driver.find_element(By.CSS_SELECTOR, "table.layout:nth-child(8) table:nth-child(1) tbody:nth-child(1) tr:nth-child(4) td:nth-child(2) > input:nth-child(1)")
        customer_name_field.send_keys("name!@#")
        sleep(1)
        error_message = self.driver.find_element(By.ID, "message")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_NC4_leading_space_name_field(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        customer_name_field = self.driver.find_element(By.CSS_SELECTOR, "table.layout:nth-child(8) table:nth-child(1) tbody:nth-child(1) tr:nth-child(4) td:nth-child(2) > input:nth-child(1)")
        customer_name_field.send_keys(" name")
        sleep(1)
        error_message = self.driver.find_element(By.ID, "message")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NC5_address_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        address_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/textarea[1]")
        address_field.click()
        address_field.send_keys("")
        address_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message3")
        self.assertEqual(error_message.text, "Address Field must not be blank")

    def test_NC6_address_field_leading_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        address_field = self.driver.find_element(By.XPATH, "//tbody/tr[7]/td[2]/textarea[1]")
        address_field.send_keys(" 123 oshawa")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message3")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NC7_city_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.click()
        city_field.send_keys("")
        city_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "City Field must not be blank")

    def test_NC8_city_field_cannot_be_numeric(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.send_keys("1234")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "Numbers are not allowed")

    def test_NC9_city_field_cannot_have_special_characters(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.send_keys("City!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_NC10_city_field_cannot_have_leading_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        city_field = self.driver.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        city_field.send_keys(" Oshawa")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message4")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NC11_state_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.click()
        state_field.send_keys("")
        state_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "State must not be blank")

    def test_NC12_state_field_cannot_be_numeric(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.send_keys("1234")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "Numbers are not allowed")

    def test_NC13_state_field_cannot_have_special_characters(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.send_keys("State!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_NC14_state_field_cannot_have_leading_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        state_field = self.driver.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        state_field.send_keys(" Punjab")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message5")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NC15_pin_field_must_be_numeric(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.send_keys("PIN1234")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_NC16_pin_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.click()
        pin_field.send_keys("")
        pin_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "PIN Code must not be blank")

    def test_NC17_pin_field_must_have_6_digits(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.send_keys("123")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "PIN Code must have 6 Digits")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "PIN Code must have 6 Digits")
        pin_field.clear()
        pin_field.send_keys("1234567")
        sleep(1)
        self.assertEqual(error_message.text, "PIN Code must have 6 Digits")

    def test_NC18_pin_field_cannot_have_special_characters(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.send_keys("123!@#")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "Special characters are not allowed")

    def test_NC19_pin_field_cannot_have_leading_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.send_keys(" 123456")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NC20_pin_field_cannot_have_blank_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        pin_field = self.driver.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        pin_field.send_keys("12 3456")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message6")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_NC21_mobile_number_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        mobile_field = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        mobile_field.click()
        mobile_field.send_keys("")
        mobile_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message7")
        self.assertEqual(error_message.text, "Mobile no must not be blank")

    def test_NC22_mobile_number_field_cannot_have_leading_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        mobile_field = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        mobile_field.send_keys(" 1234567890")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message7")
        self.assertEqual(error_message.text, "First character can not have space")

    def test_NC23_mobile_number_field_cannot_have_blank_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        mobile_field = self.driver.find_element(By.XPATH, "//tbody/tr[11]/td[2]/input[1]")
        mobile_field.send_keys("123 4567890")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message7")
        self.assertEqual(error_message.text, "Characters are not allowed")

    def test_NC24_mobile_number_field_cannot_have_special_characters(self):
        # Navigate to the "New Customer" page
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()

        # Locate the Mobile Number field
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

    def test_NC25_email_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        email_field = self.driver.find_element(By.XPATH, "//tbody/tr[12]/td[2]/input[1]")
        email_field.click()
        email_field.send_keys("")
        email_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message9")
        self.assertEqual(error_message.text, "Email-ID must not be blank")

    def test_NC26_email_field_must_be_in_correct_format(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        email_field = self.driver.find_element(By.XPATH, "//tbody/tr[12]/td[2]/input[1]")
        invalid_emails = ["guru99@gmail", "guru99", "Guru99@", "guru99@gmail.", "guru99gmail.com"]
        for email in invalid_emails:
            email_field.clear()
            email_field.send_keys(email)
            sleep(1)
            error_message = self.driver.find_element(By.CSS_SELECTOR, "#message9")
            self.assertEqual(error_message.text, "Email-ID is not valid")

    def test_NC27_email_field_cannot_have_blank_space(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        email_field = self.driver.find_element(By.XPATH, "//tbody/tr[12]/td[2]/input[1]")
        email_field.send_keys("guru 99@gmail.com")
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message9")
        self.assertEqual(error_message.text, "Email-ID is not valid")

    def test_NC28_password_field_cannot_be_empty(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'New Customer')]").click()
        password_field = self.driver.find_element(By.XPATH, "//tbody/tr[13]/td[2]/input[1]")
        password_field.click()
        password_field.send_keys("")
        password_field.send_keys(Keys.TAB)
        sleep(1)
        error_message = self.driver.find_element(By.CSS_SELECTOR, "#message18")
        self.assertEqual(error_message.text, "Password must not be blank")

    def tearDown(self):
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
