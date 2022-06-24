from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QMainWindow, QMessageBox
from components.mensagem import Mensagem
from dao.agenda_dao import AgendaDao
from model.agenda import Agenda
from view.tela_visualizar_dados import VisualizarDadosContatos
from view.ui_agenda import Ui_Agenda
import datetime


class TelaAgenda(QMainWindow, Ui_Agenda):
    def __init__(self):
        super(TelaAgenda, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Agenda')
        self.setFixedSize(473, 594)

        self.mensagem = Mensagem()
        self.listar_contatos_tabela()
        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

        self.btn_limpar.clicked.connect(self.limpar_campos_formulario)
        self.btn_cadastrar.clicked.connect(self.cadastrar_contato_agenda)
        self.btn_alterar.clicked.connect(self.alterar_contato_agenda)
        self.btn_carregar.clicked.connect(self.carregar_campos_formulario)
        self.btn_excluir.clicked.connect(self.excluir_contato)
        self.btn_visualizar_dados.clicked.connect(self.abrir_tela_visualizar_dados_contatos)
        self.btn_fechar.clicked.connect(self.close)

    def carregar_campos_formulario(self):
        linha = self.tabela_agenda.currentRow()

        agenda_dao = AgendaDao()
        dados = agenda_dao.listar_contatos_tabela()

        valor_id = dados[linha][0]

        resultado = agenda_dao.consultar_contato_id(valor_id)

        self.txt_identificador.setText(str(resultado[0][0]))
        self.txt_nome.setText(str(resultado[0][1]))
        self.txt_sobrenome.setText(str(resultado[0][2]))
        self.txt_endereco.setText(str(resultado[0][3]))
        self.txt_numero.setText(str(resultado[0][4]))
        self.txt_complemento.setText(str(resultado[0][5]))
        self.txt_bairro.setText(str(resultado[0][6]))
        self.combo_uf.setCurrentText(str(resultado[0][7]))
        self.txt_data.setText(str(resultado[0][8]))

        self.btn_alterar.setEnabled(True)
        self.btn_excluir.setEnabled(True)

    def cadastrar_contato_agenda(self):
        if self.txt_nome.text() == "":
            self.mensagem.mensagem_campo_vazio('nome')
        elif self.txt_sobrenome.text() == "":
            self.mensagem.mensagem_campo_vazio('sobrenome')
        elif self.txt_endereco.text() == "":
            self.mensagem.mensagem_campo_vazio('endereço')
        elif not self.txt_numero.text().isdigit():
            self.mensagem.mensagem_campo_numerico('número')
        elif self.combo_uf.currentText() == "Selecionar":
            self.mensagem.mensagem_combo()
        elif self.txt_data.text() == "":
            self.mensagem.mensagem_campo_vazio('data')
        else:
            agenda = Agenda()

            agenda.nome = self.txt_nome.text()
            agenda.sobrenome = self.txt_sobrenome.text()
            agenda.endereco = self.txt_endereco.text()
            agenda.numero = self.txt_numero.text()
            agenda.complemento = self.txt_complemento.text()
            agenda.bairro = self.txt_bairro.text()
            agenda.uf = self.combo_uf.currentText()
            data = self.txt_data.text()

            agenda.data = datetime.datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')

            try:
                agenda_dao = AgendaDao()
                agenda_dao.cadastrar_contato_agenda(agenda.nome, agenda.sobrenome, agenda.endereco, agenda.numero,
                                                    agenda.complemento, agenda.bairro, agenda.uf, agenda.data)

                self.mensagem.mensagem_cadastro()
                self.limpar_campos_formulario()
                self.listar_contatos_tabela()

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_erro_banco()

    def alterar_contato_agenda(self):
        if self.txt_nome.text() == "":
            self.mensagem.mensagem_campo_vazio('nome')
        elif self.txt_sobrenome.text() == "":
            self.mensagem.mensagem_campo_vazio('sobrenome')
        elif self.txt_endereco.text() == "":
            self.mensagem.mensagem_campo_vazio('endereço')
        elif not self.txt_numero.text().isdigit():
            self.mensagem.mensagem_campo_numerico('número')
        elif self.combo_uf.currentText() == "Selecionar":
            self.mensagem.mensagem_combo()
        elif self.txt_data.text() == "":
            self.mensagem.mensagem_campo_vazio('data')
        else:
            agenda = Agenda()

            agenda.id_agenda = self.txt_identificador.text()
            agenda.nome = self.txt_nome.text()
            agenda.sobrenome = self.txt_sobrenome.text()
            agenda.endereco = self.txt_endereco.text()
            agenda.numero = self.txt_numero.text()
            agenda.complemento = self.txt_complemento.text()
            agenda.bairro = self.txt_bairro.text()
            agenda.uf = self.combo_uf.currentText()
            data = self.txt_data.text()

            agenda.data = datetime.datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')

            try:
                agenda_dao = AgendaDao()
                agenda_dao.alterar_contato_agenda(agenda.id_agenda, agenda.nome, agenda.sobrenome, agenda.endereco,
                                                  agenda.numero, agenda.complemento, agenda.bairro, agenda.uf,
                                                  agenda.data)

                self.mensagem.mensagem_alteracao()
                self.limpar_campos_formulario()
                self.listar_contatos_tabela()

            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_erro_banco()

    def listar_contatos_tabela(self):
        try:
            agenda_dao = AgendaDao()
            resultado = agenda_dao.listar_contatos_tabela()

            self.tabela_agenda.setRowCount(len(resultado))
            self.tabela_agenda.setColumnCount(8)

            for i in range(len(resultado)):
                for j in range(0, 8):
                    self.tabela_agenda.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError as con_erro:
            print(con_erro)
            self.mensagem.mensagem_erro_banco()

    def excluir_contato(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setWindowTitle("Exclusão de Solução")
        msg.setText("Tem certeza que deseja excluir a Solução?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            agenda = Agenda()
            agenda.id_agenda = self.txt_identificador.text()
            try:
                agenda_dao = AgendaDao()
                agenda_dao.excluir_contato(agenda.id_agenda)

                self.mensagem.mensagem_exclusao()
                self.listar_contatos_tabela()
                self.limpar_campos_formulario()
            except ConnectionError as con_erro:
                print(con_erro)
                self.mensagem.mensagem_erro_banco()

    def abrir_tela_visualizar_dados_contatos(self):
        self.tela_visualizar = VisualizarDadosContatos()
        self.tela_visualizar.show()

    def limpar_campos_formulario(self):
        self.txt_identificador.setText("")
        self.txt_nome.setText("")
        self.txt_sobrenome.setText("")
        self.txt_endereco.setText("")
        self.txt_numero.setText("")
        self.txt_complemento.setText("")
        self.txt_bairro.setText("")
        self.combo_uf.setCurrentText("Selecionar")
        self.txt_data.setText("")

        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)
