from funcionario import Funcionario

class CalculadoraSalario():
    
    def __init__(self):
        self.tabela_encargos = {
                                'DESENVOLVEDOR' : {
                                                        'alto' : 0.2,
                                                        'baixo' : 0.1
                                                  },
                                'DBA' : {
                                            'alto' : 0.25,
                                            'baixo' : 0.15
                                        },
                                'TESTADOR' : {
                                                'alto' : 0.25,
                                                'baixo' : 0.15
                                             },
                                'GERENTE' : {
                                                'alto' : 0.3,
                                                'baixo' : 0.2
                                            }
                                }
        
    def calcular_salario(self, funcionario : Funcionario) -> float:

        match funcionario.cargo.upper():
            case 'DESENVOLVEDOR' :
                if funcionario.salario_base >= 13000:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['DESENVOLVEDOR']['alto']
                else:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['DESENVOLVEDOR']['baixo']
            case 'DBA' :
                if funcionario.salario_base >= 13000:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['DBA']['alto']
                else:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['DBA']['baixo']
            case 'TESTADOR' :
                if funcionario.salario_base >= 13000:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['TESTADOR']['alto']
                else:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['TESTADOR']['baixo']
            case 'GERENTE' :
                if funcionario.salario_base >= 13000:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['GERENTE']['alto']
                else:
                    salario_bruto = funcionario.salario_base * self.tabela_encargos['GERENTE']['baixo']
            case _:
                raise Exception('Cargo invalido!')
            
        return salario_bruto