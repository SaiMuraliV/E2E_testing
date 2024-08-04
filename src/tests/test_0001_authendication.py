import pytest
from src.lib.homepage import HomePage

@pytest.mark.LoginPage
class TestLoginPage():

    def test_login_success(self, setup):
        homepage = HomePage(setup)
        auth = homepage.click_authendication()
        auth.login('tomsmith', 'SuperSecretPassword!')
        assert "invalid!" not in auth.read_message(), "Failed to log-in"
    
    @pytest.mark.xfail
    def test_login_failure(self, setup):
        homepage = HomePage(setup)
        auth = homepage.click_authendication()
        auth.login('tomsmith', 'SuperSecret')
        assert "invalid!" not in auth.read_message(), "Failed to log-in"