# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1687, 1044)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableTaskVar = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tableTaskVar.setFont(font)
        self.tableTaskVar.setStyleSheet("background-color: #fffaea;")
        self.tableTaskVar.setObjectName("tableTaskVar")
        self.tableTaskVar.setColumnCount(6)
        self.tableTaskVar.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableTaskVar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableTaskVar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableTaskVar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableTaskVar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableTaskVar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableTaskVar.setHorizontalHeaderItem(5, item)
        self.tableTaskVar.horizontalHeader().setDefaultSectionSize(340)
        self.tableTaskVar.horizontalHeader().setStretchLastSection(True)
        self.tableTaskVar.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableTaskVar)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnExitAndClose = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnExitAndClose.setFont(font)
        self.btnExitAndClose.setStyleSheet("background-color: #66e3ff;")
        self.btnExitAndClose.setObjectName("btnExitAndClose")
        self.gridLayout.addWidget(self.btnExitAndClose, 1, 2, 1, 1)
        self.btnDelStrLast = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnDelStrLast.setFont(font)
        self.btnDelStrLast.setStyleSheet("background-color: #66e3ff;")
        self.btnDelStrLast.setObjectName("btnDelStrLast")
        self.gridLayout.addWidget(self.btnDelStrLast, 1, 1, 1, 1)
        self.btnAddStrInTable = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnAddStrInTable.setFont(font)
        self.btnAddStrInTable.setStyleSheet("background-color: #66e3ff;")
        self.btnAddStrInTable.setObjectName("btnAddStrInTable")
        self.gridLayout.addWidget(self.btnAddStrInTable, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Таблица варианта работы"))
        item = self.tableTaskVar.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Шифр\n"
"работы"))
        item = self.tableTaskVar.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Номер отделения\n"
"выполняющего\n"
"работу"))
        item = self.tableTaskVar.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Число людей,\n"
"выполняющих\n"
"работы"))
        item = self.tableTaskVar.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Продолжительность\n"
"работ (час)"))
        item = self.tableTaskVar.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Номер\n"
"отделения"))
        item = self.tableTaskVar.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Количество людей\n"
"в отделении"))
        self.btnExitAndClose.setText(_translate("Dialog", "Сохранить и выйти"))
        self.btnDelStrLast.setText(_translate("Dialog", "Удалить последнюю строку "))
        self.btnAddStrInTable.setText(_translate("Dialog", "Добвить строку"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
