from MainWindow_package import GameField, Menu, Player

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QGridLayout, QWidget, QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout
import sys

app=QApplication(sys.argv)
window=QMainWindow()
window.setGeometry(200, 100, 1000, 300)

window.setMenuBar(Menu(window))

layout=QHBoxLayout()

layout1=QVBoxLayout()
layout1.addWidget(QLabel(), 1)
layout1.addWidget(GameField(window), 4)
layout1.addWidget(QLabel(), 1)

wdg=QWidget(window)
wdg.setLayout(layout1)



layout.addWidget(Player(2), 1)
layout.addWidget(wdg, 1)
layout.addWidget(Player(1), 1)

widget=QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()
sys.exit(app.exec())


