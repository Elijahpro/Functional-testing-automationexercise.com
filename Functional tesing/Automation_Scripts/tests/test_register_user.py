# Test for user registration
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
