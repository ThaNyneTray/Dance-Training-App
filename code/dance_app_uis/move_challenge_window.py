# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\move_challenge_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChallengeWindow(object):
    def setupUi(self, ChallengeWindow):
        ChallengeWindow.setObjectName("ChallengeWindow")
        ChallengeWindow.resize(697, 466)
        self.centralwidget = QtWidgets.QWidget(ChallengeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.explanation_label = QtWidgets.QLabel(self.centralwidget)
        self.explanation_label.setObjectName("explanation_label")
        self.verticalLayout.addWidget(self.explanation_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.from_listView = QtWidgets.QListView(self.centralwidget)
        self.from_listView.setObjectName("from_listView")
        self.horizontalLayout_2.addWidget(self.from_listView)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_pushButton.setObjectName("add_pushButton")
        self.verticalLayout_2.addWidget(self.add_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.verticalLayout_2.addWidget(self.remove_pushButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.to_listView = QtWidgets.QListView(self.centralwidget)
        self.to_listView.setObjectName("to_listView")
        self.horizontalLayout_2.addWidget(self.to_listView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(458, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.next_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.next_pushButton.setObjectName("next_pushButton")
        self.horizontalLayout.addWidget(self.next_pushButton)
        self.cancel_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        ChallengeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChallengeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menubar.setObjectName("menubar")
        ChallengeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChallengeWindow)
        self.statusbar.setObjectName("statusbar")
        ChallengeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChallengeWindow)
        QtCore.QMetaObject.connectSlotsByName(ChallengeWindow)

    def retranslateUi(self, ChallengeWindow):
        _translate = QtCore.QCoreApplication.translate
        ChallengeWindow.setWindowTitle(_translate("ChallengeWindow", "Move Challenge"))
        self.explanation_label.setText(
            _translate("ChallengeWindow", "Select moves from the list below for the challenge from the list below "))
        self.add_pushButton.setText(_translate("ChallengeWindow", "Add"))
        self.remove_pushButton.setText(_translate("ChallengeWindow", "Remove"))
        self.next_pushButton.setText(_translate("ChallengeWindow", "Next"))
        self.cancel_pushButton.setText(_translate("ChallengeWindow", "Cancel"))
