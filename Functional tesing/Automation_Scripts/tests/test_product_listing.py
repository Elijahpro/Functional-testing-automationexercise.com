# Test for product listing
 def test_product_listing(self):
        self.click_products_menu()
        products = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "productinfo")))
        self.assertGreater(len(products), 0, "❌ No products listed")
        print(f"✅ test_product_listing passed: Found {len(products)} products")