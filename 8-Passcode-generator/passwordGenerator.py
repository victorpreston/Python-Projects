# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
import random
import string

class Ui_MainWindow(object):
    def alertBox(self,title,message):
        window = QtWidgets.QMessageBox()
        window.setWindowTitle(title)
        window.setText(message)
        window.setStandardButtons(QtWidgets.QMessageBox.Ok)
        window.exec_()

    def generateRandomPassword(self):
        if self.passwordLimit.text()=="":
            self.alertBox('Blank Message','Please enter your password limit')
        else:
            num = int(self.passwordLimit.text())
            password = ""
            for n in range(num):
                limit = random.randint(1,90)
                password = password + string.printable[limit]
        self.passwordLimit.clear()
        return self.outputBox.setText(password)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        self.appTitle.setGeometry(QtCore.QRect(110, 20, 431, 51))
        self.appTitle.setStyleSheet("font-family:Calibri;\n"
"font-weight:bold;\n"
"font-size:28px;\n"
"color:white;")
        self.appTitle.setObjectName("appTitle")
        self.passwordLimitTitle = QtWidgets.QLabel(self.centralwidget)
        self.passwordLimitTitle.setGeometry(QtCore.QRect(110, 90, 431, 51))
        self.passwordLimitTitle.setStyleSheet("font-family:Calibri;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"color:white;")
        self.passwordLimitTitle.setObjectName("passwordLimitTitle")
        self.passwordLimit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLimit.setGeometry(QtCore.QRect(110, 140, 431, 41))
        self.passwordLimit.setStyleSheet("font-family:Calibri;\n"
"font-weight:bold;\n"
"padding:8x;\n"
"font-size:18px;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:8px;")
        self.passwordLimit.setObjectName("passwordLimit")
        self.passwordLimit.setValidator(QIntValidator(1,99))
        self.generatePasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.generatePasswordButton.clicked.connect(self.generateRandomPassword)
        self.generatePasswordButton.setGeometry(QtCore.QRect(110, 220, 431, 41))
        self.generatePasswordButton.setStyleSheet("background-color:orange;\n"
"color:white;\n"
"font-family:Calibri;\n"
"font-weight:bold;\n"
"font-size:20px;\n"
"border-radius:8px;\n"
"")
        self.generatePasswordButton.setObjectName("generatePasswordButton")
        self.outputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.outputBox.setGeometry(QtCore.QRect(110, 310, 431, 41))
        self.outputBox.setStyleSheet("font-family:Calibri;\n"
"font-weight:bold;\n"
"padding:8x;\n"
"font-size:18px;\n"
"color:white;\n"
"border:2px solid white;\n"
"border-radius:8px;")
        self.outputBox.setObjectName("outputBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Strong Random Password Generator"))
        self.appTitle.setText(_translate("MainWindow", "Strong Random Password Generator"))
        self.passwordLimitTitle.setText(_translate("MainWindow", "Enter your password limit"))
        self.generatePasswordButton.setText(_translate("MainWindow", "Generate Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
