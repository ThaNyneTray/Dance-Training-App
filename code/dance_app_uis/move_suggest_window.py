# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\move_suggest_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MoveChallengeWindow(object):
    def setupUi(self, MoveChallengeWindow):
        MoveChallengeWindow.setObjectName("MoveChallengeWindow")
        MoveChallengeWindow.resize(265, 264)
        self.centralwidget = QtWidgets.QWidget(MoveChallengeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.move_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.move_label.setFont(font)
        self.move_label.setAlignment(QtCore.Qt.AlignCenter)
        self.move_label.setObjectName("move_label")
        self.verticalLayout.addWidget(self.move_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.time_lineEdit.setMaximumSize(QtCore.QSize(31, 23))
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.horizontalLayout.addWidget(self.time_lineEdit)
        self.time_slider = QtWidgets.QSlider(self.centralwidget)
        self.time_slider.setMinimum(1)
        self.time_slider.setProperty("value", 8)
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setObjectName("time_slider")
        self.horizontalLayout.addWidget(self.time_slider)
        self.reset_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.reset_pushButton.setObjectName("reset_pushButton")
        self.horizontalLayout.addWidget(self.reset_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_pushButton.setObjectName("start_pushButton")
        self.horizontalLayout_2.addWidget(self.start_pushButton)
        self.pause_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pause_pushButton.setEnabled(False)
        self.pause_pushButton.setObjectName("pause_pushButton")
        self.horizontalLayout_2.addWidget(self.pause_pushButton)
        self.stop_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.horizontalLayout_2.addWidget(self.stop_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.change_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.change_pushButton.setMinimumSize(QtCore.QSize(131, 23))
        self.change_pushButton.setObjectName("change_pushButton")
        self.verticalLayout.addWidget(self.change_pushButton)
        MoveChallengeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MoveChallengeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 26))
        self.menubar.setObjectName("menubar")
        MoveChallengeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MoveChallengeWindow)
        self.statusbar.setObjectName("statusbar")
        MoveChallengeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MoveChallengeWindow)
        QtCore.QMetaObject.connectSlotsByName(MoveChallengeWindow)

    def retranslateUi(self, MoveChallengeWindow):
        _translate = QtCore.QCoreApplication.translate
        MoveChallengeWindow.setWindowTitle(_translate("MoveChallengeWindow", "Move Challenge"))
        self.move_label.setText(_translate("MoveChallengeWindow", "dance move here"))
        self.time_lineEdit.setText(_translate("MoveChallengeWindow", "8"))
        self.reset_pushButton.setText(_translate("MoveChallengeWindow", "Reset"))
        self.start_pushButton.setText(_translate("MoveChallengeWindow", "Start"))
        self.pause_pushButton.setText(_translate("MoveChallengeWindow", "Pause"))
        self.stop_pushButton.setText(_translate("MoveChallengeWindow", "Stop"))
        self.change_pushButton.setText(_translate("MoveChallengeWindow", "Change Move List"))
