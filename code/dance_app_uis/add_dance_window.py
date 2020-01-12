# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_dance_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddDanceWindow(object):
    def setupUi(self, AddDanceWindow):
        AddDanceWindow.setObjectName("AddDanceWindow")
        AddDanceWindow.setEnabled(True)
        AddDanceWindow.resize(335, 241)
        self.centralwidget = QtWidgets.QWidget(AddDanceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_gridLayout = QtWidgets.QGridLayout()
        self.input_gridLayout.setObjectName("input_gridLayout")
        self.category_label = QtWidgets.QLabel(self.centralwidget)
        self.category_label.setObjectName("category_label")
        self.input_gridLayout.addWidget(self.category_label, 0, 0, 1, 1)
        self.category_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.category_comboBox.setObjectName("category_comboBox")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.category_comboBox.addItem("")
        self.input_gridLayout.addWidget(self.category_comboBox, 0, 1, 1, 1)
        self.name_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.input_gridLayout.addWidget(self.name_lineEdit, 1, 1, 1, 1)
        self.tags_label = QtWidgets.QLabel(self.centralwidget)
        self.tags_label.setObjectName("tags_label")
        self.input_gridLayout.addWidget(self.tags_label, 2, 0, 1, 1)
        self.name_label = QtWidgets.QLabel(self.centralwidget)
        self.name_label.setObjectName("name_label")
        self.input_gridLayout.addWidget(self.name_label, 1, 0, 1, 1)
        self.description_label = QtWidgets.QLabel(self.centralwidget)
        self.description_label.setObjectName("description_label")
        self.input_gridLayout.addWidget(self.description_label, 3, 0, 1, 1)
        self.description_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.description_textEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.description_textEdit.setObjectName("description_textEdit")
        self.input_gridLayout.addWidget(self.description_textEdit, 3, 1, 1, 1)
        self.tags_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tags_lineEdit.setObjectName("tags_lineEdit")
        self.input_gridLayout.addWidget(self.tags_lineEdit, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.input_gridLayout)
        self.button_gridLayout = QtWidgets.QGridLayout()
        self.button_gridLayout.setObjectName("button_gridLayout")
        self.submit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.button_gridLayout.addWidget(self.submit_pushButton, 0, 0, 1, 1)
        self.cancel_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.button_gridLayout.addWidget(self.cancel_pushButton, 0, 1, 1, 1)
        self.clear_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.button_gridLayout.addWidget(self.clear_pushButton, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.button_gridLayout)
        AddDanceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddDanceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 335, 21))
        self.menubar.setObjectName("menubar")
        AddDanceWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddDanceWindow)
        self.statusbar.setObjectName("statusbar")
        AddDanceWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddDanceWindow)
        QtCore.QMetaObject.connectSlotsByName(AddDanceWindow)

    def retranslateUi(self, AddDanceWindow):
        _translate = QtCore.QCoreApplication.translate
        AddDanceWindow.setWindowTitle(_translate("AddDanceWindow", "Add Dance Move"))
        self.category_label.setText(_translate("AddDanceWindow", "Category"))
        self.category_comboBox.setItemText(0, _translate("AddDanceWindow", "Technique/Step"))
        self.category_comboBox.setItemText(1, _translate("AddDanceWindow", "Concept"))
        self.category_comboBox.setItemText(2, _translate("AddDanceWindow", "Set"))
        self.category_comboBox.setItemText(3, _translate("AddDanceWindow", "Choreography"))
        self.name_lineEdit.setPlaceholderText(_translate("AddDanceWindow", "Enter the name of the move"))
        self.tags_label.setText(_translate("AddDanceWindow", "Tags"))
        self.name_label.setText(_translate("AddDanceWindow", "Name"))
        self.description_label.setText(_translate("AddDanceWindow", "Description"))
        self.description_textEdit.setPlaceholderText(_translate("AddDanceWindow", "(Optional) Enter description for this dance move"))
        self.tags_lineEdit.setPlaceholderText(
            _translate("AddDanceWindow", "Enter tags for this move; separate with semi-colons"))
        self.submit_pushButton.setText(_translate("AddDanceWindow", "Submit"))
        self.cancel_pushButton.setText(_translate("AddDanceWindow", "Cancel"))
        self.clear_pushButton.setText(_translate("AddDanceWindow", "Clear"))
