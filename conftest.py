import pytest
from utils.base_test import BaseTest

@pytest.fixture(scope="class")
def setup(request):
    """
    Initializes the WebDriver for the test class and tears it down after tests are done.
    """
   
    base = BaseTest()

    base.setup(request)

    request.cls.driver = base.driver

    yield base.driver

    base.teardown()
