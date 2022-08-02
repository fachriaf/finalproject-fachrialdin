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

    # POSITIVE CASE
    
    # search admin      
    def test_a_dashboardSearchUsers(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "searchSystemUser_userName").click()
        self.driver.find_element(By.ID, "searchSystemUser_userName").send_keys("Admin")
        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)
    
    # search role
    def test_b_adminsearchroles(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "searchSystemUser_userType").click()
        dropdown = self.driver.find_element(By.ID, "searchSystemUser_userType")
        dropdown.find_element(By.XPATH, "//option[. = 'Admin']").click() # search role
        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)

    # search employee
    def test_c_adminsearchemployee(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "menu_admin_viewSystemUsers").click()
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").click()
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").send_keys("Ananya Dash")
        self.driver.find_element(By.ID, "searchBtn").click()
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").click()
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)

    def test_d_adminsearchstatus(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "searchSystemUser_status").click()
        dropdown = self.driver.find_element(By.ID, "searchSystemUser_status")
        dropdown.find_element(By.XPATH, "//option[. = 'Enabled']").click()
        self.driver.find_element(By.ID, "searchBtn").click()
        time.sleep(3)

    # reset data
    def test_e_resetAdminData(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.LINK_TEXT, ">").click()
        self.driver.find_element(By.LINK_TEXT, ">").click()
        self.driver.find_element(By.ID, "searchSystemUser_userType").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_userName").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_userName").send_keys("Admin")
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_userType").click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.ID, "searchSystemUser_userType")
        time.sleep(3)
        dropdown.find_element(By.XPATH, "//option[. = 'Admin']").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_employeeName_empName").send_keys("a")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ac_odd:nth-child(4)").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "searchSystemUser_status").click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.ID, "searchSystemUser_status")
        time.sleep(3)
        dropdown.find_element(By.XPATH, "//option[. = 'Enabled']").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "resetBtn").click()
        time.sleep(3)

    # delete data      
    def test_f_deleteAdminData(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "ohrmList_chkSelectRecord_18").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "btnDelete").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "dialogDeleteBtn").click()
        time.sleep(3)

    # Add admin data      
    def test_g_addDataUsers(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        element = self.driver.find_element(By.ID, "frmLogin")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "frmLogin")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "frmLogin")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.CSS_SELECTOR, "#menu_admin_viewAdminModule > b").click()
        self.driver.find_element(By.ID, "btnAdd").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_userType").click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.ID, "systemUser_userType")
        time.sleep(3)
        dropdown.find_element(By.XPATH, "//option[. = 'Admin']").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("l")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".ac_even:nth-child(3)").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_userName").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_userName").send_keys("sdsss_")
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_status").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "systemUser_status").click()
        time.sleep(3)
        element = self.driver.find_element(By.ID, "systemUser_status")
        time.sleep(3)
        actions = ActionChains(self.driver)
        time.sleep(3)
        actions.double_click(element).perform()
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




if __name__ == "__main__": 
    unittest.main()