import pytest
from UTs.Exercises.UTs_Exercise_3 import quickSort


@pytest.mark.parametrize('actual', [[], [13], [11.1, 10, 11], [44, -44, 44], [8, 7, 2, 1, 0, 9, 6]])
def test_should_sort_given_array_of_integer_numbers_in_ascending_order(actual):
    expected = sorted(actual)
    quickSort(actual, 0, len(actual) - 1)

    assert actual == expected


@pytest.mark.parametrize('actual', ['sdasd', [[5], 15, 45], [2, 1, 0, '9', 6]])
def test_should_raise_type_error_when_array_contains_type_other_than_int_or_float(actual):
    with pytest.raises(TypeError):
        quickSort(actual, 0, len(actual) - 1)
