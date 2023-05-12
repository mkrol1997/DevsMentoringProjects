import pytest
from UTs.Exercises.UTs_Exercise_2 import *


def test_should_return_FizzBuzz_if_number_is_divisible_by_3_and_5():
    assert fizz_buzz(15) == "FizzBuzz"
    assert fizz_buzz(45) == "FizzBuzz"


def test_should_return_Fizz_if_number_is_divisible_by_3():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(81) == "Fizz"


def test_should_return_Buzz_if_number_is_divisible_by_5():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(100) == "Buzz"


def test_should_return_WrongNumber_if_number_is_not_divisible_by_3_or_5():
    assert fizz_buzz(28) == "Wrong number"
    assert fizz_buzz(997) == "Wrong number"



def test_should_raise_Exception_if_number_is_negative():
    with pytest.raises(Exception):
        fizz_buzz(-2)
        fizz_buzz(-13)


def test_should_raise_TypeError_if_number_is_not_type_int():
    with pytest.raises(TypeError):
        fizz_buzz('100')
        fizz_buzz([5])
        fizz_buzz(5.0)
