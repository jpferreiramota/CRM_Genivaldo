class Produto():
    def __init__(self, nome, qt_estoque,
                 preco, fabricante):
        self.id = 0
        self.nome = nome
        self.qt_estoque = qt_estoque
        self.preco = preco
        self.fabricante = fabricante



    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

