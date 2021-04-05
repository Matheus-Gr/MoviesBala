import sys
from PyQt5 import uic, QtWidgets
from lib import data_base, utils


def add():
    text = ui.le_textBox.text()
    if text == '':
        return
    ui.ls_list.addItem(text)
    ui.le_textBox.setText('')


def remove():
    item = ui.ls_list.selectedItems()
    if not item:
        return
    ui.ls_list.takeItem(ui.ls_list.row(item[0]))


data_base = data_base.DataBase()

app = QtWidgets.QApplication([])
ui = uic.loadUi("../../ui/exec2.ui")

title_list = data_base.get_column_data(utils.TITLE_COLUMN, utils.MOVIES_TABLE)
for title in title_list:
    ui.ls_list.addItem(title[0])

ui.bnt_1.clicked.connect(add)
ui.bnt_2.clicked.connect(remove)

ui.show()
sys.exit(app.exec())
