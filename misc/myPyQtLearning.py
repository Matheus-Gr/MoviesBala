import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, \
    QLineEdit
from PyQt5 import QtGui


class Screen(QMainWindow):
    def __init__(self):
        super().__init__()

        # SCREEN CONFIG
        self.x = 1100
        self.y = 400
        self.width = 800
        self.height = 600
        self.title = 'First Screen'

        # BUTTONS
        ####################################
        button1 = QPushButton('Button A', self)
        button1.move(20, 480)
        button1.resize(150, 100)
        button1.setStyleSheet('QPushButton{'
                              'background-color: #FF99C9;'
                              'font-size: 15px;'
                              'font-family: "Press Start 2P", cursive;'
                              '}')
        button1.clicked.connect(self.button_1_clicked)

        button2 = QPushButton('Button B', self)
        button2.move(190, 480)
        button2.resize(150, 100)
        button2.setStyleSheet('QPushButton{'
                              'background-color: #C1BDDB;'
                              'font-size: 15px;'
                              'font-family: "Press Start 2P", cursive;'
                              '}')
        button2.clicked.connect(self.button_2_clicked)

        button3 = QPushButton('Button C', self)
        button3.move(360, 480)
        button3.resize(150, 100)
        button3.setStyleSheet('QPushButton{'
                              'background-color: #BAF2E9;'
                              'font-size: 15px;'
                              'font-family: "Press Start 2P", cursive;'
                              '}')
        button3.clicked.connect(self.button_3_clicked)

        # LABELS
        ####################################
        self.label1 = QLabel(self)
        self.label1.move(20, 20)
        self.label1.setText('Hey')
        self.label1.resize(760, 50)
        self.label1.setStyleSheet('QLabel{'
                                  'font-family: "Press Start 2P", cursive;'
                                  'font-size: 30px;'
                                  'color: #303A2B'
                                  '}')

        self.image = QLabel(self)
        self.image.move(20, 90)
        self.image.setPixmap(QtGui.QPixmap(''))
        self.image.resize(350, 350)
        self.image.setScaledContents(True)

        self.label2 = QLabel(self)
        self.label2.move(400, 190)
        self.label2.setText('')
        self.label2.resize(760, 50)
        self.label2.setStyleSheet('QLabel{'
                                  'font-family: "Press Start 2P", cursive;'
                                  'font-size: 30px;'
                                  'color: #303A2B'
                                  '}')

        # TEXT BOX
        ####################################
        self.text_box = QLineEdit(self)
        self.text_box.move(400, 90)
        self.text_box.resize(350, 70)
        self.text_box.setStyleSheet('QLineEdit{'
                                    'font-family: "Press Start 2P", cursive;'
                                    'font-size: 20px;'
                                    'color: #303A2B'
                                    '}')

        # LOAD SCREEN
        ####################################
        self.load_screen()

    def load_screen(self):
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button_1_clicked(self):
        self.label1.setText('Curu relax zZ')
        self.label1.setStyleSheet('QLabel{'
                                  'font-family: "Press Start 2P", cursive;'
                                  'font-size: 30px;'
                                  'color: #FF99C9'
                                  '}')
        self.image.setPixmap(QtGui.QPixmap('curu.jpg'))

    def button_2_clicked(self):
        self.label1.setText('Beto mad thirsty')
        self.label1.setStyleSheet('QLabel{'
                                  'font-family: "Press Start 2P", cursive;'
                                  'font-size: 30px;'
                                  'color: #C1BDDB'
                                  '}')
        self.image.setPixmap(QtGui.QPixmap('beto.jpg'))

    def button_3_clicked(self):
        content = self.text_box.text()
        self.label2.setText(content)


app = QApplication(sys.argv)
screen = Screen()
sys.exit(app.exec_())
