class Jogo:
    def _init_(self, nome, categoria, taxa_de_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_de_entrada = taxa_de_entrada
        self.id = id

    def _str_(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_de_entrada}, ID: {self.id}"

class Plataforma:
    def _init_(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        self.jogos = [jogo for jogo in self.jogos if jogo.id != id]

    def listar_jogos(self):
        for jogo in self.jogos:
            print(jogo)

    def _str_(self):
        return f"A plataforma possui esses {len(self.jogos)} jogos."