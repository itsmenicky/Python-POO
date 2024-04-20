# Crie uma hierarquia de classes Animal(atributos nome e idade),
# com as classes filhas Cachorro, Gato e Cavalo (todas com o método
# emitir_som); e a classe Veterinario.

# Os atributos em comum devem ficar na classe Animal.

# Os métodos emitir_som devem imprimir uma mensagem simulando a
# emissão do som do animal correspondente.

# A classe Veterinario deve conter o método examinar(), que recebe
# como entrada um objeto que representa um animal e, quando o animal
# for examinado, esse animal deve emitir o seu som.

# No programa principal, crie objetos dos 3 tipos de animais e
# execute o método que emite o som de cada um.

from abc import ABC


class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Veterinario(ABC):
    def examinar(self, animal):
        return animal.emitir_som()


class Cachorro(Animal):
    def emitir_som(self):
        print("exibe o som do cachorro")


class Gato(Animal):
    def emitir_som(self):
        print("exibe o som do gato")


class Cavalo(Animal):
    def emitir_som(self):
        print("exibe o som do cavalo")


dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro
vet.examinar(horse)       # exibe o som do cavalo
vet.examinar(cat)         # exibe o som do gato
