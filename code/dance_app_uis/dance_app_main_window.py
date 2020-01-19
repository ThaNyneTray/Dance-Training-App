# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dance_app_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DanceAppMainWindow(object):
    def setupUi(self, DanceAppMainWindow):
        DanceAppMainWindow.setObjectName("DanceAppMainWindow")
        DanceAppMainWindow.resize(407, 160)
        self.centralwidget = QtWidgets.QWidget(DanceAppMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.add_move_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_move_pushButton.setObjectName("add_move_pushButton")
        self.gridLayout.addWidget(self.add_move_pushButton, 2, 0, 1, 1)
        self.modify_move_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.modify_move_pushButton.setObjectName("modify_move_pushButton")
        self.gridLayout.addWidget(self.modify_move_pushButton, 2, 1, 1, 1)
        self.challenge_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.challenge_pushButton.setObjectName("challenge_pushButton")
        self.gridLayout.addWidget(self.challenge_pushButton, 2, 2, 1, 1)
        DanceAppMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DanceAppMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
        self.menubar.setObjectName("menubar")
        DanceAppMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DanceAppMainWindow)
        self.statusbar.setObjectName("statusbar")
        DanceAppMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DanceAppMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DanceAppMainWindow)

    def retranslateUi(self, DanceAppMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DanceAppMainWindow.setWindowTitle(_translate("DanceAppMainWindow", "Dance App"))
        self.label.setText(
            _translate("DanceAppMainWindow", "Welcome to the Dance Training App! This is an incomplete version."))
        self.label_2.setText(_translate("DanceAppMainWindow",
                                        " I will add more features and refine existing ones with time and interest."))
        self.add_move_pushButton.setText(_translate("DanceAppMainWindow", "Add Move"))
        self.modify_move_pushButton.setText(_translate("DanceAppMainWindow", "Modify Moves"))
        self.challenge_pushButton.setText(_translate("DanceAppMainWindow", "Challenge"))
