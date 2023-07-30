class Usuario():
    def __init__(self, nome, senha, email, telefone):
        self.id = 0
        self.nome = nome
        self.senha = senha
        self.email = email
        self.telefone = telefone

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
