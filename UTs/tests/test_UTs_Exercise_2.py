import pytest
from UTs.Exercises.UTs_Exercise_2 import *


@pytest.mark.parametrize('number', [15, 45])
def test_should_return_FizzBuzz_if_number_is_divisible_by_3_and_5(number):
    actual = fizz_buzz(number)
    expected = "FizzBuzz"
    assert actual == expected


@pytest.mark.parametrize('number', [9, 576])
def test_should_return_Fizz_if_number_is_divisible_by_3_and_not_by_5(number):
    actual = fizz_buzz(number)
    expected = "Fizz"
    assert actual == expected


@pytest.mark.parametrize('number', [5, 100])
def test_should_return_Buzz_if_number_is_divisible_by_5_and_not_by_3(number):
    actual = fizz_buzz(number)
    expected = "Buzz"
    assert actual == expected


@pytest.mark.parametrize('number', [28, 997])
def test_should_return_WrongNumber_if_number_is_not_divisible_by_3_and_5(number):
    actual = fizz_buzz(number)
    expected = "Wrong number"
    assert actual == expected


@pytest.mark.parametrize('number', [-13, -127836])
def test_should_raise_Exception_if_number_is_negative(number):
    with pytest.raises(Exception) as exc:
        fizz_buzz(number)
    assert str(exc.value) == "Number must be an integer greater than 1"

@pytest.mark.parametrize('number', ['100', [5], 5.0])
def test_should_raise_TypeError_if_number_is_not_type_int(number):
    with pytest.raises(TypeError) as exc:
        fizz_buzz(number)
    assert str(exc.value) == "Wrong type: expected class <int>"
