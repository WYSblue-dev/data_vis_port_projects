import pytest
from pay_generator import GetPayData

@pytest.fixture()
def pay_data_class():
    """Used to create a reusable class obj to perform testing of specific functions.
    Any additional steps for changing the obj should take place within testing."""
    pay_data = GetPayData(10)
    return pay_data

@pytest.fixture()
def mock_user_input_all_8(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: {
            'mon': '8',
            'tues': '8',
            'wed': '8',
            'thurs': '8',
            'fri': '8',
            'sat': '8',
            'sun': '8',
        }
        )
    
@pytest.fixture()
def mock_user_input_all_0(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: {
            'mon': '0',
            'tues': '0',
            'wed': '0',
            'thurs': '0',
            'fri': '0',
            'sat': '0',
            'sun': '0',
        }
        )

@pytest.fixture()
def mock_user_input_error_strs(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: {
            'mon': '8',
            'tues': '8',
            'wed': '8',
            'thurs': '8',
            'fri': '8',
            'sat': '8',
            'sun': '8',
        }
        )

@pytest.fixture()
def mock_user_input_empty_strs(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: {
            'mon': '',
            'tues': '',
            'wed': '',
            'thurs': '',
            'fri': '',
            'sat': '',
            'sun': '',
        }
        )

def test_get_hrs_worked_no_input(pay_data_class, mock_user_input_empty_strs):
    """Test to see that the when the user enter nothing doesn't break the program."""
    hour_list = pay_data_class.get_format_hrs_list(mock_user_input_empty_strs)
    money_on_hours = pay_data_class.get_rate_to_hour_data(hour_list)
    for money_on_hour in money_on_hours:
        assert money_on_hour == 0

