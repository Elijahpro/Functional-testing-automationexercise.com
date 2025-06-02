# Test for login and logout
def test_login_logout(self):
        driver = self.driver
        wait = self.wait

        test_email = "testuser_login@test.com"
        test_password = "Test1234"

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