import getpass

from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QMessageBox
import pandas as pd
from components.mensagem import Mensagem
from dao.agenda_dao import AgendaDao
from model.agenda import Agenda
from view.ui_tela_visualizar_dados import Ui_VisualizarDados


class VisualizarDadosContatos(QMainWindow, Ui_VisualizarDados):
    def __init__(self):
        super(VisualizarDadosContatos, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Visualizar COntatos")
        self.setFixedSize(966, 500)

        self.mensagem = Mensagem()

        self.listar_contatos_tabela()
        self.btn_peswquisar_nome.clicked.connect(self.consultar_contato_nome)
        self.btn_gerar_relatorio.clicked.connect(self.gerar_relatorio)
        self.btn_fechar.clicked.connect(self.close)

    def listar_contatos_tabela(self):
        try:
            agenda_dao = AgendaDao()
            resultado = agenda_dao.listar_contatos_tabela()

            self.tabela_visualizar.setRowCount(len(resultado))
            self.tabela_visualizar.setColumnCount(9)

            for i in range(len(resultado)):
                for j in range(0, 9):
                    self.tabela_visualizar.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_erro_banco()

    def consultar_contato_nome(self):
        if self.txt_nome_pesquisa.text() == "":
            self.mensagem.mensagem_campo_vazio('pesquisar nome')
        else:
            agenda = Agenda()
            agenda.nome = self.txt_nome_pesquisa.text()

            try:
                agenda_dao = AgendaDao()
                resultado = agenda_dao.consulta_contato_nome(agenda.nome)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Consulta Contato")
                    msg.setText('Contato não encontrado!')
                    msg.exec_()

                    self.txt_nome_pesquisa.setText("")
                else:
                    self.tabela_visualizar.setRowCount(len(resultado))
                    self.tabela_visualizar.setColumnCount(9)

                    for i in range(len(resultado)):
                        for j in range(0, 9):
                            self.tabela_visualizar.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.txt_nome_pesquisa.setText("")

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_erro_banco()

    def gerar_relatorio(self):
        user_windows = getpass.getuser()

        try:
            agenda_dao = AgendaDao()
            resultado = agenda_dao.listar_contatos_tabela()

            dados = pd.DataFrame(resultado)
            dados.columns = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'Número', 'Complemento', 'Bairro', 'UF',
                             'Data Nascimento']
            dados.to_excel(f'c:\\Users\\{user_windows}\\Downloads\\Contatos Agenda.xlsx',
                           index=False)

            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Relatório de Contatos")
            msg.setText('Relatório Gerado com sucesso na pasta Downloads!')
            msg.exec_()
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_erro_banco()
