# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextTask4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextTask4(object):
    def setupUi(self, TextTask4):
        TextTask4.setObjectName("TextTask4")
        TextTask4.resize(621, 208)
        self.verticalLayout = QtWidgets.QVBoxLayout(TextTask4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(TextTask4)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(TextTask4)
        QtCore.QMetaObject.connectSlotsByName(TextTask4)

    def retranslateUi(self, TextTask4):
        _translate = QtCore.QCoreApplication.translate
        TextTask4.setWindowTitle(_translate("TextTask4", "Задание 4"))
        self.label.setText(_translate("TextTask4", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Задание 4</span></p><p align=\"center\"><br/></p><p><span style=\" font-size:14pt;\">Перестроить полигональный сетевой график в ранних сроках наступления событий в сетевой график в ортогональной форме также в ранних сроках, но по отделениям.</span></p></body></html>"))
