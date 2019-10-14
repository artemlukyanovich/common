import pytest

from homework import Rectangle

def test_get_rectangle_perimeter():
    assert Rectangle(1, 2).get_rectangle_perimeter() == (1+2)*2

def test_get_rectangle_square():
    assert Rectangle(1, 2).get_rectangle_square() == 1*2

def test_get_sum_of_corners():
    assert Rectangle(1, 2).get_sum_of_corners(3) == 3*90
    with pytest.raises(ValueError):
        Rectangle(1, 2).get_sum_of_corners(5)

def test_get_rectangle_diagonal():
    assert Rectangle(1, 2).get_rectangle_diagonal() == (1**2+2**2)**(1/2)

def test_get_radius_of_circumscribed_circle():
    assert Rectangle(1, 2).get_radius_of_circumscribed_circle() \
           == Rectangle(1, 2).get_rectangle_diagonal()/2
    assert Rectangle(1, 2).get_radius_of_circumscribed_circle() \
           == (1**2+2**2)**(1/2)/2

def test_get_radius_of_inscribed_circle():
    assert Rectangle(1, 1).get_radius_of_inscribed_circle() == 1/2
    with pytest.raises(ValueError):
        Rectangle(1, 2).get_radius_of_inscribed_circle()