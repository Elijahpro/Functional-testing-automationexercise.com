import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class AutomationExerciseTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def click_products_menu(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/products']"))).click()
        except Exception as e:
            self.fail(f"❌ Could not find or click 'Products' menu: {e}")

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        driver.find_element(By.LINK_TEXT, "Signup / Login").click()

        timestamp = str(int(time.time()))
        name = "TestUser"
        email = f"testuser_{timestamp}@test.com"

        wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(name)
        driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
        driver.find_element(By.XPATH, "//button[text()='Signup']").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Enter Account Information')]")))

        driver.find_element(By.ID, "id_gender1").click()
        driver.find_element(By.ID, "password").send_keys("Test1234")
        driver.find_element(By.ID, "days").send_keys("10")
        driver.find_element(By.ID, "months").send_keys("June")
        driver.find_element(By.ID, "years").send_keys("1995")
        driver.find_element(By.ID, "first_name").send_keys("Test")
        driver.find_element(By.ID, "last_name").send_keys("User")
        driver.find_element(By.ID, "address1").send_keys("123 Test Street")
        driver.find_element(By.ID, "country").send_keys("Canada")
        driver.find_element(By.ID, "state").send_keys("State")
        driver.find_element(By.ID, "city").send_keys("City")
        driver.find_element(By.ID, "zipcode").send_keys("12345")
        driver.find_element(By.ID, "mobile_number").send_keys("1234567890")
        driver.find_element(By.XPATH, "//button[text()='Create Account']").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))
        driver.find_element(By.LINK_TEXT, "Continue").click()

        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()=' Delete Account']"))).click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))
        except:
            pass

        print("✅ test_register_user passed")

    def test_product_listing(self):
        self.click_products_menu()
        products = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "productinfo")))
        self.assertGreater(len(products), 0, "❌ No products listed")
        print(f"✅ test_product_listing passed: Found {len(products)} products")

    def test_product_search(self):
        self.click_products_menu()
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
        search_box.send_keys("Tshirt")
        self.driver.find_element(By.ID, "submit_search").click()

        results = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "productinfo")))
        self.assertGreater(len(results), 0, "❌ No search results for 'Tshirt'")
        print("✅ test_product_search passed")

    def test_add_to_cart(self):
        self.click_products_menu()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "productinfo")))

        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]")))
        add_button.click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Continue Shopping']"))).click()

        self.driver.find_element(By.XPATH, "//a[@href='/view_cart']").click()
        cart_items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_description")))

        self.assertGreater(len(cart_items), 0, "❌ Cart is empty")
        print("✅ test_add_to_cart passed")

    def test_login_logout(self):
        driver = self.driver
        wait = self.wait

        test_email = "eliasGudeta@gmail.com"
        test_password = "elias@1212"

        driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(test_email)
        driver.find_element(By.NAME, "password").send_keys(test_password)
        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        # Confirm login
        user_logged_in = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
        self.assertIn("Logged in as", user_logged_in.text)
        print("✅ Login successful")

        # Logout
        driver.find_element(By.LINK_TEXT, "Logout").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))

        print("✅ test_login_logout passed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
