import math

import pytest


@pytest.mark.usefixtures("timespan")
class TestMathFunctions:
    @pytest.mark.square
    def test_square(self, timespan):
        num=5
        assert (5*5)==25

    # Marker
    @pytest.mark.square
    def test_sqrt(self, timespan):
        num=25
        assert math.sqrt(num)==5

    # Marker
    @pytest.mark.xfail
    def test_equality(self, timespan):
        num=10
        assert num>8


