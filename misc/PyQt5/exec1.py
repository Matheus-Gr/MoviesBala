from PyQt5 import uic, QtWidgets


def func_1():
    if ui.radB_1.isChecked():
        color = "Pink"
        ui.lb_2.setStyleSheet('QLabel{color: #F477FF};')
    elif ui.radB_2.isChecked():
        color = "Purple"
        ui.lb_2.setStyleSheet('QLabel{color: #D061FF};')
    elif ui.radB_3.isChecked():
        color = "Blue"
        ui.lb_2.setStyleSheet('QLabel{color: #509FFF};')
    elif ui.radB_4.isChecked():
        color = "Light Blue"
        ui.lb_2.setStyleSheet('QLabel{color: #61E2FF};')
    else:
        color = ""

    ui.lb_2.setText(color)


app = QtWidgets.QApplication([])
ui = uic.loadUi("../../ui/exec1.ui")
ui.btn_send.clicked.connect(func_1)

ui.show()
app.exec()
