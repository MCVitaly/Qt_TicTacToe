import PyQt6
from PyQt6.QtWidgets import QLabel, QApplication, QMainWindow, QGridLayout, QWidget
from PyQt6 import QtGui
from PyQt6.QtCore import Qt

import sys

class bigZeroOrCross(QLabel):
    def __init__(self, symbol):
        super().__init__()

        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.pen = QtGui.QPen()
        self.pen.setWidth(10)
        self.pen.setColor(Qt.GlobalColor.black)

        self.canvas=QtGui.QPixmap(self.width(), self.height())
        self.canvas.fill(Qt.GlobalColor.white)
        self.setPixmap(self.canvas)

        self.painter = QtGui.QPainter(self.canvas)
        self.painter.setPen(self.pen)

        if(symbol=='o'):
            self.painter.drawEllipse(20, 20, self.width()-40, self.height()-40)
            self.painter.end()
        elif(symbol=='x'):
            self.painter.drawLine(20, 20, self.width()-20, self.height()-20)
            self.painter.drawLine(self.width()-20, 20, 20, self.height()-20)
        self.setPixmap(self.canvas)

app=QApplication(sys.argv)

window=QMainWindow()
layout=QGridLayout()
layout.addWidget(bigZeroOrCross('x'),1,2)
widget=QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()
sys.exit(app.exec())

