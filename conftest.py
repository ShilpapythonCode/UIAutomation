import datetime
import pytest


@pytest.fixture(scope="class")
def dataShow():
    print("Hellow I am first Fixtures")
    yield
    print("I will execute at last")


@pytest.fixture(scope="class")
def dataLoad():
    print("Hi!!!!!!!!!!!!!")
    return ["Shilpa", 37 , "shilpa.goldtree@gmail.com"]


@pytest.fixture(scope="class")
def input_val():
    input = 36
    return input


@pytest.fixture()
def timespan():
    current_time = datetime.datetime.now()
    print("\n""Start Time ",  current_time)
    yield
    print("\n""End Time ",  current_time)





