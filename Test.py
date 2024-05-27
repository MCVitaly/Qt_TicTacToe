from MainWindow_package import GameField, Menu, Player

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QGridLayout, QWidget, QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QResizeEvent
import sys

app=QApplication(sys.argv)
window=QMainWindow()
window.setGeometry(200, 100, 1100, 650)
window.setWindowTitle('Tic tac toe')

menu=Menu(window)
gameField=GameField(window)
menu.restartGameAction(gameField.restartGameField)

window.setMenuBar(menu)

layout=QHBoxLayout()

layout1=QVBoxLayout()
layout1.addWidget(QLabel(), 1)
layout1.addWidget(gameField, 7)
layout1.addWidget(QLabel(), 1)

wdg=QWidget(window)
wdg.setLayout(layout1)




layout.addWidget(Player(2), 3)
layout.addWidget(wdg, 5)
layout.addWidget(Player(1), 3)

widget=QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()
sys.exit(app.exec())


