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

    #ID Already exist

    def test_a_addEmployeeIDAlreadyExist(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_pim_viewPimModule > b").click()
        self.driver.find_element(By.ID, "menu_pim_addEmployee").click()
        self.driver.find_element(By.ID, "firstName").click()
        self.driver.find_element(By.ID, "firstName").send_keys("Leo")
        self.driver.find_element(By.ID, "lastName").click()
        self.driver.find_element(By.ID, "lastName").send_keys("Silva")
        self.driver.find_element(By.ID, "employeeId").click()
        self.driver.find_element(By.ID, "employeeId").send_keys("0272")
        self.driver.find_element(By.ID, "btnSave").click()
        self.driver.find_element(By.ID, "footer").click()

    #first and last name already exist
    def test_b_addEmployeewithoutfirstandlastname(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#menu_pim_viewPimModule > b").click()
        self.driver.find_element(By.ID, "menu_pim_addEmployee").click()
        self.driver.find_element(By.ID, "firstName").click()
        self.driver.find_element(By.ID, "middleName").click()
        self.driver.find_element(By.ID, "middleName").send_keys("Andreas")
        self.driver.find_element(By.ID, "btnSave").click()
        time.sleep(3)

    #username already exist
    def test_c_addEmployeeusernameAlreadyExist(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_pim_viewPimModule > b").click()
        self.driver.find_element(By.ID, "menu_pim_addEmployee").click()
        self.driver.find_element(By.ID, "firstName").click()
        self.driver.find_element(By.ID, "firstName").send_keys("Leo")
        self.driver.find_element(By.ID, "lastName").click()
        self.driver.find_element(By.ID, "lastName").send_keys("Messi")
        self.driver.find_element(By.ID, "chkLogin").click()
        self.driver.find_element(By.ID, "user_name").click()
        self.driver.find_element(By.ID, "user_name").send_keys("Aaliyah.Haq")
        self.driver.find_element(By.CSS_SELECTOR, ".loginSection:nth-child(5)").click()
        self.driver.find_element(By.ID, "user_password").click()
        self.driver.find_element(By.ID, "user_password").send_keys("viscabarca")
        self.driver.find_element(By.ID, "re_password").click()
        self.driver.find_element(By.ID, "re_password").send_keys("viscabarca")
        time.sleep(3)

    





if __name__ == "__main__": 
    unittest.main()