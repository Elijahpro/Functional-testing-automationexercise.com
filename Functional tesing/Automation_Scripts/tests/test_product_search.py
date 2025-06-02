# Test for product search
def test_product_search(self):
        self.click_products_menu()
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "search_product")))
        search_box.send_keys("Tshirt")
        self.driver.find_element(By.ID, "submit_search").click()

        results = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "productinfo")))
        self.assertGreater(len(results), 0, "❌ No search results for 'Tshirt'")
        print("✅ test_product_search passed")