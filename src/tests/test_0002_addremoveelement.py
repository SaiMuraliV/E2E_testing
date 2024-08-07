import pytest
from src.lib.homepage import HomePage
import random

@pytest.mark.AddElementPage
class TestAddRemoveElements():

    def test_AddElement_positvie(self, setup):
        homepage = HomePage(setup)
        addpage = homepage.click_addremoveelement()
        assert "Add/Remove Elements" == addpage.get_header(), "Failed to Navigate to Add Page"
        count = random.randint(1, 10)
        addpage.addbutton(count)
        assert addpage.deletebutton(count), "Delete Element was not successful"
    
    @pytest.mark.xfail
    def test_AddElement_failure(self, setup):
        homepage = HomePage(setup)
        addpage = homepage.click_addremoveelement()
        assert "Add/Remove Elements" == addpage.get_header(), "Failed to Navigate to Add Page"
        count = random.randint(1, 10)
        addpage.addbutton(count)
        assert addpage.deletebutton(count+1), "Delete Element was not successful"
    