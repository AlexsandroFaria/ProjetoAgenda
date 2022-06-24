# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_agenda.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Agenda(object):
    def setupUi(self, Agenda):
        if not Agenda.objectName():
            Agenda.setObjectName(u"Agenda")
        Agenda.resize(473, 594)
        icon = QIcon()
        icon.addFile(u"_img/agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        Agenda.setWindowIcon(icon)
        Agenda.setStyleSheet(u"background-color: rgb(193, 193, 255);")
        self.centralwidget = QWidget(Agenda)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 100, 71, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 140, 101, 16))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 81, 16))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 220, 81, 16))
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(210, 220, 91, 20))
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 260, 81, 16))
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_uf = QComboBox(self.centralwidget)
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.addItem("")
        self.combo_uf.setObjectName(u"combo_uf")
        self.combo_uf.setGeometry(QRect(310, 260, 141, 25))
        self.combo_uf.setMinimumSize(QSize(0, 25))
        self.combo_uf.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 260, 47, 13))
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 300, 61, 16))
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_nome = QLineEdit(self.centralwidget)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(120, 100, 331, 25))
        self.txt_nome.setMinimumSize(QSize(0, 25))
        self.txt_nome.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_sobrenome = QLineEdit(self.centralwidget)
        self.txt_sobrenome.setObjectName(u"txt_sobrenome")
        self.txt_sobrenome.setGeometry(QRect(120, 140, 331, 25))
        self.txt_sobrenome.setMinimumSize(QSize(0, 25))
        self.txt_sobrenome.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_endereco = QLineEdit(self.centralwidget)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setGeometry(QRect(120, 180, 331, 25))
        self.txt_endereco.setMinimumSize(QSize(0, 25))
        self.txt_endereco.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_numero = QLineEdit(self.centralwidget)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setGeometry(QRect(120, 220, 81, 25))
        self.txt_numero.setMinimumSize(QSize(0, 25))
        self.txt_numero.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_complemento = QLineEdit(self.centralwidget)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setGeometry(QRect(310, 220, 141, 25))
        self.txt_complemento.setMinimumSize(QSize(0, 25))
        self.txt_complemento.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_bairro = QLineEdit(self.centralwidget)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(120, 260, 81, 25))
        self.txt_bairro.setMinimumSize(QSize(0, 25))
        self.txt_bairro.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_data = QLineEdit(self.centralwidget)
        self.txt_data.setObjectName(u"txt_data")
        self.txt_data.setGeometry(QRect(120, 300, 81, 25))
        self.txt_data.setMinimumSize(QSize(0, 25))
        self.txt_data.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border: 1px solid  gray;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.txt_data.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 330, 451, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cadastrar = QPushButton(self.frame)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy)
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setBold(True)
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon1 = QIcon()
        icon1.addFile(u"_img/salvar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon1)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_alterar = QPushButton(self.frame)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 30))
        self.btn_alterar.setFont(font1)
        self.btn_alterar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon2 = QIcon()
        icon2.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon2)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setFont(font1)
        self.btn_excluir.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon3 = QIcon()
        icon3.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon3)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_fechar = QPushButton(self.frame)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(0, 30))
        self.btn_fechar.setFont(font1)
        self.btn_fechar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon4 = QIcon()
        icon4.addFile(u"_img/fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon4)
        self.btn_fechar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_fechar)

        self.tabela_agenda = QTableWidget(self.centralwidget)
        if (self.tabela_agenda.columnCount() < 9):
            self.tabela_agenda.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_agenda.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tabela_agenda.setObjectName(u"tabela_agenda")
        self.tabela_agenda.setGeometry(QRect(10, 390, 451, 121))
        self.tabela_agenda.verticalHeader().setVisible(False)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 520, 451, 52))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_carregar = QPushButton(self.frame_2)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 30))
        self.btn_carregar.setFont(font1)
        self.btn_carregar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon5 = QIcon()
        icon5.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon5)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_carregar)

        self.btn_visualizar_dados = QPushButton(self.frame_2)
        self.btn_visualizar_dados.setObjectName(u"btn_visualizar_dados")
        self.btn_visualizar_dados.setMinimumSize(QSize(0, 30))
        self.btn_visualizar_dados.setFont(font1)
        self.btn_visualizar_dados.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon6 = QIcon()
        icon6.addFile(u"_img/visualizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_visualizar_dados.setIcon(icon6)
        self.btn_visualizar_dados.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_visualizar_dados)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 0, 451, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.btn_limpar = QPushButton(self.centralwidget)
        self.btn_limpar.setObjectName(u"btn_limpar")
        self.btn_limpar.setGeometry(QRect(310, 290, 141, 31))
        self.btn_limpar.setMinimumSize(QSize(0, 30))
        self.btn_limpar.setFont(font1)
        self.btn_limpar.setMouseTracking(False)
        self.btn_limpar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        icon7 = QIcon()
        icon7.addFile(u"_img/limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar.setIcon(icon7)
        self.btn_limpar.setIconSize(QSize(24, 24))
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(6, 60, 91, 20))
        self.label_10.setFont(font)
        self.txt_identificador = QLineEdit(self.centralwidget)
        self.txt_identificador.setObjectName(u"txt_identificador")
        self.txt_identificador.setEnabled(False)
        self.txt_identificador.setGeometry(QRect(120, 60, 71, 25))
        self.txt_identificador.setMinimumSize(QSize(0, 25))
        self.txt_identificador.setStyleSheet(u"border: 1px solid  gray;\n"
"border-radius: 5px\n"
"")
        Agenda.setCentralWidget(self.centralwidget)

        self.retranslateUi(Agenda)

        QMetaObject.connectSlotsByName(Agenda)
    # setupUi

    def retranslateUi(self, Agenda):
        Agenda.setWindowTitle(QCoreApplication.translate("Agenda", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("Agenda", u"Nome:*", None))
        self.label_3.setText(QCoreApplication.translate("Agenda", u"Sobrenome:*", None))
        self.label_4.setText(QCoreApplication.translate("Agenda", u"Endere\u00e7o:*", None))
        self.label_5.setText(QCoreApplication.translate("Agenda", u"N\u00famero:*", None))
        self.label_6.setText(QCoreApplication.translate("Agenda", u"Complemento:", None))
        self.label_7.setText(QCoreApplication.translate("Agenda", u"Bairro:", None))
        self.combo_uf.setItemText(0, QCoreApplication.translate("Agenda", u"Selecionar", None))
        self.combo_uf.setItemText(1, QCoreApplication.translate("Agenda", u"RO", None))
        self.combo_uf.setItemText(2, QCoreApplication.translate("Agenda", u"AC", None))
        self.combo_uf.setItemText(3, QCoreApplication.translate("Agenda", u"AM", None))
        self.combo_uf.setItemText(4, QCoreApplication.translate("Agenda", u"RR", None))
        self.combo_uf.setItemText(5, QCoreApplication.translate("Agenda", u"PA", None))
        self.combo_uf.setItemText(6, QCoreApplication.translate("Agenda", u"AP", None))
        self.combo_uf.setItemText(7, QCoreApplication.translate("Agenda", u"TO", None))
        self.combo_uf.setItemText(8, QCoreApplication.translate("Agenda", u"MA", None))
        self.combo_uf.setItemText(9, QCoreApplication.translate("Agenda", u"PI", None))
        self.combo_uf.setItemText(10, QCoreApplication.translate("Agenda", u"CE", None))
        self.combo_uf.setItemText(11, QCoreApplication.translate("Agenda", u"RN", None))
        self.combo_uf.setItemText(12, QCoreApplication.translate("Agenda", u"PB", None))
        self.combo_uf.setItemText(13, QCoreApplication.translate("Agenda", u"PE", None))
        self.combo_uf.setItemText(14, QCoreApplication.translate("Agenda", u"AL", None))
        self.combo_uf.setItemText(15, QCoreApplication.translate("Agenda", u"SE", None))
        self.combo_uf.setItemText(16, QCoreApplication.translate("Agenda", u"BA", None))
        self.combo_uf.setItemText(17, QCoreApplication.translate("Agenda", u"MG", None))
        self.combo_uf.setItemText(18, QCoreApplication.translate("Agenda", u"ES", None))
        self.combo_uf.setItemText(19, QCoreApplication.translate("Agenda", u"RJ", None))
        self.combo_uf.setItemText(20, QCoreApplication.translate("Agenda", u"SP", None))
        self.combo_uf.setItemText(21, QCoreApplication.translate("Agenda", u"PR", None))
        self.combo_uf.setItemText(22, QCoreApplication.translate("Agenda", u"SC", None))
        self.combo_uf.setItemText(23, QCoreApplication.translate("Agenda", u"RS", None))
        self.combo_uf.setItemText(24, QCoreApplication.translate("Agenda", u"MS", None))
        self.combo_uf.setItemText(25, QCoreApplication.translate("Agenda", u"MT", None))
        self.combo_uf.setItemText(26, QCoreApplication.translate("Agenda", u"GO", None))
        self.combo_uf.setItemText(27, QCoreApplication.translate("Agenda", u"DF", None))

        self.label_8.setText(QCoreApplication.translate("Agenda", u"UF:*", None))
        self.label_9.setText(QCoreApplication.translate("Agenda", u"Data:*", None))
        self.txt_data.setInputMask(QCoreApplication.translate("Agenda", u"##/##/####", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("Agenda", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("Agenda", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("Agenda", u"Excluir", None))
        self.btn_fechar.setText(QCoreApplication.translate("Agenda", u"Fechar", None))
        ___qtablewidgetitem = self.tabela_agenda.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Agenda", u"Identificador", None));
        ___qtablewidgetitem1 = self.tabela_agenda.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Agenda", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_agenda.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Agenda", u"Sobrenome", None));
        ___qtablewidgetitem3 = self.tabela_agenda.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Agenda", u"Endere\u00e7o", None));
        ___qtablewidgetitem4 = self.tabela_agenda.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Agenda", u"N\u00famero", None));
        ___qtablewidgetitem5 = self.tabela_agenda.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Agenda", u"Complemento", None));
        ___qtablewidgetitem6 = self.tabela_agenda.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Agenda", u"Bairro", None));
        ___qtablewidgetitem7 = self.tabela_agenda.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Agenda", u"UF", None));
        ___qtablewidgetitem8 = self.tabela_agenda.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Agenda", u"Data", None));
        self.btn_carregar.setText(QCoreApplication.translate("Agenda", u"Carregar", None))
        self.btn_visualizar_dados.setText(QCoreApplication.translate("Agenda", u"Visualizar Dados", None))
        self.label.setText(QCoreApplication.translate("Agenda", u"Agenda de Contatos", None))
        self.btn_limpar.setText(QCoreApplication.translate("Agenda", u"Limpar", None))
        self.label_10.setText(QCoreApplication.translate("Agenda", u"Identificador:", None))
    # retranslateUi

