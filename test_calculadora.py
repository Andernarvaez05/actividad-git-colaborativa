from calculadora import sumar, restar

def test_sumar():
    assert sumar(5, 3) == 8
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(10, 4) == 6
    assert restar(0, 5) == -5