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

    # View Employee Data
    def test_a_vD(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "employee").click()
        self.driver.find_element(By.ID, "employee").send_keys("Cecil Bonaparte")
        self.driver.find_element(By.ID, "btnView").click()
        time.sleep(5)

    # View Detail Employee Data
    def test_b_viewDetailData(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "viewSubmitted").click()
        time.sleep(5)


    # View search week employers
    def test_c_searchWeekEmployers(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "viewSubmitted").click()
        self.driver.find_element(By.ID, "startDates").click()
        dropdown = self.driver.find_element(By.ID, "startDates")
        dropdown.find_element(By.XPATH, "//option[. = '2020-09-07 to 2020-09-13']").click()
        time.sleep(5)

    # Delete timesheets // fail
    def test_d_deleteDataTimesheetsPositiveCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "viewSubmitted").click()
        self.driver.find_element(By.ID, "btnEdit").click()
        self.driver.find_element(By.ID, "initialRows_1_toDelete").click()
        self.driver.find_element(By.ID, "submitRemoveRows").click()
        time.sleep(5)

    




    





if __name__ == "__main__": 
    unittest.main()