from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *
import sys
from code.dance_app_uis.move_suggest_window import Ui_MoveChallengeWindow


class MoveChallengeWindow(QtWidgets.QMainWindow):
    # init function
    def __init__(self):
        super(MoveChallengeWindow, self).__init__()
        self.ui = Ui_MoveChallengeWindow()
        self.ui.setupUi(self)

        self.attach_slots()

    def attach_slots(self):
        self.ui.time_slider.valueChanged.connect(lambda: self.val_changed(self.ui.time_slider, "lineEdit"))
        self.ui.time_lineEdit.textChanged.connect(lambda: self.val_changed(self.ui.time_lineEdit, "slider"))
        self.ui.reset_pushButton.clicked.connect(self.reset)
        self.ui.start_pushButton.clicked.connect(self.start_suggestions)
        self.ui.stop_pushButton.clicked.connect(self.stop_suggestions)
        self.ui.change_pushButton.clicked.connect(self.open_moves_selection)

    # slot/method that links the slider with the line edit
    def val_changed(self, which, string):
        if not self.ui.time_lineEdit.text():
            return
        elif string == "lineEdit":
            self.ui.time_lineEdit.setText(str(self.ui.time_slider.value()))
        elif string == "slider":
            self.ui.time_slider.setValue(int(self.ui.time_lineEdit.text()))

    # slot/method for reset button
    def reset(self):
        self.ui.time_lineEdit.setText("8")
        self.ui.time_slider.setValue(8)

    # slot/method for start button
    def start_suggestions(self):
        pass

    # slot/method for stop button
    def stop_suggestions(self):
        pass

    # TODO: this is terrible coding my man. I wonder how many guidelines
    #  I've broken just now.
    def open_moves_selection(self):
        import code.move_challenge_code as mcc

        mcc.window.show()


_excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    _excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

# def execute():
#     #   app = QtWidgets.QApplication(sys.argv)
#     window = MoveChallengeWindow()
#     window.show()
#     # app.exec_()

# execute()
