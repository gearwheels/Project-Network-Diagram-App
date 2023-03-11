# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_startWin(object):
    def setupUi(self, startWin):
        startWin.setObjectName("startWin")
        startWin.resize(1327, 844)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        startWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        startWin.setWindowIcon(icon)
        startWin.setAutoFillBackground(False)
        startWin.setStyleSheet("\n"
"#startWin{background-image: url(:/newPrefix/spaceBackground.png);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(startWin)
        self.verticalLayout.setContentsMargins(20, 5, 20, 10)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelWelcome = QtWidgets.QLabel(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.labelWelcome.setFont(font)
        self.labelWelcome.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.labelWelcome.setLineWidth(5)
        self.labelWelcome.setMidLineWidth(5)
        self.labelWelcome.setObjectName("labelWelcome")
        self.verticalLayout.addWidget(self.labelWelcome)
        self.labelPicture = QtWidgets.QLabel(startWin)
        self.labelPicture.setAutoFillBackground(False)
        self.labelPicture.setStyleSheet("image: url(:/newPrefix/logo_mca-min.png);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.labelPicture.setText("")
        self.labelPicture.setObjectName("labelPicture")
        self.verticalLayout.addWidget(self.labelPicture)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditGroup = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditGroup.setFont(font)
        self.lineEditGroup.setStyleSheet("background-color: #fffaea;")
        self.lineEditGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditGroup.setMaxLength(30)
        self.lineEditGroup.setObjectName("lineEditGroup")
        self.gridLayout.addWidget(self.lineEditGroup, 2, 1, 1, 1)
        self.labelGroup = QtWidgets.QLabel(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelGroup.setFont(font)
        self.labelGroup.setObjectName("labelGroup")
        self.gridLayout.addWidget(self.labelGroup, 2, 0, 1, 1)
        self.lineEditSurname = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditSurname.setFont(font)
        self.lineEditSurname.setStyleSheet("background-color: #fffaea;")
        self.lineEditSurname.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly)
        self.lineEditSurname.setMaxLength(200)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.gridLayout.addWidget(self.lineEditSurname, 0, 1, 1, 1)
        self.labelSurname = QtWidgets.QLabel(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelSurname.setFont(font)
        self.labelSurname.setStyleSheet("")
        self.labelSurname.setObjectName("labelSurname")
        self.gridLayout.addWidget(self.labelSurname, 0, 0, 1, 1)
        self.lineEditNumINGroup = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.lineEditNumINGroup.setFont(font)
        self.lineEditNumINGroup.setStyleSheet("background-color: #fffaea;")
        self.lineEditNumINGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditNumINGroup.setInputMask("")
        self.lineEditNumINGroup.setMaxLength(8)
        self.lineEditNumINGroup.setObjectName("lineEditNumINGroup")
        self.gridLayout.addWidget(self.lineEditNumINGroup, 1, 1, 1, 1)
        self.labelNumGroup = QtWidgets.QLabel(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.labelNumGroup.setFont(font)
        self.labelNumGroup.setObjectName("labelNumGroup")
        self.gridLayout.addWidget(self.labelNumGroup, 1, 0, 1, 1)
        self.btnSignLab = QtWidgets.QPushButton(startWin)
        self.btnSignLab.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.btnSignLab.setFont(font)
        self.btnSignLab.setAutoFillBackground(False)
        self.btnSignLab.setStyleSheet("color: rgb(234, 234, 234);\n"
"background-color: rgb(46, 101, 158);")
        self.btnSignLab.setCheckable(True)
        self.btnSignLab.setDefault(False)
        self.btnSignLab.setFlat(False)
        self.btnSignLab.setObjectName("btnSignLab")
        self.gridLayout.addWidget(self.btnSignLab, 3, 1, 1, 1)
        self.btnDeveloperMode = QtWidgets.QPushButton(startWin)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnDeveloperMode.setFont(font)
        self.btnDeveloperMode.setStyleSheet("color: rgb(234, 234, 234);\n"
"background-color: rgb(46, 101, 158);")
        self.btnDeveloperMode.setCheckable(True)
        self.btnDeveloperMode.setObjectName("btnDeveloperMode")
        self.gridLayout.addWidget(self.btnDeveloperMode, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 14)
        self.gridLayout.setColumnStretch(2, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 3)

        self.retranslateUi(startWin)
        QtCore.QMetaObject.connectSlotsByName(startWin)

    def retranslateUi(self, startWin):
        _translate = QtCore.QCoreApplication.translate
        startWin.setWindowTitle(_translate("startWin", "РЕГИСТРАЦИЯ"))
        self.labelWelcome.setText(_translate("startWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#e7e7e7;\">ПОСТРОЕНИЕ МЕТОДА СЕТЕВОГО ПЛАНИРОВАНИЯ И УПРАВЛЕНИЯ В </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; font-weight:600; color:#e7e7e7;\">ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССАХ ЭКСПЛУАТАЦИИ КОСМИЧЕСКИХ СРЕДСТВ</span></p></body></html>"))
        self.labelGroup.setText(_translate("startWin", "<html><head/><body><p><span style=\" font-weight:600; color:#e7e7e7;\">ВЗВОД</span></p></body></html>"))
        self.labelSurname.setText(_translate("startWin", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#e7e7e7;\">Ф.И.О.</span></p></body></html>"))
        self.labelNumGroup.setText(_translate("startWin", "<html><head/><body><p><span style=\" font-weight:600; color:#e7e7e7;\">ВАРИАНТ</span></p></body></html>"))
        self.btnSignLab.setText(_translate("startWin", "Начать работу"))
        self.btnDeveloperMode.setText(_translate("startWin", "Вход преподавателя"))
from qt_designer_ui.resources import backGround_rc
from qt_designer_ui.resources import labelMAI_rc
from qt_designer_ui.resources import labelVKAMoj_rc
from qt_designer_ui.resources import spaceBackground_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startWin = QtWidgets.QDialog()
    ui = Ui_startWin()
    ui.setupUi(startWin)
    startWin.show()
    sys.exit(app.exec_())
