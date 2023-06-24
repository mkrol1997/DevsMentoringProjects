from UTs.Exercises.UTs_Exercise_8 import show_message
from unittest.mock import call
import pytest

@pytest.mark.parametrize('call_1, call_2, call_3',
                         [('Test message', 'Lorem Ipsum', 'qwerty'), (1, 2, 3), ([], [], [])])
def test_should_return_True_when_function_calls_equal_to_set_value(mocker, call_1, call_2, call_3):
    mock_show_message = mocker.Mock(spec=show_message)

    mock_show_message(call_1)
    mock_show_message(call_2)
    mock_show_message(call_3)

    calls = [call(call_1), call(call_2), call(call_3)]

    actual = mock_show_message.call_count
    expected = len(calls)

    mock_show_message.assert_has_calls(calls)
    assert actual == expected
