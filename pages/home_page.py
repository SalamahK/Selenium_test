from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.ID, "search")  
        self.search_input = (By.CSS_SELECTOR, "input[placeholder='Search Student']")

    def search_student(self, search_term):
        self.driver.find_element(*self.search_input).send_keys(search_term)
        self.driver.find_element(*self.search_input).send_keys("\n")  

    def select_search_result(self, result_text):
        results = self.driver.find_elements(*self.search_result)
        for result in results:
            if result_text in result.text:
                result.click()
                break
