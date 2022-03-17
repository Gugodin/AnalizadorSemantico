from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(656, 287)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 261, 20))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 130, 471, 20))
        font1 = QFont()
        font1.setPointSize(9)
        self.lineEdit.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(230, 70, 201, 20))
        font2 = QFont()
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.message = QLabel(self.centralwidget)
        self.message.setObjectName(u"message")
        self.message.setGeometry(QRect(180, 230, 311, 21))
        self.message.setFont(font2)
        self.message.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 170, 75, 23))
        self.pushButton.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ANALIZADOR SINTACTICO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Escriba el comando de linux:", None))
        self.message.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Comprobar", None))
    # retranslateUi

