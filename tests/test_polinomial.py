from polinomials import Polinomial
def test_print():

    p= Polinomial((2,1,0,3))
    assert str(p) == "3x^3 + x + 2"

import pytest
def test_equality():
    assert Polinomial((0, 1)) == Polinomial((0, 1))


@pytest.mark.parametrize(
    "a, b, sum",
    (((0,), (0, 1), (0, 1)),
     ((2, 0, 3), (1, 2), (3, 2, 3)),
     ((4, 2), (10, 2, 4), (14, 4, 4)))
    )
def test_add(a, b, sum):
    assert Polinomial(a) + Polinomial(b) == Polinomial(sum)


def test_add_scalar():
    assert Polinomial((2, 1)) + 3 == Polinomial((5, 1))


def test_reverse_add_scalar():
    assert 3 + Polinomial((2, 1)) == Polinomial((5, 1))


def test_add_unknown():
    with pytest.raises(TypeError):
        Polinomial((1,)) + "frog"

