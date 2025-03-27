class Carro:
    def __init__(self, modelo, ano, valor_diaria, disponivel):
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def alugar(self):
        self.disponivel = False
    
    def devolver(self, modelo, dias):
        self.disponivel = True
        self.valor_diaria = self.valor_diaria * dias
        print(f'\nO valor a ser pago pelo aluguel do {modelo} é de R$: {self.valor_diaria}')