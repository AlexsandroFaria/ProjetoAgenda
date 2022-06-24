from PySide6 import QtGui
from PySide6.QtWidgets import QMessageBox


class Mensagem:

    def mensagem_campo_vazio(self, campo):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Campos em branco!")
        msg.setText(f'O campo {campo} não pode estar em branco!')
        msg.exec_()

    def mensagem_campo_numerico(self, campo):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Campo numérico!")
        msg.setText(f'O campo {campo} só pode conter números!')
        msg.exec_()

    def mensagem_combo(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Campos em branco!")
        msg.setText('Informe um valor válido no campo UF.')
        msg.exec_()

    def mensagem_erro_banco(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Erro de Conexão!")
        msg.setText('Erro de conexão com o banco. Tente novamente mais tarde.')
        msg.exec_()

    def mensagem_cadastro(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Cadastro de contato!")
        msg.setText('Contato cadastrado com sucesso!')
        msg.exec_()

    def mensagem_alteracao(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Alteração de contato!")
        msg.setText('Contato alterado com sucesso!')
        msg.exec_()

    def mensagem_exclusao(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/agenda.png"))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Exclusão de contato!")
        msg.setText('Contato excluidoo com sucesso!')
        msg.exec_()
