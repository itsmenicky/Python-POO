# Greetings User!! Code by Isolated Thinker ;)

from rich import print
from tqdm import tqdm
import time
import os

nome = input('Qual o seu nome??: ')
if nome.isdigit():
    print('[red]Heyy sem números, insira seu nome da próxima....Saindo....')
    exit()

else:
    print(f'[blue]---|Bem-vindo a minha calculadora em Python {nome}!! Por: Isolated Thinker|---')

def resultado():
    for i in tqdm(range(1), desc = 'Em um segundo você terá seu resultado...', colour='green'):
        time.sleep(1.5)
        os.system('cls')
    print(f'[green]-->O resultado dessa {operacao} é {x}')
    time.sleep(2)
    os.system('cls')

def invalido():
  if not num1.isdigit() or not num2.isdigit():
    os.system('cls')
    print('')
    print('[red]-->O valor insirido não é válido!!')
    time.sleep(0.9)
    os.system('cls')
    print('')
    print('[red]-->Por favor insira apenas números reais!!')
    os.system('cls')
    pass

while True:

    for i in tqdm(range(1), desc = 'Carregando...', colour='blue'):
     time.sleep(2.5)
     os.system('cls')
    operacao = str(input(f'-->Oque iremos fazer agora {nome}?? (multiplicacao, divisao, adicao ou subtracao)?: '))

    if operacao == "multiplicacao":
        os.system('cls')
        num1 = input('Insira o primeiro fator: ')
        num2 = input('Insira o segundo fator: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 * num2
        resultado()
        pergunta = str(input('-->Deseja realizar outra operação? (s/n): '))
        if pergunta == 's':
         pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Resposta inválida!!')
            break

    elif operacao == "divisao":
        os.system('cls')
        num1 = input('Insira o dividendo: ')
        num2 = input('Insira o divisor: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 / num2
        resultado()
        pergunta = str(input('-->Deseja realizar outra operação? (s/n): '))
        if pergunta == 's':
            pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Resposta inválida!!')
            break

    elif operacao == "adicao":
        os.system('cls')
        num1 = input('Insira o primeiro número: ')
        num2 = input('Insira o segundo número: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 + num2
        resultado()
        pergunta = str(input('-->Deseja realizar outra operação? (s/n): '))
        if pergunta == 's':
            pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Resposta inválida!!')
            break

    elif operacao == "subtracao":
        os.system('cls')
        num1 = input ('Insira o primeiro número: ')
        num2 = input ('Insira o segundo número: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 - num2
        os.system('cls')
        resultado()
        pergunta = str(input('-->Deseja realizar outra operação? (s/n): '))
        if pergunta == 's':
            pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Resposta inválida!!')
            break

    else:
        print('[red]-->Insira uma operação válida!!')