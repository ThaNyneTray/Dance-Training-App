# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\modify_dance_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifyDanceMove(object):
    def setupUi(self, ModifyDanceMove):
        ModifyDanceMove.setObjectName("ModifyDanceMove")
        ModifyDanceMove.resize(561, 414)
        self.centralwidget = QtWidgets.QWidget(ModifyDanceMove)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.search_lineEdit = QtWidgets.QLineEdit(self.splitter)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.filter_comboBox = QtWidgets.QComboBox(self.splitter)
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
        self.moves_View = QtWidgets.QTableView(self.splitter_3)
        self.moves_View.setShowGrid(False)
        self.moves_View.setObjectName("moves_View")
        self.moves_View.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.splitter_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_Button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_Button.setEnabled(True)
        self.cancel_Button.setMinimumSize(QtCore.QSize(111, 23))
        self.cancel_Button.setObjectName("cancel_Button")
        self.horizontalLayout.addWidget(self.cancel_Button)
        self.undo_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_Button.sizePolicy().hasHeightForWidth())
        self.undo_Button.setSizePolicy(sizePolicy)
        self.undo_Button.setMinimumSize(QtCore.QSize(101, 23))
        self.undo_Button.setObjectName("undo_Button")
        self.horizontalLayout.addWidget(self.undo_Button)
        self.submit_Button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_Button.sizePolicy().hasHeightForWidth())
        self.submit_Button.setSizePolicy(sizePolicy)
        self.submit_Button.setMinimumSize(QtCore.QSize(121, 23))
        self.submit_Button.setObjectName("submit_Button")
        self.horizontalLayout.addWidget(self.submit_Button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        ModifyDanceMove.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyDanceMove)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 561, 21))
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
        self.search_lineEdit.setPlaceholderText(
            _translate("ModifyDanceMove", "enter search term; e.g kick step, hip hop e.t.c"))
        self.filter_comboBox.setItemText(0, _translate("ModifyDanceMove", "Everything"))
        self.filter_comboBox.setItemText(1, _translate("ModifyDanceMove", "Name"))
        self.filter_comboBox.setItemText(2, _translate("ModifyDanceMove", "Category"))
        self.filter_comboBox.setItemText(3, _translate("ModifyDanceMove", "Tags"))
        self.filter_comboBox.setItemText(4, _translate("ModifyDanceMove", "Description"))
        self.cancel_Button.setText(_translate("ModifyDanceMove", "Cancel Changes"))
        self.undo_Button.setText(_translate("ModifyDanceMove", "Undo Changes"))
        self.submit_Button.setText(_translate("ModifyDanceMove", "Submit Changes"))
