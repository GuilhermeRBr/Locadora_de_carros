class Carro:
    def __init__(self, modelo, ano, valor_diaria):
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = True

    def exibir_disponivel(self):
        print(f'\nModelo: {self.modelo} | Ano: {self.ano} | Valor da diaria R$: {self.valor_diaria}')

    def alugar(self):
        self.disponivel = False
    
    def devolver(self, dias):
        self.disponivel = True
