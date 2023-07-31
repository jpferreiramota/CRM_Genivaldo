class UsuarioDAO():
    def __init__(self, con):
        self.con = con

    # CRUD - Create, Retrieve, Update, Delete
    def inserir(self, usuario):
        try:
            sql = "INSERT INTO Usuario(nome, senha, " \
                  "email, telefone) VALUES (%s, %s, %s, %s)"

            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.nome, usuario.senha, usuario.email, usuario.telefone))
            self.con.commit()

            codigo = cursor.lastrowid
            return codigo
        except:
            return 0

    def autenticar(self, email, senha):
        try:
            sql = "SELECT * FROM Usuario WHERE email=%s AND senha=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (email, senha))

            Usuario = cursor.fetchone()  # lastrowid, fetchone, fetchall
            return  Usuario
        except:
            return None

    def listar(self, id=None):
        try:
            cursor = self.con.cursor()
            if id != None:
                # pegar somente um usuário
                sql = "SELECT * FROM Usuario WHERE id=%s"
                cursor.execute(sql, (id,))
                Usuario = cursor.fetchone()
                return Usuario
            else:
                # pegar todas os usuários
                sql = "SELECT * FROM Usuario"
                cursor.execute(sql)
                Usuarios = cursor.fetchall()
                return Usuarios
        except:
            return None

    def atualizar(self, usuario):
        try:
            sql = "UPDATE Usuario SET nome=%s, email=%s, telefone=%s WHERE id=%s"

            cursor = self.con.cursor()
            cursor.execute(sql, (usuario.nome, usuario.email, usuario.telefone, usuario.id))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0

    def buscar(self, id):
        try:
            cursor = self.con.cursor()
            sql = "SELECT * FROM Usuario WHERE id=%s"
            cursor.execute(sql, (id,))
            Usuario = cursor.fetchone()
            return Usuario
        except:
            return 0

    def excluir(self, id):
        try:
            sql = "DELETE FROM Usuario WHERE id = %s"
            cursor = self.con.cursor()
            cursor.execute(sql, (id,))
            self.con.commit()
            return cursor.rowcount
        except:
            return 0













