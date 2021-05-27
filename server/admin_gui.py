# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import json
from server import ServerProgram
from user_data_handler import UserDataHandler
from weather_data_handler import WeatherDataHandler

class AdminProgram(object):

    def Login(self, MainWindow, serverProgram):
        username = self.username_box.text()
        password = self.password_box.text()

        file = open("data/user_data.json", )
        data = json.load(file)
        if data[0]["username"] != username:
            file.close()
            QtWidgets.QMessageBox.about(MainWindow, "" , "Wrong admin username")
        elif data[0]["password"] != password:
            file.close()
            QtWidgets.QMessageBox.about(MainWindow, "" , "Wrong admin password")
        else:
            file.close()
            # Create a window allow admin update weather data

        pass


    def setupUi(self, MainWindow, serverProgram):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 261)

        self.WELCOME_label = QtWidgets.QLabel(MainWindow)
        self.WELCOME_label.setGeometry(QtCore.QRect(50, 10, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        self.WELCOME_label.setFont(font)
        self.WELCOME_label.setAlignment(QtCore.Qt.AlignCenter)
        self.WELCOME_label.setObjectName("WELCOME_label")

        self.username_box = QtWidgets.QLineEdit(MainWindow)
        self.username_box.setGeometry(QtCore.QRect(50, 80, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.username_box.setFont(font)
        self.username_box.setDragEnabled(True)
        self.username_box.setClearButtonEnabled(True)
        self.username_box.setObjectName("username_box")

        self.password_box = QtWidgets.QLineEdit(MainWindow)
        self.password_box.setGeometry(QtCore.QRect(50, 130, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.password_box.setFont(font)
        self.password_box.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_box.setDragEnabled(True)
        self.password_box.setClearButtonEnabled(True)
        self.password_box.setObjectName("password_box")

        self.login_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.Login(serverProgram))
        self.login_button.setGeometry(QtCore.QRect(120, 190, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.WELCOME_label.setText(_translate("MainWindow", "Welcome Admin"))
        self.username_box.setText(_translate("MainWindow", "Username"))
        self.password_box.setText(_translate("MainWindow", "Password"))
        self.login_button.setText(_translate("MainWindow", "Login"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = AdminProgram()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
