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

    #add vacancies
    def test_a_addVacanciesNegatifCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#menu_recruitment_viewRecruitmentModule > b").click()
        self.driver.find_element(By.ID, "menu_recruitment_viewJobVacancy").click()
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.ID, "btnSave").click()
        time.sleep(3)

    # delete vacancies
    def test_b_deleteVacanciesNegatifCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#menu_recruitment_viewRecruitmentModule > b").click()
        self.driver.find_element(By.ID, "menu_recruitment_viewJobVacancy").click()
        time.sleep(3)

    #Search vacancies
    def test_c_searchVacanciesNegatifCase(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.set_window_size(1376, 744)
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("adin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
        self.driver.find_element(By.ID, "txtUsername").click()
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "frmLogin").click()
        self.driver.find_element(By.ID, "txtPassword").click()
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "txtPassword").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "#menu_recruitment_viewRecruitmentModule > b").click()
        self.driver.find_element(By.ID, "menu_recruitment_viewJobVacancy").click()
        self.driver.find_element(By.ID, "vacancySearch_jobTitle").click()
        self.driver.find_element(By.CSS_SELECTOR, ".inner:nth-child(2)").click()
        self.driver.find_element(By.ID, "vacancySearch_jobTitle").click()
        dropdown = self.driver.find_element(By.ID, "vacancySearch_jobTitle")
        dropdown.find_element(By.XPATH, "//option[. = 'IT Manager']").click()
        self.driver.find_element(By.ID, "vacancySearch_jobVacancy").click()
        dropdown = self.driver.find_element(By.ID, "vacancySearch_jobVacancy")
        dropdown.find_element(By.XPATH, "//option[. = 'Associate IT Manager']").click()
        self.driver.find_element(By.ID, "vacancySearch_hiringManager").click()
        dropdown = self.driver.find_element(By.ID, "vacancySearch_hiringManager")
        dropdown.find_element(By.XPATH, "//option[. = 'Odis Adalwin']").click()
        self.driver.find_element(By.ID, "vacancySearch_status").click()
        dropdown = self.driver.find_element(By.ID, "vacancySearch_status")
        dropdown.find_element(By.XPATH, "//option[. = 'Closed']").click()
        self.driver.find_element(By.ID, "btnSrch").click()
        time.sleep(3)






if __name__ == "__main__": 
    unittest.main()