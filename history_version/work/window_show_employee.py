# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_show_employee.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from back import database
from functools import partial

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(738, 434)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 331, 16))
        self.label.setObjectName("label")
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 20, 701, 331))
        self.tableWidget_2.setRowCount(15)
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 380, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_2.clicked.connect(partial(self.show_employee))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "检查员工的信息"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Fresh"))

    def show_employee(self):
        print("hh")
        x = database()
        x.show_employee(self.tableWidget_2)