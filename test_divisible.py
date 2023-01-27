import pytest


@pytest.mark.usefixtures("input_val", "timespan")
class TestDivisibleClass:

    def test_divisible_by_3(self, input_val, timespan):
        #print("\n""Start Time ", timespan)
        print(input_val, "Divisible by 3")
        assert input_val % 3 == 0 , "Value is not divisible"

    def test_divisible_by_6(self,input_val ,timespan):
        #print("\n""Start Time ", timespan)
        print(input_val, "Divisible by 6")
        assert input_val % 6 == 0