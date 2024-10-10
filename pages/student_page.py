from selenium.webdriver.common.by import By

class StudentPage:
    def __init__(self, driver):
        self.driver = driver
        self.create_student_button = (By.LINK_TEXT, "Create Student")
        self.first_name_input = (By.ID, "first_name")
        self.last_name_input = (By.ID, "last_name")
        self.reg_no_input = (By.ID, "reg_no")
        self.submit_button = (By.ID, "create_std")
        self.update_button = (By.ID, "edit_student")
        self.edit_button = (By.XPATH, "//a[contains(text(), 'Edit')]")  
        self.delete_button = (By.XPATH, "//a[contains(text(), 'Delete')]")  
    
    def create_student(self, first_name, last_name, reg_no):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.reg_no_input).send_keys(reg_no)
        self.driver.find_element(*self.submit_button).click()

    def edit_student(self, new_first_name, new_last_name, new_reg_no):
        self.driver.find_element(*self.edit_button).click()
        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.first_name_input).send_keys(new_first_name)
        self.driver.find_element(*self.last_name_input).clear()
        self.driver.find_element(*self.last_name_input).send_keys(new_last_name)
        self.driver.find_element(*self.reg_no_input).clear()
        self.driver.find_element(*self.reg_no_input).send_keys(new_reg_no)
        self.driver.find_element(*self.update_button).click()

    def delete_student(self):
        self.driver.find_element(*self.delete_button).click()
        self.driver.switch_to.alert.accept()
