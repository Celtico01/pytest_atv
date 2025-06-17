import pytest
from calculadora import Calculadora

# Instância única compartilhada durante toda a sessão
calculadora = Calculadora()

@pytest.fixture(scope="session")
def calc():
    return calculadora
