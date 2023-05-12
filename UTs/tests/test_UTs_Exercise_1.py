from UTs.Exercises.UTs_Exercise_1 import *
import pytest


@pytest.mark.is_prime
def test_should_return_true_if_number_is_2():
    number = 2
    assert is_prime_number(number)

@pytest.mark.is_prime
def test_should_return_true_if_number_is_prime_and_greater_than_two():
    assert is_prime_number(7)
    assert is_prime_number(211)
    assert is_prime_number(15485863)

@pytest.mark.is_not_prime
def test_should_return_false_if_number_is_type_float():
    number = 179.1

    assert not is_prime_number(number)

@pytest.mark.is_not_prime
def test_should_return_false_if_number_is_type_str():
    number = '13'

    assert not is_prime_number(number)

@pytest.mark.is_not_prime
def test_should_return_false_if_number_is_negative():
    number = -7

    assert not is_prime_number(number)

@pytest.mark.is_not_prime
def test_should_return_false_if_number_is_0():
    number = 0

    assert not is_prime_number(number)

@pytest.mark.is_not_prime
def test_should_return_false_if_number_is_1():
    number = 1

    assert not is_prime_number(number)

