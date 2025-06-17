class ConversorMorse():

    def __init__(self):
        self.mapeamento_cod_morse = {
                                        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
                                        'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
                                        'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
                                        'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
                                        'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
                                        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
                                        'Y': '-.--',  'Z': '--..',
                                        
                                        '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                                        '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                                        '9': '----.', '0': '-----',
                                        
                                        ' ': ' /'  # separador entre palavras

                                    }

    def __call__(self, frase : str) -> str:
        codigo_morse = ''

        for letra in frase.upper():
            codigo_morse += self.mapeamento_cod_morse[letra] + ' '
        
        return codigo_morse[:-1] # remove o ultimo espaço