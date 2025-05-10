import pytest

from pay_generator import GetPayData

@pytest.fixture()
def pay_data():
    """Used to create a reusable class obj to perform testing of specific functions.
    Any additional steps for changing the obj should take place within testing."""
    pay_data = GetPayData(10)
    return pay_data

@pytest.mark.parametrize('inputs, expected'[
    ([0],{'mon':0},)
])

def test_get_hrs_worked_no_input(pay_data):
    """Test to see that the when the user enter nothing doesn't break the program."""
    temp_answers = pay_data._get_hrs_worked()
    assert temp_answers == dict

# need to review this to understand how this decortor works and what the set
# attr function is also need to look over lambda again which is a annonomyous func.

# @pytest.mark.parametrize('inputs, expected', [
#     # Test case for all zeros (no meaningful input)
#     ([0]*7, {'mon': 0, 'tue': 0, 'wed': 0, 'thu': 0, 'fri': 0, 'sat': 0, 'sun': 0}),
#     # Add more test cases as needed
# ])

# def test_get_hrs_worked_no_input(pay_data, inputs, expected, monkeypatch):
#     """Test that entering zeros doesn't break the program and returns proper structure."""
#     # Mock the input function to provide predefined answers
#     monkeypatch.setattr('builtins.input', lambda _: str(inputs.pop(0)))
    
#     result = pay_data._get_hrs_worked()
#     assert result == expected
