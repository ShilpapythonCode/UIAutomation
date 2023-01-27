import pytest


@pytest.mark.usefixtures("dataLoad", "dataShow", "timespan")
class TestFixtures:

    def test_multi(self, dataShow, timespan):
        a=10
        b=10
        assert a==b

    def test_m2(self, dataShow, timespan):
        a = 'Selenium'
        b = 'Welcome to Selenium Pytest.'
        assert a in b

    def test_dataExample(self, dataLoad, timespan):
        print("1717")
        print(dataLoad)
