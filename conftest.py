import pytest


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="C:\\Users\\Kshitij Popli\\Desktop\\PythonPractice\\raw.csv", help="Enter the csv file locations"
         )
