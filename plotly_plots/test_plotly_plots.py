import pytest

from die import Die as D

@pytest.fixture()
def die():
    """Used to create a class for ease of testing"""
    die = D()
    return die

def test_roll_die_gives_randint(die):
    """used to test the action of rolling die with our class Die"""
    poss_num = set(range(1, die.num_sides+1))
    rolled = set()

    while rolled != poss_num:
        rolled.add(die.roll_die())
    assert rolled == poss_num