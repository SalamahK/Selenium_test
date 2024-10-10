from selenium.webdriver.common.by import By

class CoursePage:
    def __init__(self, driver):
        self.driver = driver
        self.create_course_button = (By.LINK_TEXT, "Create Course")
        self.course_name_input = (By.ID, "name")
        self.course_code_input = (By.ID, "code")
        self.submit_button = (By.ID, "create_subj")
        self.update_button = (By.ID, "update_btn")
        self.edit_button = (By.XPATH, "//a[contains(text(), 'Edit')]")  
        self.delete_button = (By.XPATH, "//a[contains(text(), 'Delete')]")  

    def create_course(self, course_name, course_code):
        self.driver.find_element(*self.course_name_input).send_keys(course_name)
        self.driver.find_element(*self.course_code_input).send_keys(course_code)
        self.driver.find_element(*self.submit_button).click()

    def edit_course(self, new_course_name, new_course_code):
        self.driver.find_element(*self.edit_button).click()
        self.driver.find_element(*self.course_name_input).clear()
        self.driver.find_element(*self.course_name_input).send_keys(new_course_name)
        self.driver.find_element(*self.course_code_input).clear()
        self.driver.find_element(*self.course_code_input).send_keys(new_course_code)
        self.driver.find_element(*self.update_button).click()

    def delete_course(self):
        self.driver.find_element(*self.delete_button).click()
        self.driver.switch_to.alert.accept()
