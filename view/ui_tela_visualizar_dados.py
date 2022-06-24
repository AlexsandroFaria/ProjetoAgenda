# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_tela_visualizar_dados.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_VisualizarDados(object):
    def setupUi(self, VisualizarDados):
        if not VisualizarDados.objectName():
            VisualizarDados.setObjectName(u"VisualizarDados")
        VisualizarDados.resize(966, 500)
        icon = QIcon()
        icon.addFile(u"_img/agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        VisualizarDados.setWindowIcon(icon)
        VisualizarDados.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.frame = QFrame(VisualizarDados)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 951, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.tabela_visualizar = QTableWidget(VisualizarDados)
        if (self.tabela_visualizar.columnCount() < 9):
            self.tabela_visualizar.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_visualizar.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tabela_visualizar.setObjectName(u"tabela_visualizar")
        self.tabela_visualizar.setGeometry(QRect(20, 160, 931, 281))
        self.tabela_visualizar.verticalHeader().setVisible(False)
        self.frame_2 = QFrame(VisualizarDados)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(40, 450, 921, 43))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.btn_gerar_relatorio = QPushButton(self.frame_2)
        self.btn_gerar_relatorio.setObjectName(u"btn_gerar_relatorio")
        self.btn_gerar_relatorio.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btn_gerar_relatorio.setFont(font1)
        self.btn_gerar_relatorio.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon1 = QIcon()
        icon1.addFile(u"_img/relatorio.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_relatorio.setIcon(icon1)
        self.btn_gerar_relatorio.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_gerar_relatorio)

        self.btn_fechar = QPushButton(self.frame_2)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(0, 30))
        self.btn_fechar.setFont(font1)
        self.btn_fechar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon2 = QIcon()
        icon2.addFile(u"_img/fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon2)
        self.btn_fechar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_fechar)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.groupBox = QGroupBox(VisualizarDados)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 70, 331, 81))
        self.groupBox.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_nome_pesquisa = QLineEdit(self.groupBox)
        self.txt_nome_pesquisa.setObjectName(u"txt_nome_pesquisa")
        self.txt_nome_pesquisa.setMinimumSize(QSize(0, 25))
        self.txt_nome_pesquisa.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.txt_nome_pesquisa)

        self.btn_peswquisar_nome = QPushButton(self.groupBox)
        self.btn_peswquisar_nome.setObjectName(u"btn_peswquisar_nome")
        self.btn_peswquisar_nome.setMinimumSize(QSize(0, 30))
        self.btn_peswquisar_nome.setFont(font1)
        self.btn_peswquisar_nome.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon3 = QIcon()
        icon3.addFile(u"_img/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_peswquisar_nome.setIcon(icon3)
        self.btn_peswquisar_nome.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_peswquisar_nome)


        self.retranslateUi(VisualizarDados)

        QMetaObject.connectSlotsByName(VisualizarDados)
    # setupUi

    def retranslateUi(self, VisualizarDados):
        VisualizarDados.setWindowTitle(QCoreApplication.translate("VisualizarDados", u"Form", None))
        self.label.setText(QCoreApplication.translate("VisualizarDados", u"Lista de Contatos", None))
        ___qtablewidgetitem = self.tabela_visualizar.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VisualizarDados", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_visualizar.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VisualizarDados", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_visualizar.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VisualizarDados", u"Sobrenome", None));
        ___qtablewidgetitem3 = self.tabela_visualizar.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VisualizarDados", u"Endere\u00e7o", None));
        ___qtablewidgetitem4 = self.tabela_visualizar.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VisualizarDados", u"N\u00famero", None));
        ___qtablewidgetitem5 = self.tabela_visualizar.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("VisualizarDados", u"Complemento", None));
        ___qtablewidgetitem6 = self.tabela_visualizar.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("VisualizarDados", u"Bairro", None));
        ___qtablewidgetitem7 = self.tabela_visualizar.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("VisualizarDados", u"UF", None));
        ___qtablewidgetitem8 = self.tabela_visualizar.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("VisualizarDados", u"Data de Nascimento", None));
        self.label_2.setText("")
        self.btn_gerar_relatorio.setText(QCoreApplication.translate("VisualizarDados", u"Gerar Relat\u00f3rio", None))
        self.btn_fechar.setText(QCoreApplication.translate("VisualizarDados", u"Fechar", None))
        self.label_3.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("VisualizarDados", u"Pesquisar por nome do Contato", None))
        self.btn_peswquisar_nome.setText(QCoreApplication.translate("VisualizarDados", u"Pesquisar", None))
    # retranslateUi

