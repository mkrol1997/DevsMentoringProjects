import pytest


@pytest.fixture
def set_config_values(mocker):
    mocker.patch('decouple.config', return_value='TEST_VALUE')


def test_connect_to_database_should_return_expected_str_when_connectedToDb(set_config_values):
    from UTs.Exercises.UTs_Exercise_6 import DbHandler
    actual = DbHandler().connect_to_database()
    expected = 'I am connecting to TEST_VALUE as TEST_VALUE with pass: TEST_VALUE...'

    assert actual == expected


def test_show_msg_when_connected_should_return_expected_str_when_connectedToDb(set_config_values):
    from UTs.Exercises.UTs_Exercise_6 import DbHandler
    actual = DbHandler().show_msg_when_connected()
    expected = 'TEST_VALUE'

    assert actual == expected

def test_show_msg_when_interrputed_should_return_expected_str_when_notConnectedToDb(set_config_values):
    from UTs.Exercises.UTs_Exercise_6 import DbHandler
    actual = DbHandler().show_msg_when_interrputed()
    expected = 'TEST_VALUE'

    assert actual == expected
