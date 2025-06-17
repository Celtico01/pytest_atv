class Conversor():
    
    def __init__(self):
        self.mapeamento_valor = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:   'X',
            40:   'XL',
            50:   'L',
            90:   'XC',
            100:  'C',
            400:  'CD',
            500:  'D',
            900:  'CM',
            1000: 'M'
        }
    
    def converter(self, valor: int) -> str:
        
        if not isinstance(valor, int):
            raise TypeError("O valor deve ser um inteiro")
        if valor <= 0:
            raise ValueError('Valor para converter não pode ser negativo ou zero.')
        if valor > 3999:
            raise ValueError('O limite do conversor é 3999')
        
        resultado = ""
        valores = sorted(self.mapeamento_valor.keys(), reverse=True)
        
        for v in valores:
            while valor >= v:
                resultado += self.mapeamento_valor[v]
                valor -= v
        
        return resultado
