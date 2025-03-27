from models.carros import Carro
from models.locadora import Locadora
from ultils.checks import verificar_ano


def main():
    locadora = Locadora()

    opcao = 0
    while True:
        print('-' * 50)
        print('\nBEM VINDO A LOCADORA DE VEICULOS !!\n'
        '\n1 - Adicionar um novo carro à locadora.\n'
        '2 - Ver a lista de carros disponíveis.\n'
        '3 - Alugar um carro (digitando o modelo).\n'
        '4 - Devolver um carro, informando quantos dias ficou com ele.\n'
        '5 - Sair do programa.\n')

        opcao = input('Digite o numero da opção: ')
        print('')
        print('-' * 50)

        if opcao.isdigit():
            opcao = int(opcao)
            match opcao:
                case 1:
                    modelo = input('\nDigite o modelo do carro: ').lower()
                    ano = verificar_ano()
                    valor_diaria = input('Digite o valor da diária R$: ')
                    
                    while True:
                        if valor_diaria.isdigit():
                            valor_diaria = float(valor_diaria)
                            break
                        print('Valor inválido, digite novamente !!')
                        valor_diaria = input('Digite o valor da diária R$: ')

                    carro = Carro(modelo, ano, valor_diaria, True)
                    locadora.adicionar_carro(carro)

                case 2:
                    locadora.listar_carros_disponiveis()

                case 3:
                    modelo = str(input('\nDigite o modelo que deseja alugar: ').lower())
                    locadora.alugar_carro(modelo)

                case 4:
                    modelo = str(input('\nDigite o modelo que está alugado: ').lower())
                    dias = int(input('Quantos dias ficou com o carro: '))

                    locadora.devolver_carro(modelo, dias)

                case 5:
                    print('\nEncerrando programa...')
                    break

                case _:
                    print('\nDigite uma opção valida !!\n')
        else:
            print('\nDigite uma opção valida !!\n')
main()