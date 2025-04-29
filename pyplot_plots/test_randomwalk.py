import pytest

from random_walk import RandomWalk as rw

@pytest.fixture()
def ranwak():
    """Used for creat a resuable consistent instance of random walk class"""
    ranwak = rw()
    ranwak.run_walk()
    return ranwak

def test_default_5000_points_generated(ranwak):
    """test if the default 5000 parameter work as expected."""
    assert len(ranwak.x_val) == ranwak.num_points
    assert len(ranwak.y_val) == ranwak.num_points

def test_num_points_arg_matches_points_in_x_y(ranwak):
    """Used to chekc if when we pass a arg if it adds the correct amount of points."""
    ranwak.num_points = 50000
    ranwak.run_walk()
    assert len(ranwak.x_val) == ranwak.num_points
    assert len(ranwak.y_val) == ranwak.num_points

def test_points_can_generate_the_same_points(ranwak):
    """Checks to see that some points do indeed match. By using the set function to remove all
    dups from the list changing the len value."""
    points = list(zip(ranwak.x_val, ranwak.y_val))
    assert len(points) != len(set(points))