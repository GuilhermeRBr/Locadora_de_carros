from models.carros import Carro
from ultils.checks import formatar_dinheiro

class Locadora():
    def __init__(self):
        self.carros = [Carro(
            modelo='honda', ano=2009, valor_diaria=500, disponivel=True),
            Carro(modelo='toyota', ano=2010, valor_diaria=600, disponivel=True),
            Carro(modelo='ford', ano=2011, valor_diaria=700, disponivel=False),
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

    def alugar_carro(self, modelo):
        if not self.carros:
            print('\nNão há carros na locadora!!')
            return
        
        for carro in self.carros:
            if modelo.lower() == carro.modelo.lower():  
                print('Parabens, você alugou um novo veiculo')
                carro.alugar()
                return
            
        print(f'{modelo} Não esta disponivel para aluguel') 



    def devolver_carro(self, modelo, dias):
        if not self.carros:
            print('Não há carros na locadora !!')
            return
        for carro in self.carros:
            if modelo.lower() == carro.modelo.lower():
                carro.devolver(modelo, dias)
                return
        print(f'Este modelo não se encontra na nossa locadora!!')