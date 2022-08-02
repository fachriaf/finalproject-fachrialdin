import unittest
import time
from requests import delete
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit() 

    # NEGATIVE CASE

    #Required
    def test_addAssignLeaveNegativeCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_leave_viewLeaveModule > b").click()
        self.driver.find_element(By.ID, "menu_leave_assignLeave").click()
        self.driver.find_element(By.ID, "assignBtn").click()
        time.sleep(3)

    #Start Date < End Date
    def test_assignLeaveStartDateLessthanEndDate(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_leave_viewLeaveModule > b").click()
        self.driver.find_element(By.ID, "menu_leave_assignLeave").click()
        self.driver.find_element(By.ID, "assignleave_txtEmployee_empName").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .ui-datepicker-trigger").click()
        time.sleep(3)
        element = self.driver.find_element(By.LINK_TEXT, "10")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "10").click()
        time.sleep(3)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-trigger:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "17").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(7)").click()
        time.sleep(3)

    

    





if __name__ == "__main__": 
    unittest.main()