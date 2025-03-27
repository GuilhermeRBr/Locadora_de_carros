from datetime import date


def formatar_dinheiro(valor):
    return f"R${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def verificar_ano():
    while True:
        ano = input('Digite o ano do carro: ')
        if ano.isdigit():
            ano = int(ano)
            if ano > 1900 and ano <= date.today().year:
                return ano
        print('Ano inválido, digite novamente !!')
