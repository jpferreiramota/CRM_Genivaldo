class Cliente():
    def __init__(self, nome, rua, bairro, numero, cep, telefone, email):
        self.id = 0
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.numero = numero
        self.cep = cep
        self.telefone = telefone
        self.email = email

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
