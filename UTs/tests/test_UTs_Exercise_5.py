from UTs.Exercises.UTs_Exercise_5 import *
from datetime import datetime

def test_calcDiff_should_return_correctValue_when_timeGapIs_one_hour(mocker):
    NOW = datetime(year=2021, month=11, day=3, hour=10, minute=22,  second=28, tzinfo=timezone.utc)
    mock_datetime = mocker.MagicMock(wraps=datetime)
    mock_datetime.now.return_value = NOW
    mocker.patch("UTs.Exercises.UTs_Exercise_5.datetime", mock_datetime)

    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }

    assert calc_diff(case) == 3600


def test_calcDiff_should_return_correctValue_when_timeGapIs_one_year_and_endTimeIs_None(mocker):
    NOW = datetime(year=2022, month=11, day=3, hour=9, minute=22,  second=28, tzinfo=timezone.utc)
    mock_datetime = mocker.MagicMock(wraps=datetime)
    mock_datetime.now.return_value = NOW
    mocker.patch("UTs.Exercises.UTs_Exercise_5.datetime", mock_datetime)

    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }

    assert calc_diff(case) == 31536000


def test_calcDiff_should_return_0_when_timeGapIs_0_and_endTimeIs_None(mocker):
    NOW = datetime(year=2021, month=11, day=3, hour=9, minute=22,  second=28, tzinfo=timezone.utc)
    mock_datetime = mocker.MagicMock(wraps=datetime)
    mock_datetime.now.return_value = NOW
    mocker.patch("UTs.Exercises.UTs_Exercise_5.datetime", mock_datetime)

    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': None
    }

    assert calc_diff(case) == 0

def test_calcDiff_should_return_0_when_timeGapIs_0_and_endTimeIs_set():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': '2021-11-03T09:22:28+00:00'
    }

    assert calc_diff(case) == 0


def test_calcDiff_should_return_correctValue_when_endTimeIs_set():
    case = {
        'start_time': '2021-11-03T09:22:28+00:00',
        'end_time': '2021-11-04T09:22:28+00:00'
    }

    assert calc_diff(case) == 86400
