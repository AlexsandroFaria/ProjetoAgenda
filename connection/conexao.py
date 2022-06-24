import mysql.connector


class Conexao:

    def __init__(self, host="localhost", user="root", pwd="rootalf", db="db_agenda"):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def conecta(self):
        self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.pwd, database=self.db)
        self.cur = self.con.cursor()

    def desconecta(self):
        self.con.close()

    def executar_consulta(self, sql):
        self.conecta()
        self.cur.execute(sql)
        resultado = self.cur.fetchall()
        self.desconecta()
        return resultado

    def executar_query(self, sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta()
