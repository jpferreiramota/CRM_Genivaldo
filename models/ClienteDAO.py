class ClienteDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, cliente):
        try:
            sql = "INSERT INTO Cliente(nome, " \
                  "rua, bairro, numero, cep, telefone, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (cliente.nome, cliente.rua,
                                 cliente.bairro, cliente.numero, cliente.cep, cliente.telefone, cliente.email))
            self.con.commit()
            codigo = cursor.lastrowid
            return codigo
        except:
            return 0


    def buscar(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM Cliente WHERE id=%s"
            cursor.execute(sql, (id,))
            cliente = cursor.fetchone()
            return cliente
        except:
            return 0


    def listar(self, id=None):
        try:
            cursor = self.con.cursor()
            if id != None:
                # pegar somente uma cliente
                sql = "SELECT * FROM Cliente WHERE id=%s"
                cursor.execute(sql, (id,))
                clientes = cursor.fetchone()
                return clientes
            else:
                # pegar todas as clientes
                sql = "SELECT * FROM Cliente WHERE id>0"
                cursor.execute(sql)
                clientes = cursor.fetchall()
                return clientes
        except:
            return None

    def atualizar(self, cliente):
        try:
            sql = "UPDATE Cliente " \
                  "SET nome=%s, rua=%s, bairro=%s, cep=%s, numero=%s, telefone=%s, email=%s WHERE id=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (cliente.nome, cliente.rua, cliente.bairro,
                                 cliente.cep, cliente.numero, cliente.telefone, cliente.email, cliente.id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0

















