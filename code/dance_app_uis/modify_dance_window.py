# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify_dance_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifyDanceMove(object):
    def setupUi(self, ModifyDanceMove):
        ModifyDanceMove.setObjectName("ModifyDanceMove")
        ModifyDanceMove.resize(569, 407)
        self.centralwidget = QtWidgets.QWidget(ModifyDanceMove)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.filter_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_comboBox.sizePolicy().hasHeightForWidth())
        self.filter_comboBox.setSizePolicy(sizePolicy)
        self.filter_comboBox.setObjectName("filter_comboBox")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.gridLayout.addWidget(self.filter_comboBox, 0, 4, 1, 1)
        self.search_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.gridLayout.addWidget(self.search_lineEdit, 0, 0, 1, 4)
        self.moves_View = QtWidgets.QTableView(self.centralwidget)
        self.moves_View.setShowGrid(False)
        self.moves_View.setObjectName("moves_View")
        self.moves_View.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.moves_View, 1, 0, 1, 5)
        self.undo_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_Button.sizePolicy().hasHeightForWidth())
        self.undo_Button.setSizePolicy(sizePolicy)
        self.undo_Button.setObjectName("undo_Button")
        self.gridLayout.addWidget(self.undo_Button, 2, 2, 1, 1)
        self.submit_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_Button.sizePolicy().hasHeightForWidth())
        self.submit_Button.setSizePolicy(sizePolicy)
        self.submit_Button.setObjectName("submit_Button")
        self.gridLayout.addWidget(self.submit_Button, 2, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_Button.sizePolicy().hasHeightForWidth())
        self.cancel_Button.setSizePolicy(sizePolicy)
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 2, 4, 1, 1)
        ModifyDanceMove.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyDanceMove)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        ModifyDanceMove.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifyDanceMove)
        self.statusbar.setObjectName("statusbar")
        ModifyDanceMove.setStatusBar(self.statusbar)

        self.retranslateUi(ModifyDanceMove)
        QtCore.QMetaObject.connectSlotsByName(ModifyDanceMove)

    def retranslateUi(self, ModifyDanceMove):
        _translate = QtCore.QCoreApplication.translate
        ModifyDanceMove.setWindowTitle(_translate("ModifyDanceMove", "Modify Dance Video"))
        self.filter_comboBox.setItemText(0, _translate("ModifyDanceMove", "Everything"))
        self.filter_comboBox.setItemText(1, _translate("ModifyDanceMove", "Name"))
        self.filter_comboBox.setItemText(2, _translate("ModifyDanceMove", "Category"))
        self.filter_comboBox.setItemText(3, _translate("ModifyDanceMove", "Tags"))
        self.filter_comboBox.setItemText(4, _translate("ModifyDanceMove", "Description"))
        self.search_lineEdit.setPlaceholderText(
            _translate("ModifyDanceMove", "enter search term; e.g kick step, hip hop e.t.c"))
        self.undo_Button.setText(_translate("ModifyDanceMove", "Undo Changes"))
        self.submit_Button.setText(_translate("ModifyDanceMove", "Submit Changes"))
        self.cancel_Button.setText(_translate("ModifyDanceMove", "Cancel Changes"))
