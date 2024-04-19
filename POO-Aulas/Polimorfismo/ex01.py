# Implemente as classes Operacao, Soma, Subtracao, Multiplicacao e
# Divisao:

# - A classe Operacao deve ser abstrata. O método calcular da classe
# Operação também deve ser abstrato.

# - As classes filhas devem implementar o método calcular.
# Esse método deve realizar a operação correspondente e retornar o resultado.

# - Observe que as classes não possuem atributos, portanto não
# precisam ter construtores.

from abc import ABC, abstractmethod


class Operacao(ABC):
    @abstractmethod
    def calcular(self, x, y):
        pass


class Soma(Operacao):
    def calcular(self, x, y):
        return x + y


class Subtracao(Operacao):
    def calcular(self, x, y):
        return x - y


class Multiplicacao(Operacao):
    def calcular(self, x, y):
        return x * y


class Divisao(Operacao):
    def calcular(self, x, y):
        return x / y

# Programa Principal

soma = Soma()
sub = Subtracao()
div = Divisao()
mult = Multiplicacao()

print(soma.calcular(10, 5))      # 15
print(sub.calcular(10, 5))       # 5
print(div.calcular(10, 5))       # 2.0
print(mult.calcular(10, 5))      # 50

