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

    #invalid view data
    def test_a_searchinvaliddata(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "employee").click()
        self.driver.find_element(By.ID, "employee").send_keys("Luis Suarez")
        element = self.driver.find_element(By.ID, "btnView")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.ID, "btnView").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        time.sleep(5)
    # delete rows (ok)
    def test_b_deleteRowsNegativeCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "viewSubmitted").click()
        self.driver.find_element(By.ID, "btnEdit").click()
        self.driver.find_element(By.ID, "submitRemoveRows").click()
        time.sleep(5)

    # reset rows (no)
    def test_c_resetRows(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_time_viewTimeModule > b").click()
        self.driver.find_element(By.ID, "viewSubmitted").click()
        self.driver.find_element(By.ID, "btnEdit").click()
        self.driver.find_element(By.ID, "btnReset").click() 
        time.sleep(5)
  

    





if __name__ == "__main__": 
    unittest.main()