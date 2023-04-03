# Greetings User!! Code by itsmenicky ;)

from rich import print
from tqdm import tqdm
import time
import os

nome = input('Whats your name??: ')
if nome.isdigit():
    print('[red]Heyy no numbers, enter your name next time....closing....')
    exit()

else:
    print(f'[blue]---|Welcome to my calculator in pyhton {nome}!! By: Isolated Thinker|---')

def resultado():
    for i in tqdm(range(1), desc = 'in a second you will have your result...', colour='green'):
        time.sleep(1.5)
        os.system('cls')
    print(f'[green]-->The result of this {operacao} is {x}')
    time.sleep(2)
    os.system('cls')

def invalido():
  if not num1.isdigit() or not num2.isdigit():
    os.system('cls')
    print('')
    print('[red]-->Invalid value!!')
    time.sleep(0.9)
    os.system('cls')
    print('')
    print('[red]-->Please, enter only real numbers!!')
    os.system('cls')
    pass

while True:

    for i in tqdm(range(1), desc = 'Loading...', colour='blue'):
     time.sleep(2.5)
     os.system('cls')
     operacao = str(input(f'-->What we will gonna do now {nome}?? (multiplication, division, addition or subtraction)?: '))

    if operacao == "multiplication":
        os.system('cls')
        num1 = input('Enter with the first factor: ')
        num2 = input('Enter with the second factor: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 * num2
        resultado()
        pergunta = str(input('-->Want to do another operation? (y/n): '))
        if pergunta == 's':
         pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Invalid answer!!')
            break

    elif operacao == "division":
        os.system('cls')
        num1 = input('Enter with the dividend: ')
        num2 = input('Enter with the divider: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 / num2
        resultado()
        pergunta = str(input('-->Want to do another operation? (y/n): '))
        if pergunta == 's':
            pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Invalid answer!!')
            break

    elif operacao == "addition":
        os.system('cls')
        num1 = input('Enter with the first number: ')
        num2 = input('Enter with the second number: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 + num2
        resultado()
        pergunta = str(input('-->Want to do another operation? (y/n): '))
        if pergunta == 's':
            pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Invalid answer!!')
            break

    elif operacao == "subtraction":
        os.system('cls')
        num1 = input ('Enter with the first number: ')
        num2 = input ('Enter with the second number: ')
        invalido()
        num1 = int(num1)
        num2 = int(num2)
        x = num1 - num2
        os.system('cls')
        resultado()
        pergunta = str(input('-->Want to do another operation? (y/n): '))
        if pergunta == 's':
            pass
        elif pergunta == 'n':
            break
        else:
            print('[red]-->Invalid answer!!')
            break

    else:
        print('[red]-->Enter with a valid operation!!')
