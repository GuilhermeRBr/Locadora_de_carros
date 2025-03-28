from models.carros import Carro
from utils.checks import formatar_dinheiro

class Locadora():
    def __init__(self):
        self.carros = [Carro(
            modelo='civic', ano=2009, valor_diaria=150, disponivel=True),
            Carro(modelo='hillux', ano=2015, valor_diaria=200, disponivel=True),
            Carro(modelo='focus', ano=2011, valor_diaria=100, disponivel=False),
            ]

    def adicionar_carro(self, carro):
        self.carros.append(carro)
        print('\nCarro adicionado com sucesso !!\n') 

    def listar_carros_disponiveis(self):
        if not self.carros:
            print('\nNão há carros na locadora!!')
            return
        for carro in self.carros:
              if carro.disponivel:
                print(f'\nModelo: {carro.modelo.capitalize()} | Ano: {carro.ano} | Valor da diaria: {formatar_dinheiro(carro.valor_diaria)}')
        print('')

    def alugar_carro(self, modelo):
        if not self.carros:
            print('\nNão há carros na locadora!!')
            return
        
        for carro in self.carros:
            if modelo.lower() == carro.modelo.lower():  
                print('\nParabens, você alugou um novo veiculo')
                carro.alugar()
                return
            
        print(f'\n{modelo} Não esta disponivel para aluguel') 



    def devolver_carro(self, modelo, dias):
        if not self.carros:
            print('\nNão há carros na locadora !!')
            return
        for carro in self.carros:
            if modelo.lower() == carro.modelo.lower():
                print(f'\nO valor a ser pago pelo aluguel do {modelo} é de: {formatar_dinheiro(carro.devolver(dias))}\nObrigado por alugar conosco!!\n')
                return
        print(f'\nEste modelo não se encontra na nossa locadora!!')