import pytest
from funcionario import Funcionario
from calculadora_salario import CalculadoraSalario

@pytest.fixture
def calculadora():
    return CalculadoraSalario()

def test_salario_desenvolvedor_alto(calculadora):
    funcionario = Funcionario(nome="João", salario_base=15000, cargo="DESENVOLVEDOR")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 15000 * 0.2
    assert resultado == esperado

def test_salario_desenvolvedor_baixo(calculadora):
    funcionario = Funcionario(nome="Maria", salario_base=10000, cargo="DESENVOLVEDOR")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 10000 * 0.1
    assert resultado == esperado

def test_salario_dba_alto(calculadora):
    funcionario = Funcionario(nome="Carlos", salario_base=14000, cargo="DBA")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 14000 * 0.25
    assert resultado == esperado

def test_salario_dba_baixo(calculadora):
    funcionario = Funcionario(nome="Ana", salario_base=12000, cargo="DBA")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 12000 * 0.15
    assert resultado == esperado

def test_salario_testador_alto(calculadora):
    funcionario = Funcionario(nome="Pedro", salario_base=15000, cargo="TESTADOR")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 15000 * 0.25
    assert resultado == esperado

def test_salario_testador_baixo(calculadora):
    funcionario = Funcionario(nome="Laura", salario_base=11000, cargo="TESTADOR")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 11000 * 0.15
    assert resultado == esperado

def test_salario_gerente_alto(calculadora):
    funcionario = Funcionario(nome="Roberto", salario_base=14000, cargo="GERENTE")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 14000 * 0.3
    assert resultado == esperado

def test_salario_gerente_baixo(calculadora):
    funcionario = Funcionario(nome="Fernanda", salario_base=12000, cargo="GERENTE")
    resultado = calculadora.calcular_salario(funcionario)
    esperado = 12000 * 0.2
    assert resultado == esperado

def test_cargo_invalido(calculadora):
    funcionario = Funcionario(nome="Invalido", salario_base=10000, cargo="ESTAGIARIO")
    with pytest.raises(Exception, match="Cargo invalido!"):
        calculadora.calcular_salario(funcionario)
