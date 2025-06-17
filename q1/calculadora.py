import math
from datetime import datetime

class Calculadora:
    """Operações básicas"""

    def __init__(self):
        self.erros_log = []  # só armazenar mensagens de erro

    def _registrar_erro(self, mensagem: str):
        self.erros_log.append(mensagem)
        self.salvar_log_txt()

    def soma(self, a: float, b: float) -> float:
        try:
            return a + b
        except Exception as e:
            msg = f"[{datetime.now()}] Erro na soma: {e}"
            self._registrar_erro(msg)
            raise

    def subtrai(self, a: float, b: float) -> float:
        try:
            return a - b
        except Exception as e:
            msg = f"[{datetime.now()}] Erro na subtração: {e}"
            self._registrar_erro(msg)
            raise

    def multiplica(self, a: float, b: float) -> float:
        try:
            return a * b
        except Exception as e:
            msg = f"[{datetime.now()}] Erro na multiplicação: {e}"
            self._registrar_erro(msg)
            raise

    def divide(self, a: float, b: float) -> float:
        try:
            if b == 0:
                raise ValueError("Divisão por zero não é permitida")
            return a / b
        except Exception as e:
            msg = f"[{datetime.now()}] Erro na divisão: {e}"
            self._registrar_erro(msg)
            raise

    def potencia(self, base: float, expoente: float) -> float:
        try:
            return base ** expoente
        except Exception as e:
            msg = f"[{datetime.now()}] Erro na potenciação: {e}"
            self._registrar_erro(msg)
            raise

    def raiz(self, numero: float) -> float:
        try:
            if numero < 0:
                raise ValueError("Não é possível calcular raiz de número negativo")
            return math.sqrt(numero)
        except Exception as e:
            msg = f"[{datetime.now()}] Erro na raiz quadrada: {e}"
            self._registrar_erro(msg)
            raise

    def salvar_log_txt(self, caminho_arquivo="erros_calculadora.txt") -> None:
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                for linha in self.erros_log:
                    f.write(linha + "\n")
            print(f"Log de erros salvo em {caminho_arquivo}")
        except Exception as e:
            print(f"Erro ao salvar log de erros: {e}")
