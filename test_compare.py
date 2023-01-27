# marker
import pytest


@pytest.mark.usefixtures("timespan")
class TestCompare:
    def test_greater_equal(self, timespan):
        num = 100
        assert num == 100

    def test_less(self, timespan):
        num = 100
        assert num < 200


