import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def _login(self, username, password):
        browser = self.browser
        user_field = browser.find_element_by_name('username')
        user_field.send_keys(username)

        password_field = browser.find_element_by_name('password')
        password_field.send_keys(password)
        
        password_field.send_keys(Keys.RETURN)

    def test_login(self):
        browser = self.browser
        browser.get("http://diabcontrol1.herokuapp.com")
        self._login('admin', 'admin123')
        self.assertIn('Welcome to DiabControl system', browser.page_source)

    def test_patients(self):
        browser = self.browser
        browser.get("http://diabcontrol1.herokuapp.com")
        self._login('doctor_a@example.com', 'admin123')

        # Narrowing web element, to be sure that link comes from nav
        nav = self.browser.find_element_by_css_selector('.nav-sidebar')
        nav.find_element_by_link_text("My patients").click()

        expected_headers = ['Email', 'First Name', 'Last Name']
        headers_text = [e.text for e in self.browser.find_elements_by_tag_name('th')]
        self.assertListEqual(expected_headers, headers_text)


if __name__ == "__main__":
    unittest.main()

