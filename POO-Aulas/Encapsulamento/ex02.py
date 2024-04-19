# Implemente a classe Filme, com os atributos titulo e genero
# Todos os atributos devem ser privados
# Crie os métodos get e set para todos os atributos

# No seu programa principal, faça a seguinte implementação:
# - Criar uma lista de filmes vazia
# - Cadastrar 3 filmes (com os dados informados pelo usuário)
# - Armazenar os objetos na lista de filmes
# - Percorrer a lista de filmes e imprimir no terminal os dados de todos os filmes cadastrados



class Filmes:

    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo
    
    def get_genero(self):
        return self.__genero
    
    def set_titulo(self, titulo):
        newtitulo = input("Insira seu nome: ")
        self.__titulo = newtitulo

    def set_genero(self, genero):
        newgenero = input("Insira seu nome: ")
        self.__genero = newgenero

Filme = []

for i in range(3):

    nomtitulo = input("Digite o título do filme: ")
    nomgenero = input("Digite o gênero: ")
    Filme.append(Filmes(nomtitulo, nomgenero))
    i+=1

for g in range(len(Filme)):
    print(f"\033[31m--------------------------------------------------\033[0m")
    print(f"Nome do filme: {Filme[g].get_titulo()}")
    print(f"Gênero do filme: {Filme[g].get_genero()}")
    print(f"\033[31m--------------------------------------------------\033[0m")