# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1558, 923)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        MainMenu.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        MainMenu.setStyleSheet("#centralwidget{background-color: #d5fffe;}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableVar = QtWidgets.QTableWidget(self.frame)
        self.tableVar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.tableVar.setFont(font)
        self.tableVar.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tableVar.setAutoFillBackground(False)
        self.tableVar.setStyleSheet("background-color: #fffaea;\n"
"\n"
"")
        self.tableVar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableVar.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableVar.setLineWidth(2)
        self.tableVar.setMidLineWidth(0)
        self.tableVar.setAutoScrollMargin(16)
        self.tableVar.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableVar.setGridStyle(QtCore.Qt.SolidLine)
        self.tableVar.setRowCount(0)
        self.tableVar.setColumnCount(6)
        self.tableVar.setObjectName("tableVar")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableVar.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        item.setFont(font)
        self.tableVar.setHorizontalHeaderItem(5, item)
        self.tableVar.horizontalHeader().setVisible(True)
        self.tableVar.horizontalHeader().setCascadingSectionResizes(True)
        self.tableVar.horizontalHeader().setDefaultSectionSize(243)
        self.tableVar.horizontalHeader().setHighlightSections(True)
        self.tableVar.horizontalHeader().setMinimumSectionSize(70)
        self.tableVar.horizontalHeader().setSortIndicatorShown(False)
        self.tableVar.horizontalHeader().setStretchLastSection(True)
        self.tableVar.verticalHeader().setVisible(False)
        self.tableVar.verticalHeader().setCascadingSectionResizes(True)
        self.tableVar.verticalHeader().setDefaultSectionSize(35)
        self.tableVar.verticalHeader().setMinimumSectionSize(25)
        self.tableVar.verticalHeader().setSortIndicatorShown(False)
        self.tableVar.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tableVar)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.btnTask5 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask5.setFont(font)
        self.btnTask5.setStyleSheet("background-color: #66e3ff;")
        self.btnTask5.setObjectName("btnTask5")
        self.gridLayout.addWidget(self.btnTask5, 5, 2, 1, 1)
        self.btnTask4 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask4.setFont(font)
        self.btnTask4.setStyleSheet("background-color: #66e3ff;")
        self.btnTask4.setObjectName("btnTask4")
        self.gridLayout.addWidget(self.btnTask4, 4, 2, 1, 1)
        self.btnTeacherMode = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTeacherMode.setFont(font)
        self.btnTeacherMode.setStyleSheet("background-color: #66e3ff;")
        self.btnTeacherMode.setCheckable(True)
        self.btnTeacherMode.setObjectName("btnTeacherMode")
        self.gridLayout.addWidget(self.btnTeacherMode, 5, 4, 1, 1)
        self.btnTask2 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask2.setFont(font)
        self.btnTask2.setStyleSheet("background-color: #66e3ff;")
        self.btnTask2.setObjectName("btnTask2")
        self.gridLayout.addWidget(self.btnTask2, 2, 2, 1, 1)
        self.btnTask6 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask6.setFont(font)
        self.btnTask6.setStyleSheet("background-color: #66e3ff;")
        self.btnTask6.setObjectName("btnTask6")
        self.gridLayout.addWidget(self.btnTask6, 6, 2, 1, 1)
        self.btnTask3 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask3.setFont(font)
        self.btnTask3.setStyleSheet("background-color: #66e3ff;")
        self.btnTask3.setObjectName("btnTask3")
        self.gridLayout.addWidget(self.btnTask3, 3, 2, 1, 1)
        self.btnTask1 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnTask1.setFont(font)
        self.btnTask1.setStyleSheet("background-color: #66e3ff;")
        self.btnTask1.setObjectName("btnTask1")
        self.gridLayout.addWidget(self.btnTask1, 1, 2, 1, 1)
        self.btnSaveReportAs = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.btnSaveReportAs.setFont(font)
        self.btnSaveReportAs.setStyleSheet("background-color: #66e3ff;")
        self.btnSaveReportAs.setObjectName("btnSaveReportAs")
        self.gridLayout.addWidget(self.btnSaveReportAs, 6, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.gridLayout.setColumnStretch(2, 8)
        self.gridLayout.setColumnStretch(3, 5)
        self.gridLayout.setColumnStretch(4, 8)
        self.verticalLayout.addWidget(self.frame_2)
        MainMenu.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainMenu)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1558, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAboutProgram = QtWidgets.QMenu(self.menuBar)
        self.menuAboutProgram.setObjectName("menuAboutProgram")
        self.version = QtWidgets.QMenu(self.menuAboutProgram)
        self.version.setObjectName("version")
        self.menu = QtWidgets.QMenu(self.menuAboutProgram)
        self.menu.setObjectName("menu")
        self.function = QtWidgets.QMenu(self.menuBar)
        self.function.setObjectName("function")
        MainMenu.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)
        self.actionPrintReport = QtWidgets.QAction(MainMenu)
        self.actionPrintReport.setObjectName("actionPrintReport")
        self.actionOpenReport = QtWidgets.QAction(MainMenu)
        self.actionOpenReport.setObjectName("actionOpenReport")
        self.actionactionSaveReportReport_3 = QtWidgets.QAction(MainMenu)
        self.actionactionSaveReportReport_3.setObjectName("actionactionSaveReportReport_3")
        self.actionHelpWithProg = QtWidgets.QAction(MainMenu)
        self.actionHelpWithProg.setObjectName("actionHelpWithProg")
        self.actionHelpWithTheory = QtWidgets.QAction(MainMenu)
        self.actionHelpWithTheory.setObjectName("actionHelpWithTheory")
        self.actionEditTaskVariant = QtWidgets.QAction(MainMenu)
        self.actionEditTaskVariant.setObjectName("actionEditTaskVariant")
        self.actionPreviewReport = QtWidgets.QAction(MainMenu)
        self.actionPreviewReport.setObjectName("actionPreviewReport")
        self.actionPrint = QtWidgets.QAction(MainMenu)
        self.actionPrint.setObjectName("actionPrint")
        self.actionReportSign = QtWidgets.QAction(MainMenu)
        self.actionReportSign.setObjectName("actionReportSign")
        self.num_ver = QtWidgets.QAction(MainMenu)
        self.num_ver.setObjectName("num_ver")
        self.action_2 = QtWidgets.QAction(MainMenu)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainMenu)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainMenu)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainMenu)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainMenu)
        self.action_6.setObjectName("action_6")
        self.actionHelpWithProgTeach = QtWidgets.QAction(MainMenu)
        self.actionHelpWithProgTeach.setObjectName("actionHelpWithProgTeach")
        self.actionDecryptRep = QtWidgets.QAction(MainMenu)
        self.actionDecryptRep.setObjectName("actionDecryptRep")
        self.actionImportDB = QtWidgets.QAction(MainMenu)
        self.actionImportDB.setObjectName("actionImportDB")
        self.actionExportDB = QtWidgets.QAction(MainMenu)
        self.actionExportDB.setObjectName("actionExportDB")
        self.menuHelp.addAction(self.actionHelpWithProg)
        self.menuHelp.addAction(self.actionHelpWithProgTeach)
        self.menuHelp.addAction(self.actionHelpWithTheory)
        self.version.addAction(self.num_ver)
        self.menu.addSeparator()
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_6)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_3)
        self.menuAboutProgram.addAction(self.version.menuAction())
        self.menuAboutProgram.addAction(self.menu.menuAction())
        self.function.addAction(self.actionEditTaskVariant)
        self.function.addAction(self.actionImportDB)
        self.function.addAction(self.actionExportDB)
        self.function.addSeparator()
        self.function.addAction(self.actionReportSign)
        self.function.addSeparator()
        self.function.addAction(self.actionDecryptRep)
        self.function.addAction(self.actionPreviewReport)
        self.function.addAction(self.actionPrint)
        self.menuBar.addAction(self.function.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuAboutProgram.menuAction())

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Меню"))
        item = self.tableVar.horizontalHeaderItem(0)
        item.setText(_translate("MainMenu", "Шифр работы"))
        item = self.tableVar.horizontalHeaderItem(1)
        item.setText(_translate("MainMenu", "Номер отделения\n"
"выполняющего\n"
"работу"))
        item = self.tableVar.horizontalHeaderItem(2)
        item.setText(_translate("MainMenu", "Число людей,\n"
"выполняющих работы"))
        item = self.tableVar.horizontalHeaderItem(3)
        item.setText(_translate("MainMenu", "Продолжительность\n"
"работ (час)"))
        item = self.tableVar.horizontalHeaderItem(4)
        item.setText(_translate("MainMenu", "Номер\n"
"отделения"))
        item = self.tableVar.horizontalHeaderItem(5)
        item.setText(_translate("MainMenu", "Количество\n"
"людей\n"
"в отделении"))
        self.btnTask5.setText(_translate("MainMenu", "Задание 5"))
        self.btnTask4.setText(_translate("MainMenu", "Задание 4"))
        self.btnTeacherMode.setText(_translate("MainMenu", "Режим преподавателя"))
        self.btnTask2.setText(_translate("MainMenu", "Задание 2"))
        self.btnTask6.setText(_translate("MainMenu", "Задание 6"))
        self.btnTask3.setText(_translate("MainMenu", "Задание 3"))
        self.btnTask1.setText(_translate("MainMenu", "Задание 1"))
        self.btnSaveReportAs.setText(_translate("MainMenu", "Сохранить отчет как"))
        self.menuHelp.setTitle(_translate("MainMenu", "Справка"))
        self.menuAboutProgram.setTitle(_translate("MainMenu", "О программе"))
        self.version.setTitle(_translate("MainMenu", "Версия"))
        self.menu.setTitle(_translate("MainMenu", "Разработчики"))
        self.function.setTitle(_translate("MainMenu", "Дополнительные функции"))
        self.actionPrintReport.setText(_translate("MainMenu", "печать отчета"))
        self.actionOpenReport.setText(_translate("MainMenu", "открыть отчет"))
        self.actionactionSaveReportReport_3.setText(_translate("MainMenu", "сохранить отчет"))
        self.actionHelpWithProg.setText(_translate("MainMenu", "Справка по работе с программой для студента"))
        self.actionHelpWithTheory.setText(_translate("MainMenu", "Справка по теории"))
        self.actionEditTaskVariant.setText(_translate("MainMenu", "Редактировать варианты"))
        self.actionPreviewReport.setText(_translate("MainMenu", "Предпросмотр отчета"))
        self.actionPrint.setText(_translate("MainMenu", "Печать отчета"))
        self.actionReportSign.setText(_translate("MainMenu", "Изменить данные студента"))
        self.num_ver.setText(_translate("MainMenu", "1.0"))
        self.action_2.setText(_translate("MainMenu", "Иванов Ф. А."))
        self.action_3.setText(_translate("MainMenu", "Гаврилов В. К."))
        self.action_4.setText(_translate("MainMenu", "Доронин О. А."))
        self.action_5.setText(_translate("MainMenu", "Мариничев И. А."))
        self.action_6.setText(_translate("MainMenu", "Тимофеев А. В."))
        self.actionHelpWithProgTeach.setText(_translate("MainMenu", "Справка по работе с программой для преподавателя"))
        self.actionDecryptRep.setText(_translate("MainMenu", "Расшифровать отчет"))
        self.actionImportDB.setText(_translate("MainMenu", "Импорт вариантов заданий"))
        self.actionExportDB.setText(_translate("MainMenu", "Экспорт вариантов заданий"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())

