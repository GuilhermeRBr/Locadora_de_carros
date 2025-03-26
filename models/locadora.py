from models.carros import Carro

class Locadora():
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)
        print('\nCarro adicionado com sucesso !!') 

    def listar_carros_disponiveis(self):
        if not self.carros:
            print('\nNão ha carros na locadora!!')
        for i in self.carros:
            i.exibir_disponivel()
            

    def alugar_carro(modelo):
        pass

    def devolver_carro(modelo, dias):
        pass