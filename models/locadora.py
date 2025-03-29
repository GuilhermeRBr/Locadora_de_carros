from models.carros import Carro
from utils.checks import formatar_dinheiro
import json

class Locadora():
    def __init__(self):
        with open('models/carros.json', 'r') as arq:
            self.carros = json.load(arq)

    def adicionar_carro(self, carro):
        novo_carro = {
            'modelo': carro.modelo,
            'ano': carro.ano,
            'valor_diaria': carro.valor_diaria,
            'disponivel': carro.disponivel
        }
        try:
            self.carros.append(novo_carro)
            print('\nCarro adicionado com sucesso!!')
        except:
            print('\nErro ao adicionar carro')

        with open('models/carros.json', 'w') as arq:
            json.dump(self.carros, arq, indent=4, ensure_ascii=False)

    def listar_carros_disponiveis(self):
        if not self.carros:
            print('\nNão há carros na locadora!!')
            return
        for carro in self.carros:
            if carro['disponivel']:
                print(f'\n{carro['modelo'].capitalize()} | Ano: {carro['ano']} | Valor da diaria: {formatar_dinheiro(carro['valor_diaria'])}')
        print('')

    def alugar_carro(self, modelo):
        if not self.carros:
            print('\nNão há carros na locadora!!')
            return
        
        for carro in self.carros:
            if modelo.lower() == carro['modelo'].lower():  
                print('\nParabens, você alugou um novo veiculo')
                carro['disponivel'] = False

                with open('models/carros.json', 'w') as arq:
                    json.dump(self.carros, arq, indent=4, ensure_ascii=False)
                return
            
        print(f'\n{modelo} Não esta disponivel para aluguel') 



    def devolver_carro(self, modelo, dias):
        if not self.carros:
            print('\nNão há carros na locadora !!')
            return
        for carro in self.carros:
            if carro['disponivel'] == False:
                if modelo.lower() == carro['modelo'].lower():
                    print(f'\nO valor a ser pago pelo aluguel do {modelo.capitalize()} é de: {formatar_dinheiro(Carro.devolver(dias, carro['valor_diaria']))}\n\nObrigado por alugar conosco!!\n')
                    carro['disponivel'] = True
                    with open('models/carros.json', 'w') as arq:
                        json.dump(self.carros, arq, indent=4, ensure_ascii=False)
                    return
                
        print(f'\n{modelo.capitalize()} Não foi alugado por você!!')
