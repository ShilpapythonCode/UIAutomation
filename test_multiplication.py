# Parameterized Test :
import pytest


@pytest.mark.usefixtures("timespan")
class TestParametrize:
    @pytest.mark.parametrize("num, output", [(1, 11), (2, 22), (3, 33), (4, 44), (5,55)])
    def test_multiplication_11(self, num, output, timespan):
        assert 11*num == output

    @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
    def test_val(self, test_input, expected, timespan):
        assert eval(test_input) == expected

    @pytest.mark.parametrize("data", [8,9,6,11])
    def test_greater_than_5(self, data, timespan):
        if data>5:
            assert True
        else:
            assert False, "given number is not greater than 5"

    @pytest.mark.parametrize("data", [1,2,4,3])
    def test_less_than_5(self, data, timespan):
        if data<5:
            assert True
        else:
            assert False, "given number is not less than 5"
