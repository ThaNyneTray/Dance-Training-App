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
        ModifyDanceMove.resize(612, 489)
        self.centralwidget = QtWidgets.QWidget(ModifyDanceMove)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.search_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.horizontalLayout_2.addWidget(self.search_lineEdit)
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
        self.horizontalLayout_2.addWidget(self.filter_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.moves_View = QtWidgets.QTableView(self.centralwidget)
        self.moves_View.setShowGrid(False)
        self.moves_View.setObjectName("moves_View")
        self.moves_View.horizontalHeader().setCascadingSectionResizes(False)
        self.moves_View.verticalHeader().setVisible(False)
        self.horizontalLayout_3.addWidget(self.moves_View)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.category_label = QtWidgets.QLabel(self.centralwidget)
        self.category_label.setObjectName("category_label")
        self.verticalLayout.addWidget(self.category_label)
        self.category_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.category_comboBox.setObjectName("category_comboBox")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.verticalLayout.addWidget(self.category_comboBox)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.verticalLayout.addWidget(self.name_lineEdit)
        self.tags_label = QtWidgets.QLabel(self.centralwidget)
        self.tags_label.setObjectName("tags_label")
        self.verticalLayout.addWidget(self.tags_label)
        self.tags_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tags_lineEdit.setObjectName("tags_lineEdit")
        self.verticalLayout.addWidget(self.tags_lineEdit)
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setObjectName("description_label")
        self.verticalLayout.addWidget(self.description_label)
        self.description_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.description_textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.description_textEdit.setObjectName("description_textEdit")
        self.verticalLayout.addWidget(self.description_textEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        ModifyDanceMove.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyDanceMove)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 26))
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
        self.category_label.setText(_translate("ModifyDanceMove", "Category"))
        self.category_comboBox.setItemText(0, _translate("ModifyDanceMove", "Technique/Step"))
        self.category_comboBox.setItemText(1, _translate("ModifyDanceMove", "Concept"))
        self.category_comboBox.setItemText(2, _translate("ModifyDanceMove", "Set"))
        self.category_comboBox.setItemText(3, _translate("ModifyDanceMove", "Choreography"))
        self.name_label.setText(_translate("ModifyDanceMove", "Name"))
        self.name_lineEdit.setPlaceholderText(_translate("ModifyDanceMove", "Enter the name of the move"))
        self.tags_label.setText(_translate("ModifyDanceMove", "Tags"))
        self.tags_lineEdit.setPlaceholderText(
            _translate("ModifyDanceMove", "Enter tags for this move; separate with semi-colons"))
        self.description_label.setText(_translate("ModifyDanceMove", "Description"))
        self.cancel_Button.setText(_translate("ModifyDanceMove", "Cancel Changes"))
        self.undo_Button.setText(_translate("ModifyDanceMove", "Undo Changes"))
        self.submit_Button.setText(_translate("ModifyDanceMove", "Submit Changes"))
