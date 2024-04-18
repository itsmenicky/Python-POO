# Escreva um programa para armazenar dados de veículos. 
# Crie a classe Motor que contém cilindrada e potencia. 
# Crie a classe Veiculo contendo ano de fabricação, preco e motor. Crie também o metodo exibir_dados para mostrar os dados do Veículo.
# Crie a classe Carro, que herda da classe Veiculo e adiciona os atributos cor e modelo. Crie também o metodo exibir_dados para mostrar os dados do Carro.
# Crie a classe Caminhão, que herda da classe Veiculo e adiciona o atributos comprimento (em metros). Crie também o metodo exibir_dados para mostrar os dados do Caminhão.
# Obs.: A classe Motor não possui relação de herança com a classe Veiculo, possui apenas uma relação de associação (o veiculo possui um motor)


class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia

class Veiculo():
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print(f"Ano do veículo: {self.ano}\nPreço: {self.preco}\nMotor: {self.motor}")


class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        print(f"Ano do veículo: {self.ano}\nPreço: {self.preco}\nMotor: \n Cilindrada:{self.motor.cilindrada}\n Potencia: {self.motor.potencia}\nCor: {self.cor}\nModelo: {self.modelo}\n\n")

class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento
    
    def exibir_dados(self):
        print(f"Ano do veículo: {self.ano}\nPreço: {self.preco}\nMotor: \n Cilindrada:{self.motor.cilindrada}\n Potencia: {self.motor.potencia}\nComprimento: {self.comprimento} metros")

motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()           # imprime os valores de todos os atributos do carro
caminhao.exibir_dados()        # imprime os valores de todos os atributos do caminhão