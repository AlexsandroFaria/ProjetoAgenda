import mysql.connector
from _mysql_connector import MySQLInterfaceError


class CreateDatabase:

    criacao_database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rootalf",
        database=None
    )

    criacao_database2 = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="rootalf",
        database="db_agenda"
    )

    def criar_banco(self):
        try:
            cursor = self.criacao_database.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS db_agenda")
            print('Banco de dados Agenda criado com sucesso!')
        except MySQLInterfaceError as erro:
            print(erro)

    def criacao_tabela(self):
        cursor = self.criacao_database2.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS db_agenda.tb_agenda(
            id_agenda INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(255) NOT NULL,
            sobrenome VARCHAR(255) NOT NULL,
            endereco VARCHAR(255),
            numero int,
            complemento VARCHAR(255),
            bairro VARCHAR(255),
            uf  VARCHAR(2),
            data date,
            PRIMARY KEY(id_agenda)
        );                  
        """)
        print("Tabela criada com sucesso!")



