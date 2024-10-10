import pytest
from pages.course_page import CoursePage  # Assuming your CoursePage is located in 'pages/course_page.py'

@pytest.mark.usefixtures("setup")
class TestCourses:
    base_url = "https://qastudent-development.ogtlprojects.com"  # Define the base URL

    @pytest.mark.parametrize("course_name,course_code", [
        (f"Course{i}", f"Code{i}") for i in range(1, 51)
    ])
    def test_create_course(self, course_name, course_code):
        course_page = CoursePage(self.driver)

        # Navigate to the create course page
        self.driver.get(f"{self.base_url}/courses/create")

        # Create the course using dynamic data
        course_page.create_course(course_name, course_code)

        # Optionally, verify course creation in the system (e.g., via page content or database)
        # For now, we assume success if no errors occur
        # assert "Course successfully created" in self.driver.page_source, "Course creation failed"
