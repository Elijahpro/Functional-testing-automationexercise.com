# Test for adding to cart
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
