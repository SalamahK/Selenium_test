import pytest
from pages.student_page import StudentPage

@pytest.mark.usefixtures("setup")
class TestStudents:
    base_url = "https://qastudent-development.ogtlprojects.com" 

    @pytest.mark.parametrize("first_name,last_name,reg_no", [
        (f"Student{i}", f"Last{i}", f"RegNo{i}") for i in range(1, 51)
    ])
    def test_create_student(self, first_name, last_name, reg_no):
        student_page = StudentPage(self.driver)

        # Navigate to the create student page
        self.driver.get(f"{self.base_url}/students/create")

        # Create the student using dynamic data
        student_page.create_student(first_name, last_name, reg_no)