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

    # POSITIVE CASE

    #ASSIGN DATA
    def test_addAssignLeave(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_leave_viewLeaveModule > b").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "menu_leave_assignLeave").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "assignleave_txtEmployee_empName").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "assignleave_txtEmployee_empName").send_keys("jyothi lakshmisetty")
        time.sleep(3)
        self.driver.find_element(By.ID, "assignleave_txtLeaveType").click()
        dropdown = self.driver.find_element(By.ID, "assignleave_txtLeaveType")
        dropdown.find_element(By.XPATH, "//option[. = 'CAN - Bereavement']").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .ui-datepicker-trigger").click()
        element = self.driver.find_element(By.LINK_TEXT, "1")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "1").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-trigger:nth-child(3)").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "7").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "assignleave_partialDays").click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.ID, "assignleave_partialDays")
        time.sleep(3)
        dropdown.find_element(By.XPATH, "//option[. = 'All Days']").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "assignleave_txtComment").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "assignleave_txtComment").send_keys("test")
        time.sleep(3)
        self.driver.find_element(By.ID, "assignBtn").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "confirmOkButton").click()
        time.sleep(3)

    #Start > End
    def test_a_assignLeaveStartDateMorethanEndDate(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_leave_viewLeaveModule > b").click()
        self.driver.find_element(By.ID, "menu_leave_assignLeave").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .ui-datepicker-trigger").click()
        element = self.driver.find_element(By.LINK_TEXT, "2")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "2").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-trigger:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "1").click()
        time.sleep(3)

    #Partial Day and coment isn't fill
    def test_a_partialDaysandCommentisntfill(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#menu_leave_viewLeaveModule > b").click()
        self.driver.find_element(By.ID, "menu_leave_assignLeave").click()
        self.driver.find_element(By.ID, "assignleave_txtEmployee_empName").click()
        self.driver.find_element(By.ID, "assignleave_txtEmployee_empName").send_keys("John Smith")
        self.driver.find_element(By.CSS_SELECTOR, "#frmLeaveApply ol").click()
        self.driver.find_element(By.ID, "assignleave_txtLeaveType").click()
        dropdown = self.driver.find_element(By.ID, "assignleave_txtLeaveType")
        dropdown.find_element(By.XPATH, "//option[. = 'CAN - Bereavement']").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) > .ui-datepicker-trigger").click()
        element = self.driver.find_element(By.LINK_TEXT, "5")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "5").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ui-datepicker-trigger:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "12").click()
        self.driver.find_element(By.ID, "assignleave_partialDays").click()
        self.driver.find_element(By.ID, "assignleave_txtComment").click()
        self.driver.find_element(By.ID, "assignBtn").click()
        element = self.driver.find_element(By.ID, "assignBtn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.ID, "confirmOkButton").click()




    

    





if __name__ == "__main__": 
    unittest.main()