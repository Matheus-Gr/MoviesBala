from PyQt5 import uic, QtWidgets


def func_1():
    print('gay')


app = QtWidgets.QApplication([])
ui = uic.loadUi("../../ui/some.ui")
ui.btn_send.clicked.connect(func_1)

ui.show()
app.exec()
