def test_soma(calc):
    assert calc.soma(2, 3) == 5
    assert calc.soma(-1, 1) == 0
    assert calc.soma(0, 0) == 0

def test_subtrai(calc):
    assert calc.subtrai(5, 3) == 2
    assert calc.subtrai(3, 5) == -2
    assert calc.subtrai(0, 0) == 0

def test_multiplica(calc):
    assert calc.multiplica(4, 5) == 20
    assert calc.multiplica(0, 10) == 0
    assert calc.multiplica(-2, 3) == -6

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    assert calc.divide(-6, 2) == -3

def test_divide_por_zero(calc):
    import pytest
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    assert calc.potencia(5, 0) == 1
    assert calc.potencia(9, 0.5) == 3

def test_raiz(calc):
    assert calc.raiz(4) == 2
    assert calc.raiz(0) == 0
    import pytest
    with pytest.raises(ValueError):
        calc.raiz(-9)
