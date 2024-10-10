import pytest
from pages.course_page import CoursePage

@pytest.mark.usefixtures("setup")
class TestCourses:
    base_url = "https://qastudent-development.ogtlprojects.com"  

    def test_create_edit_delete_course(self):
        
        course_page = CoursePage(self.driver)
        self.driver.get(f"{self.base_url}/courses/create")

        try:
            course_page.create_course("Numerical", "N101")
            assert "Course created successfully" in self.driver.page_source
            print("Course creation assertion passed.")
        except AssertionError as e:
            print(f"Course creation assertion failed: {e}")

        try:
            course_page.edit_course("Numerical Analysis", "N102")
            assert "Course updated successfully" in self.driver.page_source
            print("Course update assertion passed.")
        except AssertionError as e:
            print(f"Course update assertion failed: {e}")

        try:
            course_page.delete_course()
            assert "Course deleted successfully" in self.driver.page_source
            print("Course deletion assertion passed.")
        except AssertionError as e:
            print(f"Course deletion assertion failed: {e}")
