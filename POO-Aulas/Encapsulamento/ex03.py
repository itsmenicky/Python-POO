class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def get_senha(self):
        return self.__senha
    

class ContaBancaria:
    def __init__(self, numero, cliente, saldo, senha):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = saldo
        self.__senha = senha
    
    def __validar_senha(self, senha):
        if senha == self.cliente.get_senha():
            return True
        else:
            print('ERRO. Senha inválida')
            return False
    
    def sacar(self, valor, senha):
        if self.__validar_senha(senha):
            if valor <= self.__saldo:
                self.__saldo -= valor
                print('Saque realizado com sucesso')
            else:
                print('ERRO. Saldo insuficiente')
    
    def depositar(self, valor, senha):
        if self.__validar_senha(senha):
            self.__saldo += valor
            print('Depósito realizado com sucesso')
    
    def get_saldo(self):
        return self.__saldo

cliente1 = Cliente("João", "111111111", "123456")
conta = ContaBancaria(111, cliente1, 0, "123456")

while True:
    try:
        print('\033[0;32m1 - Depósito')
        print('2 - Saque')
        print('3 - Consultar Saldo')
        print('4 - Finalizar')
        opcao = int(input('Escolha uma das opções no menu: '))
        if opcao == 1:
            valor = float(input('\033[mValor para depósito: \033[m'))
            senha = input('Digite a senha: ')
            conta.depositar(valor, senha)
        elif opcao == 2:
            valor = float(input('Valor para saque: '))
            senha = input('Digite a senha: ')
            conta.sacar(valor, senha)
        elif opcao == 3:
            senha = input('Digite a senha: ')
            print(f"Saldo: {conta.get_saldo()}")
        elif opcao == 4:
            break
        else:
            print('Opção inválida. Digite novamente')
    except ValueError:
        print('Erro: Valor informado não é um número')