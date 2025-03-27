class Carro:
    def __init__(self, modelo, ano, valor_diaria, disponivel):
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel

    def alugar(self):
        self.disponivel = False
    
    def devolver(self, dias):
        self.disponivel = True
        valor_aluguel= self.valor_diaria * dias
        return valor_aluguel
        