import pytest
from src.lib.homepage import HomePage

@pytest.mark.HomePage
class TestHomePage():

    def test_001(self, setup):
        homepage = HomePage(setup)
        assert homepage.get_header() == "Welcome to the-internet", "Failed to load homepage"