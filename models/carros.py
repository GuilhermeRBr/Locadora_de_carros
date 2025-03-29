class Carro:
    def __init__(self, modelo, ano, valor_diaria, disponivel):
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = disponivel
 
    @staticmethod
    def devolver(dias, valor_diaria):
        valor_aluguel= valor_diaria * dias
        return valor_aluguel
        
