import pytest
from conversor_morse import ConversorMorse  # ajuste o nome do arquivo conforme necessário

@pytest.fixture
def conversor():
    return ConversorMorse()

def test_letras_simples(conversor):
    assert conversor("A") == ".-"
    assert conversor("SOS") == "... --- ..."

def test_numeros(conversor):
    assert conversor("123") == ".---- ..--- ...--"

def test_misto(conversor):
    assert conversor("HELLO 2025") == ".... . .-.. .-.. ---  / ..--- ----- ..--- ....."

def test_espacos(conversor):
    assert conversor("A B C") == ".-  / -...  / -.-."

def test_minusculas(conversor):
    assert conversor("sos") == "... --- ..."

def test_necio(conversor):
    assert conversor('VASCAO') == "...- .- ... -.-. .- ---"

def test_string_vazia(conversor):
    assert conversor("") == ""

def test_caractere_invalido(conversor):
    with pytest.raises(KeyError):
        conversor("Olá!")  # "Á" e "!" não estão no mapeamento
