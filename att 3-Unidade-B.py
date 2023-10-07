class Animal:
    def _init_(self, nome, especie, idade, dieta, habitat):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = habitat

    def descricao(self):
        return f"{self.nome} é uma {self.especie} de {self.idade} anos que é tem uma  {self.dieta} e vive em {self.habitat}."

class Zoologico:
    def _init_(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, nome):
        self.animais = [animal for animal in self.animais if animal.nome != nome]

    def listar_animais(self):
        for animal in self.animais:
            print(animal.descricao())

    def buscar_por_especie(self, especie):
        return [animal for animal in self.animais if animal.especie == especie]

    def listar_por_habitat(self, habitat):
        return [animal for animal in self.animais if animal.habitat == habitat]