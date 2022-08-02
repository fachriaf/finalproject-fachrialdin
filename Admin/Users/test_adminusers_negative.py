import unittest
import time
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

    #Search users negative case
    def test_a_searchusersNegativeCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "searchSystemUser_userName").click()
        self.driver.find_element(By.ID, "searchSystemUser_userName").send_keys("HSHB")
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").click()
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").send_keys("ajjaja")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "#search_form ol").click()
        self.driver.find_element(By.ID, "searchSystemUser_userType").click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.ID, "searchSystemUser_userType")
        dropdown.find_element(By.XPATH, "//option[. = 'Admin']").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_status").click()
        dropdown = self.driver.find_element(By.ID, "searchSystemUser_status")
        dropdown.find_element(By.XPATH, "//option[. = 'Enabled']").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)

    #Add Exist Data Negative Case
    def test_b_addExistDataNegativeCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("a")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ac_even:nth-child(1)").click()
        self.driver.find_element(By.ID, "systemUser_userName").click()
        self.driver.find_element(By.ID, "systemUser_userName").send_keys("a")
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_userName").click()
        self.driver.find_element(By.ID, "systemUser_userName").send_keys("Aaliyah.Haq")
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_status").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_password").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_password").send_keys("viscabarca123")
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_confirmPassword").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_confirmPassword").send_keys("viscabarca123")
        time.sleep(3)
        self.driver.find_element(By.ID, "btnSave").click()
        time.sleep(3)
        element = self.driver.find_element(By.ID, "btnSave")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "btnSave")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "btnSave")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "btnSave").click()
        self.driver.find_element(By.ID, "btnSave").click()
        self.driver.find_element(By.ID, "btnSave").click()


    #Confirm Password Negative Case
    def test_c_addDataConfirmPasswordNegativeCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").click()
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("Leo messi")
        self.driver.find_element(By.ID, "systemUser_userName").click()
        self.driver.find_element(By.ID, "systemUser_userName").send_keys("leomessi_")
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").click()
        self.driver.find_element(By.ID, "systemUser_password").click()
        self.driver.find_element(By.ID, "systemUser_password").send_keys("viscabarca123")
        self.driver.find_element(By.ID, "systemUser_confirmPassword").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_confirmPassword").send_keys("viscabarca234")
        time.sleep(3)
        self.driver.find_element(By.ID, "btnSave").click()
        time.sleep(3)
    





if __name__ == "__main__": 
    unittest.main()