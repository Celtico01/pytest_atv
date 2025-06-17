import pytest
from conversor_romano import Conversor  # Ajuste o import conforme seu arquivo

@pytest.fixture
def conversor():
    return Conversor()

def test_conversao_basica(conversor):
    assert conversor.converter(1) == "I"
    assert conversor.converter(3) == "III"
    assert conversor.converter(4) == "IV"
    assert conversor.converter(9) == "IX"
    assert conversor.converter(58) == "LVIII"
    assert conversor.converter(1994) == "MCMXCIV"

def test_limites_validos(conversor):
    assert conversor.converter(3999) == "MMMCMXCIX"

def test_valores_invalidos(conversor):
    with pytest.raises(ValueError, match="Valor para converter não pode ser negativo ou zero."):
        conversor.converter(0)
    with pytest.raises(ValueError, match="Valor para converter não pode ser negativo ou zero."):
        conversor.converter(-5)
    with pytest.raises(ValueError, match="O limite do conversor é 3999"):
        conversor.converter(4000)

def test_tipo_entrada(conversor):
    with pytest.raises(TypeError, match="O valor deve ser um inteiro"):
        conversor.converter("dez")
    with pytest.raises(TypeError, match="O valor deve ser um inteiro"):
        conversor.converter(3.14)
