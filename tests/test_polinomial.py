from polinomials import Polinomial
def test_print():

    p= Polinomial((2,1,0,3))
    assert str(p) == "3x^3 + x + 2"
