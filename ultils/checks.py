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

def verificar_float():
    while True:
        valor = input('Digite o valor da diária R$: ')
        if valor.isdigit():
            valor = float(valor)
            return valor
        print('Valor inválido, digite novamente !!')

def verificar_int():
    while True:
        valor = input('Quantos dias ficou com o carro: ')
        if valor.isdigit():
            return int(valor)
        print('Valor inválido, digite novamente !!')