# Crie uma hierarquia de classes para representar os diferentes tipos
# de funcionários de um escritório que tem os seguintes cargos:
# gerente, assistente e vendedor.

# Escreva uma superclasse abstrata chamada Funcionario que define o
# método abstrato calcular_salario().

# Essa classe também deve ter os seguintes atributos: nome, matricula
# e salario_base.

# A classe Funcionario deverá ser herdada pelas outras classes que
# são: Gerente, Assistente e Vendedor.

# Em cada classe-filha deve-se sobrescrever o método calcular_salario().
# Este método deve calcular e retornar o salário de cada funcionário,
# da seguinte forma:
# - O assistente recebe o salário_base.
# - O gerente recebe duas vezes o salário_base.
# - O vendedor recebe o salário_base mais uma comissão de 10%.
# - Implemente um programa principal que cria um objeto de cada tipo
# (gerente, assistente e vendedor) e os armazena em uma lista.
# Percorra essa lista e imprima o salário de cada funcionário.

from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self, nome, matricula, salario_base):
        pass


class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 2


class Assistente(Funcionario):
    def calcular_salario(self):
        return self.salario_base


class Vendedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.10)


# Programa Principal
gerente = Gerente('Augusto', 2222, 1500)
assistente = Assistente('Cesar', 5555, 2000)
vendedor = Vendedor('Zezé', 6666, 3000)

lista_objetos = [gerente, assistente, vendedor]

for item in range(len(lista_objetos)):
    print(lista_objetos[item].calcular_salario())
    item += 1
