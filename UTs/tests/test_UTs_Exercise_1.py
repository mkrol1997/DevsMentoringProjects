from UTs.Exercises.UTs_Exercise_1 import is_prime_number
import pytest


@pytest.mark.is_prime
def test_should_return_true_if_number_isEqualTo_2():
    actual = is_prime_number(2)
    expected = True

    assert actual is expected


@pytest.mark.is_prime
@pytest.mark.parametrize("number", [7, 211, 15485863])
def test_should_return_true_if_number_is_prime_and_greater_than_two(number):
    actual = is_prime_number(number)
    expected = True

    assert actual is expected


@pytest.mark.is_not_prime
@pytest.mark.parametrize("number", [79.7, 101.0])
def test_should_return_false_if_number_is_type_float(number):
    actual = is_prime_number(number)
    expected = False

    assert actual is expected


@pytest.mark.is_not_prime
@pytest.mark.parametrize("number", ['13', 'TEST_STRING'])
def test_should_return_false_if_number_is_type_str(number):
    actual = is_prime_number(number)
    expected = False

    assert actual is expected


@pytest.mark.is_not_prime
@pytest.mark.parametrize('number', [-7, -123])
def test_should_return_false_if_integerNumber_is_from_negative_range(number):
    actual = is_prime_number(number)
    expected = False

    assert actual is expected


@pytest.mark.is_not_prime
@pytest.mark.parametrize('number', [1, 0])
def test_should_return_false_if_number_is_positive_integer_lower_than_2(number):
    actual = is_prime_number(number)
    expected = False

    assert actual is expected


