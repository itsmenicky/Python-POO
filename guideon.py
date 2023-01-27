import os
import time
import pyttsx3
from pytube import YouTube
from playsound import playsound
from pathlib import Path
from os.path import getmtime
import moviepy.editor as mp
import re
import pathlib
import glob
import speech_recognition as sr
from datetime import date

r = sr.Recognizer()
m = sr.Microphone()

def getMic():
    with m as source: r.adjust_for_ambient_noise(source)
    with m as source: audio = r.listen(source)
    print('Ok! Lendo o que você disse...')
    try:
        value = r.recognize_google(audio, language='pt-BR')
        os.system('cls')
        return value
    except sr.UnknownValueError:
        print('Erro aí seu troxa')
        os.system('cls')
        value = input('Não entendi o que você disse. Por favor, digite no console: ')
        return value


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", "brazil")
    engine.setProperty("rate", 210)
    engine.setProperty("volume", 1)

    engine.say(audio)
    engine.runAndWait()

#Guideon STORAGE
if not os.path.isdir("C:/Guideon"):
    os.mkdir('C:\Guideon')

if not os.path.isdir("C:/Guideon/Info"):
    os.mkdir("C:\Guideon\Info")
if not os.path.isdir('C:/Guideon/Texts'):
    os.mkdir('C:/Guideon/Texts')

Username = "C:/Guideon/Info/name.txt"

if os.path.exists(Username):
    with open(Username) as file:
        name = file.read()
else:
    name = None

if not name:
    with open(Username,'w') as file:
        os.system("cls")
        speak("Olá! Como posso chamar você??")

        userName = getMic()

        name = userName
        if name.isdigit():
            os.system("cls")
            speak("Heyy...sem números...me diga seu nome")
            
        else:
         file.write(name)
         speak("Olá " + name + " meu nome é Guideon...é um prazer conhecer você!")
         time.sleep(2)
else:

     log = 'C:/Guideon/Info/log.txt'

     if os.path.exists(log):
      with open(log) as file:
         lastAccess = file.read()
     
     else:
      with open(log, 'w') as file:
        recentLog = date.today()
        dayLog = recentLog.day
        monthLog = recentLog.month
        yearLog = recentLog.year
        if monthLog == 1:
          monthLog = 'janeiro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
        elif monthLog == 2:
          monthLog = 'fevereiro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
       
        elif monthLog == 3:
          monthLog = 'março'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 4:
          monthLog = 'abril'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 5:
          monthLog = 'maio'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 6:
          monthLog = 'junho'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 7:
          monthLog = 'julho'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 8:
          monthLog = 'agosto'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 9:
          monthLog = 'setembro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 10:
          monthLog = 'outubro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 11:
          monthLog = 'novembro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        else:
          monthLog = 'dezembro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')

     os.system("cls")
     speak("Olá de novo " + name)

     data_atual = date.today()
     dia = data_atual.day
     mes = data_atual.month
     ano = data_atual.year
     
     if mes == 1:
       mes = 'janeiro'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')
      
     elif mes == 2:
       mes = 'fevereiro'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 3:
       mes = 'março'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 4:
       mes = 'abril'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 5:
       mes = 'maio'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 6:
       mes = 'junho'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 7:
       mes = 'julho'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 8:
       mes = 'agosto'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 9:
       mes = 'setembro'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 10:
       mes = 'outubro'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     elif mes == 11:
       mes = 'novembro'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     else:
       mes = 'dezembro'
       speak(f'hoje é dia {dia} de {mes} de {ano}')
       with open(log) as file:
        speak(f'nos falamos pela última vez no {lastAccess}')

     with open(log, 'w') as file:
        recentLog = date.today()
        dayLog = recentLog.day
        monthLog = recentLog.month
        yearLog = recentLog.year
        if monthLog == 1:
          monthLog = 'janeiro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
        elif monthLog == 2:
          monthLog = 'fevereiro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
       
        elif monthLog == 3:
          monthLog = 'março'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 4:
          monthLog = 'abril'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 5:
          monthLog = 'maio'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 6:
          monthLog = 'junho'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 7:
          monthLog = 'julho'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 8:
          monthLog = 'agosto'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 9:
          monthLog = 'setembro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 10:
          monthLog = 'outubro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        elif monthLog == 11:
          monthLog = 'novembro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
          
        else:
          monthLog = 'dezembro'
          file.write(f'dia {dayLog} de {monthLog} de {yearLog}')
       

while True:

    os.system("cls")

    speak(f"Como posso te ajudar {name}?")

    print(f'-PAINEL DE OPÇÕES-\n\n--->Baixe uma música\n--->Texto\n--->Ajuda\n--->Sair')

    userQuote1 = getMic()
    

    if userQuote1 == "baixe uma música":

        os.system("cls")
        speak("Ok. Insira o link da música no console e irei buscá-la para você")
        link = input("-> ")
        yt = YouTube(link)
        speak("Insira o caminho onde eu devo salvar a música...")
        path = input("-> ")
        print("Baixando...")
        ys = yt.streams.filter(only_audio=True).first().download(path)
        print("Download completo!")
        print('Convertendo arquivo...')
        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        print('Sucesso!')
        os.system("cls")
        directory = Path(path)
        files = directory.glob('*.mp3')
        recentFile = max(files, key=getmtime)
        #playsound(recentFile)
        
        speak("Sua música já foi baixada no lugar escolhido. Diga 'painel' para acessar o Painel de Funções novamente, ou 'sair' para fechar o assistente... ")
        
        userOption1 = getMic()

        if userOption1 == "painel":
            pass

        elif userOption1 == "sair":
            os.system("cls")
            speak("Até a próxima " + name)
            
            exit()
        


    elif userQuote1 == "texto" or userQuote1 == "textu" or userQuote1 == "testo" or userQuote1 == "testu":
        os.system("cls")
        speak("Oque deseja fazer?")
        
        print("O que você deseja?\n--->Criar texto\n--->Editar texto\n--->Ler texto\n\n-> ")

        userFunction1 = getMic()

        if userFunction1 == "criar texto":
            os.system('cls')
            speak("Qual será o nome do texto?: ")
            
            nameFile = input("-> ")
            arquivo = f"C:/Guideon/Texts/{nameFile}.txt"

            if os.path.exists(arquivo):
                speak("Já existe um arquivo de texto salvo com este nome")
                
            else:
                with open(arquivo, 'w') as file:
                    os.system("cls")
                    speak("Escreva seu texto..")
                    
                    STT = getMic()
                    Texto = STT
                    file.write(Texto)
                    print("Texto salvo")
                    time.sleep(2)

        elif userFunction1 == "editar texto":
            speak("Qual o nome do arquivo de texto que deseja editar?")
            nameFile = input("-> ")
            textFile = f"C:/Guideon/Texts/{nameFile}.txt"
            
            if os.path.exists(textFile):
                with open(textFile, 'w') as file:
                   os.system('cls')
                   speak("Insira o novo texto")

                   STT_Editor = getMic()
                   newText = STT_Editor
                   file.write(newText)
                   print("Texto salvo")
                   time.sleep(2)

        elif userFunction1 == "ler texto" or userFunction1 == "er texto" or userFunction1 == "er testo" or userFunction1 == "er testu" or userFunction1 == "er textu" or userFunction1 == "ler texto" or userFunction1 == "ler testo" or userFunction1 == "ler testu" or userFunction1 == "ler textu":
            nameFile = input("Qual o nome do texto?: ")
            diretorio = pathlib.Path("C:/Guideon/Texts")
            if os.path.exists(f'C:/Guideon/Texts/{nameFile}.txt'):
                for file in diretorio.glob(f'{nameFile}.txt'):
                    for line in open(file):
                        speak(line)
            if not os.path.exists(f"C:/Guideon/Texts/{nameFile}.txt"):
                speak('não há nenhum texto salvo com este nome')

    elif userQuote1 == "ajuda":
     speak("\nIrei te auxiliar da melhor forma possível "+ name +"...Eu sou uma assistente em construção, tendo como funções armazenar Textos, ler Textos, editar Textos e baixar músicas do YouTube. Para que eu faça algumas destas funções, basta digitar no painel de funções alguma das disponíveis.")
     

     speak("Diga painel para acessar o Painel de Funções, ou sair para fechar o assistente...")
     

     userOption2 = getMic()

     if userOption2 == "painel":
         pass

     elif userOption2 == "sair":
         os.system("cls")
         speak("Até a próxima " + name)
         
         exit()

    elif userQuote1 == "sair":
      os.system("cls")
      speak("Até a próxima " + name)
      
      exit()
