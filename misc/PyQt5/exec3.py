from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox


def func_1():
    data = ui.le_textBox.text()
    print(data)
    ui.le_textBox.setText('')
    if data == '' or ('0' <= data <= '9'):
        QMessageBox.about(ui, 'Alert', 'Invalid name!')


app = QtWidgets.QApplication([])
ui = uic.loadUi("../../ui/exec3.ui")
ui.btn_send.clicked.connect(func_1)

ui.show()
app.exec()
