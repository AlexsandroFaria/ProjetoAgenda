from PySide6.QtWidgets import QApplication
import sys
from connection.create_database import CreateDatabase
from view.tela_agenda import TelaAgenda


def criacao_banco():
    criacao_banco = CreateDatabase()
    criacao_banco.criar_banco()
    criacao_banco.criacao_tabela()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tela_agenda = TelaAgenda()

    criacao_banco()

    tela_agenda.show()

    app.exec()



