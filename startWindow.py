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
        startWin.resize(1328, 853)
        self.verticalLayout = QtWidgets.QVBoxLayout(startWin)
        self.verticalLayout.setContentsMargins(20, 5, 20, 10)
        self.verticalLayout.setSpacing(25)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelWelcome = QtWidgets.QLabel(startWin)
        self.labelWelcome.setLineWidth(5)
        self.labelWelcome.setMidLineWidth(5)
        self.labelWelcome.setObjectName("labelWelcome")
        self.verticalLayout.addWidget(self.labelWelcome)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.labelSurname = QtWidgets.QLabel(startWin)
        self.labelSurname.setObjectName("labelSurname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSurname)
        self.lineEditSurname = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditSurname.setFont(font)
        self.lineEditSurname.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly)
        self.lineEditSurname.setMaxLength(25)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditSurname)
        self.labelName = QtWidgets.QLabel(startWin)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly)
        self.lineEditName.setMaxLength(25)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelNumGroup = QtWidgets.QLabel(startWin)
        self.labelNumGroup.setObjectName("labelNumGroup")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelNumGroup)
        self.lineEditNumINGroup = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditNumINGroup.setFont(font)
        self.lineEditNumINGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditNumINGroup.setInputMask("")
        self.lineEditNumINGroup.setMaxLength(2)
        self.lineEditNumINGroup.setObjectName("lineEditNumINGroup")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditNumINGroup)
        self.labelGroup = QtWidgets.QLabel(startWin)
        self.labelGroup.setObjectName("labelGroup")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelGroup)
        self.lineEditGroup = QtWidgets.QLineEdit(startWin)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditGroup.setFont(font)
        self.lineEditGroup.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEditGroup.setMaxLength(15)
        self.lineEditGroup.setObjectName("lineEditGroup")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditGroup)
        self.btnSignLab = QtWidgets.QPushButton(startWin)
        self.btnSignLab.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.btnSignLab.setFont(font)
        self.btnSignLab.setCheckable(True)
        self.btnSignLab.setDefault(False)
        self.btnSignLab.setFlat(False)
        self.btnSignLab.setObjectName("btnSignLab")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btnSignLab)
        self.btnDeveloperMode = QtWidgets.QPushButton(startWin)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnDeveloperMode.setFont(font)
        self.btnDeveloperMode.setCheckable(True)
        self.btnDeveloperMode.setObjectName("btnDeveloperMode")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.btnDeveloperMode)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(startWin)
        QtCore.QMetaObject.connectSlotsByName(startWin)

    def retranslateUi(self, startWin):
        _translate = QtCore.QCoreApplication.translate
        startWin.setWindowTitle(_translate("startWin", "Dialog"))
        self.labelWelcome.setText(_translate("startWin", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Times New Roman\'; font-size:20pt; color:#000000;\">ПРАКТИЧЕСКОЕ ЗАНЯТИЕ № 3</span></p><p align=\"center\"><span style=\" font-family:\'Times New Roman\'; font-size:20pt; color:#000000;\">ИСПОЛЬЗОВАНИЕ МЕТОДА СЕТЕВОГО ПЛАНИРОВАНИЯ И УПРАВЛЕНИЯ В </span></p><p align=\"center\"><span style=\" font-family:\'Times New Roman\'; font-size:20pt; color:#000000;\">ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССАХ ЭКСПЛУАТАЦИИ КОСМИЧЕСКИХ СРЕДСТВ</span></p></body></html>"))
        self.labelSurname.setText(_translate("startWin", "<html><head/><body><p><span style=\" font-size:16pt;\">Фамилия</span></p></body></html>"))
        self.labelName.setText(_translate("startWin", "<html><head/><body><p><span style=\" font-size:16pt;\">Имя</span></p></body></html>"))
        self.labelNumGroup.setText(_translate("startWin", "<html><head/><body><p><span style=\" font-size:16pt;\">Номер по списку в группе</span></p></body></html>"))
        self.labelGroup.setText(_translate("startWin", "<html><head/><body><p><span style=\" font-size:16pt;\">Группа</span></p></body></html>"))
        self.btnSignLab.setText(_translate("startWin", "Начать работу"))
        self.btnDeveloperMode.setText(_translate("startWin", "Режим разработчика"))

