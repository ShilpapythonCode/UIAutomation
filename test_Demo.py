import pytest
#from UIAutomation.test_timestamp import TestTime


@pytest.mark.usefixtures("timespan")
class TestMath():

    @pytest.mark.math
    def test_m1(self, timespan):
        #print("Start time", timespan)
        a=3
        b=4
        assert a+1 == b, "test passed"
       # assert a == b, "Test failed because a not equal to b "
        #print("End time", timespan)

    @pytest.mark.string
    def test_m2(self, timespan):
        name="selenium"
        assert name.upper()=="SELENIUM"

    @pytest.mark.string
    def test_m3(self, timespan):
        assert True

    @pytest.mark.string
    def test_m4(self, timespan):
        assert True

    @pytest.mark.math
    def test_m5(self, timespan):
        assert 100==100

    @pytest.mark.string
    def test_m6(self, timespan):
        assert "SELENIUM".lower()=="selenium"

    @pytest.mark.login
    def test_login_FB(self, timespan):
        assert "admin"+"123"=="admin123"

