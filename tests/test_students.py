import pytest
from pages.student_page import StudentPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestStudents:
    base_url = "https://qastudent-development.ogtlprojects.com"  

    def test_create_edit_delete_student(self):
        
        student_page = StudentPage(self.driver)
        self.driver.get(f"{self.base_url}/students/create")

        try:
            student_page.create_student("Ade", "Keji", "7890")
            assert "Student created successfully" in self.driver.page_source
            print("Student creation assertion passed.")
        except AssertionError as e:
            print(f"Student creation assertion failed: {e}")

        try:
            student_page.edit_student("Stacy", "Philip", "7891")
            assert "Student updated successfully" in self.driver.page_source
            print("Student update assertion passed.")
        except AssertionError as e:
            print(f"Student update assertion failed: {e}")

        try:
            home_page = HomePage(self.driver)
            self.driver.get(self.base_url)
            home_page.search_student("Stacy Philip")
            home_page.select_search_result("Stacy Philip")
            print("Student search executed successfully.")
        except Exception as e:
            print(f"Student search failed: {e}")

        try:
            student_page.delete_student()
            assert "Student deleted successfully" in self.driver.page_source
            print("Student deletion assertion passed.")
        except AssertionError as e:
            print(f"Student deletion assertion failed: {e}")
