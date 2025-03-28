# Locadora de Veículos

Este projeto é um sistema simples para gerenciar uma locadora de veículos, permitindo adicionar carros, listar os disponíveis, alugar e devolver veículos.

## 📌 Funcionalidades
- Adicionar um novo carro à locadora.
- Listar os carros disponíveis para aluguel.
- Alugar um carro informando o modelo.
- Devolver um carro e calcular o valor do aluguel com base nos dias de uso.

## 🚀 Como Usar
### 1️⃣ Executar o programa
Para rodar o código, execute o arquivo principal no terminal:
```bash
python main.py
```

### 2️⃣ Escolher uma opção no menu
O programa exibe um menu interativo:
```
BEM VINDO A LOCADORA DE VEÍCULOS !!

1 - Adicionar um novo carro à locadora.
2 - Ver a lista de carros disponíveis.
3 - Alugar um carro (digitando o modelo).
4 - Devolver um carro, informando quantos dias ficou com ele.
5 - Sair do programa.
```

Digite o número correspondente à ação desejada.

## 📂 Estrutura do Código
- `main()`: Função principal que gerencia o menu interativo.
- `Locadora`: Classe responsável pelo gerenciamento dos carros.
- `Carro`: Classe que representa um carro com atributos como modelo, ano e valor da diária.
- Funções auxiliares (`verificar_ano()`, `verificar_float()`, `verificar_int()`) para validar entradas do usuário.

## 🛠 Tecnologias Utilizadas
- Python 3

## 📜 Licença
Este projeto é apenas um exemplo de estudo e pode ser modificado livremente.

