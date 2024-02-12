from PyQt5 import QtCore, QtGui, QtWidgets


class PA_Root(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("/*Main Window*/\n"
"/*Central Widget*/\n"
"#centralwidget{\n"
"    background-image: url(./pics/bc6.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"}\n"
"#Action{\n"
"    background-image: url(./pics/bc6.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"}\n"
"#Home{\n"
"    background-image: url(./pics/bc9.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"}\n"
"#stt{\n"
"    background: transparent;\n"
"    color: cyan;\n"
"}\n"
"#stt:hover{\n"
"    background: transparent;\n"
"    color: lime;\n"
"}\n"
"#stt:pressed{\n"
"    background: transparent;\n"
"    color: blue;\n"
"}\n"
"#version_h{\n"
"    color: white;\n"
"}\n"
"#pic_cont{\n"
"    background-image: url(./pics/TEXT.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"}\n"
"#qtb{\n"
"    background-image: url(./pics/btn_login3.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#qtb:hover{\n"
"    background-image: url(./pics/btn_login2.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#qtb:pressed{\n"
"    background-image: url(./pics/btn_login.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#browse_btn{\n"
"    background-image: url(./pics/btn_login.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#browse_btn:hover{\n"
"    background-image: url(./pics/btn_login3.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#browse_btn:pressed{\n"
"    background-image: url(./pics/btn_login4.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#browse_lbl{\n"
"    border: 5px solid blue;\n"
"    border-radius: 30px;\n"
"}\n"
"#browse_txt{\n"
"    background: transparent;\n"
"    border: none;\n"
"    border-bottom: 5px solid lime;\n"
"    padding: 10px;\n"
"}\n"
"#status{\n"
"    border: 5px solid blue;\n"
"    border-radius: 30px;\n"
"}\n"
"#stt_conv{\n"
"    background-image: url(./pics/btn_login4.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#stt_conv:hover{\n"
"    background-image: url(./pics/btn_login.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#stt_conv:pressed{\n"
"    background-image: url(./pics/btn_login3.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center center;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"/**********************************/\n"
"#back_btn{\n"
"    background-color: red;\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#back_btn:hover{\n"
"    background-color: rgb(255, 165, 138);\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}\n"
"#back_btn:pressed{\n"
"    background-color: rgb(253, 255, 115);\n"
"    border: none;\n"
"    border-radius: 30px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.stt = QtWidgets.QPushButton(self.Home)
        self.stt.setGeometry(QtCore.QRect(370, 420, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.stt.setFont(font)
        self.stt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stt.setObjectName("stt")
        self.version_h = QtWidgets.QLabel(self.Home)
        self.version_h.setGeometry(QtCore.QRect(220, 120, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.version_h.setFont(font)
        self.version_h.setObjectName("version_h")
        self.pic_cont = QtWidgets.QFrame(self.Home)
        self.pic_cont.setGeometry(QtCore.QRect(200, 170, 351, 241))
        self.pic_cont.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pic_cont.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pic_cont.setObjectName("pic_cont")
        self.qtb = QtWidgets.QPushButton(self.Home)
        self.qtb.setGeometry(QtCore.QRect(10, 20, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.qtb.setFont(font)
        self.qtb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.qtb.setObjectName("qtb")
        self.stackedWidget.addWidget(self.Home)
        self.Action = QtWidgets.QWidget()
        self.Action.setObjectName("Action")
        self.stt_conv = QtWidgets.QPushButton(self.Action)
        self.stt_conv.setGeometry(QtCore.QRect(20, 420, 741, 71))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.stt_conv.setFont(font)
        self.stt_conv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stt_conv.setObjectName("stt_conv")
        self.browse_btn = QtWidgets.QPushButton(self.Action)
        self.browse_btn.setGeometry(QtCore.QRect(440, 140, 331, 91))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.browse_btn.setFont(font)
        self.browse_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_btn.setObjectName("browse_btn")
        self.browse_lbl = QtWidgets.QLabel(self.Action)
        self.browse_lbl.setGeometry(QtCore.QRect(10, 70, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.browse_lbl.setFont(font)
        self.browse_lbl.setObjectName("browse_lbl")
        self.browse_txt = QtWidgets.QLineEdit(self.Action)
        self.browse_txt.setGeometry(QtCore.QRect(240, 80, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.browse_txt.setFont(font)
        self.browse_txt.setObjectName("browse_txt")
        self.status = QtWidgets.QLabel(self.Action)
        self.status.setGeometry(QtCore.QRect(10, 270, 761, 111))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.back_btn = QtWidgets.QPushButton(self.Action)
        self.back_btn.setGeometry(QtCore.QRect(20, 500, 741, 71))
        font = QtGui.QFont()
        font.setFamily("Vazir")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setObjectName("back_btn")
        self.stackedWidget.addWidget(self.Action)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF To Audio"))
        self.stt.setText(_translate("MainWindow", "Start"))
        self.version_h.setText(_translate("MainWindow", "version : 1.0.0"))
        self.qtb.setText(_translate("MainWindow", "Quit"))
        self.stt_conv.setText(_translate("MainWindow", "Start Converting"))
        self.browse_btn.setText(_translate("MainWindow", "Browse PDF..."))
        self.browse_lbl.setText(_translate("MainWindow", "Browse PDF File :"))
        self.browse_txt.setPlaceholderText(_translate("MainWindow", "Browse And Choose Your PDF File..."))
        self.status.setText(_translate("MainWindow", "Status: "))
        self.back_btn.setText(_translate("MainWindow", "Back To Home"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
