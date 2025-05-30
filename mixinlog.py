from abc import ABC, abstractmethod

class MixinLog(ABC):
    @abstractmethod
    def mostrar_log(self):
        pass

class MixinLogRoute(MixinLog):
    delimitador = '-=' * 45

    def __init__(self, rota: str, metodo: str, funcao: str):
        self.rota = rota
        self.metodo = metodo
        self.funcao = funcao

    def mostrar_log(self):
        print(self.delimitador)
        print(f'Rota usada: {self.rota}')
        print(f'Método usado: {self.metodo}')
        print(f'Função usada: {self.funcao}')
        print(self.delimitador)
