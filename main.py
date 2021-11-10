import unittest

# import HtmlTestRunner

import TestRunner

from appium import webdriver 

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        desired_caps = dict(
        platformName='Android',
        deviceName='emulator-5558',
        appActivity='.service.LoginActivity',
        appPackage='com.sinhvien.quanlichitieu',
        noReset='true',
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def test_5_correct_account(self):
        print("test login with correct account")

        username = self.driver.find_element_by_id('com.sinhvien.quanlichitieu:id/edUsername')
        username.send_keys("test")

        password = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/edPassword")
        password.send_keys("test")

        current_screen = self.driver.current_activity

        login = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/btnLogin")
        login.click()

        message = self.driver.find_element_by_xpath("//android.widget.Toast[1]").get_attribute('text')
        self.assertEqual(message.strip(),"Dang nhap thanh cong")
        self.assertTrue(current_screen != self.driver.current_activity, True)

    def test_4_inncorrect_account(self):
        print("test login with incorrect account")
 
        username = self.driver.find_element_by_id('com.sinhvien.quanlichitieu:id/edUsername')
        username.send_keys("test")

        password = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/edPassword")
        password.send_keys("123")

        login = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/btnLogin")
        login.click()

        message = self.driver.find_element_by_xpath("//android.widget.Toast[1]").get_attribute('text')
        self.assertEqual(message,"Email hoac mat khau khong chinh xac")

    def test_3_empty_password(self):
        print("test login with empty password")

        username = self.driver.find_element_by_id('com.sinhvien.quanlichitieu:id/edUsername')
        username.send_keys("test")
        login = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/btnLogin")
        login.click()
        error_state = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/edPassword")
        is_error = error_state.get_attribute("focused")
        self.assertEqual(is_error,'true')


    def test_2_empty_username(self):
        print("test login with empty username")

        login = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/btnLogin")
        login.click()
        error_state = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/edUsername")
        is_error = error_state.get_attribute("focused")
        self.assertEqual(is_error,'true')

    
    def test_1_empty_two_field(self):
        print("test login with empty username and password")

        login = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/btnLogin")
        login.click()
        error_state = self.driver.find_element_by_id("com.sinhvien.quanlichitieu:id/edUsername")
        is_error = error_state.get_attribute("focused")
        self.assertEqual(is_error,'true')
     
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=TestRunner.TestRunner())