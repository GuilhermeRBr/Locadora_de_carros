from models.carros import Carro
from models.locadora import Locadora


def main():
    locadora = Locadora()
    carro = Carro(None, None, None)
    opcao = 0
    while True:
        print('\nBEM VINDO A LOCADORA DE VEICULOS !!\n'
        '\n1 - Adicionar um novo carro à locadora.\n'
        '2 - Ver a lista de carros disponíveis.\n'
        '3 - Alugar um carro (digitando o modelo).\n'
        '4 - Devolver um carro, informando quantos dias ficou com ele.\n'
        '5 - Sair do programa.\n')

        opcao = int(input('Digite o numero da opção: '))

        match opcao:
            case 1:
                modelo = str(input('\nDigite o modelo do carro: '))
                ano = int(input('Digite o ano: '))
                valor_diaria = float(input('Digite o valor da diária R$: '))
                
                carro = Carro(modelo, ano, valor_diaria)
                locadora.adicionar_carro(carro)

            case 2:
                locadora.listar_carros_disponiveis()
            case 3:
                pass
            case 4:
                pass
            case 5:
                print('\nEncerrando programa...')
                break
            case _:
                print('\nDigite uma opção valida !!')
main()