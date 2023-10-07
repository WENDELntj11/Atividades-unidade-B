class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = 'Disponivel'
class  Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livro_emprestados = []
class Bibliotecas:
    def __init__(self):
        self.livros = []
        self.membros = []
    def adicionar_livros(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)
    def adicionar_membros(self, nome):
        membro = Membro(nome)
        self.membros.append(membros):
    def empretar_livros(self, titulo_livros, nome_membros):
        for Livros in self.livros:
            if Livro.titulo == titulo_livros and Livros.status == 'Disponivel':
              for membro in self.membros:
                if membro.nome == nome_membros:
                    membro.livro_emprestados.append(Livros)
                    Livro.status = 'emprestados'
                    return 'O livro foi emprestados com sucesso!'
        return "Hoje nao foi possivel de emprestar o livro."
    
    def retornar_livros(self, tiutlo_livro, nome_membro):
        for membro in self.membros:
            if membro.nome == nome_membro:
                for livro in membro.livro_emprestados:
                    if livro.titulo == tiutlo_livro:
                        membro.status = "Disponivel"
                        return "Esse livro foi retornado com sucesso!"
        return " Infelizmente nao foi possivel retornar o livro."



      
        
        

