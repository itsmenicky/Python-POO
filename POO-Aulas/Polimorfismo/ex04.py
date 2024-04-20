# Um banco trabalha com três tipos de contas:
# - conta corrente
# - conta especial
# - conta poupança

# Em todas as contas é necessário armazenar o número da conta, o nome 
# do correntista e o saldo.

# Para a conta especial é necessário armazenar também o valor do 
# limite.

# As operações possíveis são: depósito, saque e impressão do saldo. 
# Essas operações devem ser definidas numa classe abstrata denominada 
# Conta.
# - A operação de depósito e saldo são iguais para os três tipos de 
# conta.
# - A operação de saque só é diferente na conta especial, pois esta 
# admite que o saldo fique negativo até o limite estabelecido.
# - Nas demais contas o saque não pode ser realizado se não houver 
# saldo suficiente.

# Implemente uma hierarquia de classes que atenda a descrição acima.

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    def deposito(self, valor):
        self.saldo += valor
    @abstractmethod
    def saque(self, valor):
        pass
    def impressao_saldo(self):
        print(f"Saldo do correntista: {self.saldo}")

class ContaCorrente(Conta):
    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente!")
        else:
            self.saldo -= valor

class ContaPoupanca(Conta):
    def saque(self, valor):
        if self.saldo < valor:
            print("Saldo Insuficiente!")
        else:
            self.saldo -= valor

class ContaEspecial(Conta):
    def __init__(self, numero, nome, saldo, limite):
        super().__init__(numero, nome, saldo)
        self.limite = limite
    def saque(self):
        self.saldo = -(self.limite) 

#Programa principal

conta_especial = ContaEspecial(222, 'Alberto', 1500, 100)
conta_corrente = ContaCorrente(333, 'Cláudio', 2000)
conta_poupanca = ContaPoupanca(444, 'Ana', 3500)

conta_especial.saque()
print(conta_especial.saldo)    #Resultado
conta_corrente.saque(300)
print(conta_corrente.saldo)   #1700
conta_poupanca.saque(300)
print(conta_poupanca.saldo)    #3200