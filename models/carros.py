class Carro:
    def __init__(self, modelo, ano, valor_diaria):
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.disponivel = True
        print('Carro adicionado com sucesso !!')

    def alugar(self):
        self.disponivel = False
    
    def devolver(self, dias):
        self.disponivel = True
