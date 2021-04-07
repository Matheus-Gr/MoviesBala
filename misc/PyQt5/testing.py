from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QIcon


def func_1():
    print('gay')


app = QtWidgets.QApplication([])
ui = uic.loadUi("../../ui/moviesBala.ui")

item = QListWidgetItem("Title title title\nuser")
item.setIcon(QIcon(r"../../posters/1.jpg"))
ui.listMovie.addItem(item)

ui.show()
app.exec()
