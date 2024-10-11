import pytest
from pages.course_page import CoursePage  # Assuming your CoursePage is located in 'pages/course_page.py'

@pytest.mark.usefixtures("setup")
class TestCourses:
    base_url = "https://qastudent-development.ogtlprojects.com" 

    @pytest.mark.parametrize("course_name,course_code", [
        (f"Course{i}", f"Code{i}") for i in range(1, 51)
    ])
    def test_create_course(self, course_name, course_code):
        course_page = CoursePage(self.driver)

        self.driver.get(f"{self.base_url}/courses/create")

        course_page.create_course(course_name, course_code)

        
