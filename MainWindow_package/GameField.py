from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPalette

player = 1
class GameFieldButton(QPushButton):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(30)
        self.setStyleSheet("background-color: white; font-size: 24px; min-width: 40px; min-height: 40px; ")
        self.setFixedHeight(30)

        self.access=True




class GameFieldCell_wdg(QWidget):
    def __init__(self, _gameField):
        super().__init__()

        self._gameFieldPointer=_gameField

        self.vinner_in_cell=None

        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.buttons = [
            [GameFieldButton() for _ in range(3)] for _ in range(3)
        ]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(lambda _, x_of_button=i, y_of_button=j: self.button_clicked(x_of_button, y_of_button))
                self.layout.addWidget(self.buttons[i][j], i, j)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("black"))
    def button_clicked(self, x_of_button, y_of_button):
        name_of_button=self.buttons[x_of_button][y_of_button]

        if not name_of_button.access:
            return

        global player

        if player==1:
            name_of_button.setText("x")
            player=2
        else:
            name_of_button.setText("o")
            player=1

        name_of_button.access=False
        self.check_vinner_in_cells()


    def check_vinner_in_cells(self):
        if(self.buttons[0][0].text()==self.buttons[1][1].text()==self.buttons[2][2].text()=='x' or
           self.buttons[0][2].text()==self.buttons[1][1].text()==self.buttons[2][0].text()=='x' or
            self.buttons[0][0].text()==self.buttons[0][1].text()==self.buttons[0][2].text()=='x' or
            self.buttons[1][0].text()==self.buttons[1][1].text()==self.buttons[1][2].text()=='x' or
            self.buttons[2][0].text()==self.buttons[2][1].text()==self.buttons[2][2].text()=='x' or
            self.buttons[0][0].text()==self.buttons[0][1].text()==self.buttons[0][2].text()=='x' or
            self.buttons[1][0].text()==self.buttons[1][1].text()==self.buttons[1][2].text()=='x' or
            self.buttons[2][0].text()==self.buttons[2][1].text()==self.buttons[2][2].text()=='x'):
            self.vinner_in_cell='x'
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].setText('x')
        elif (self.buttons[0][0].text()==self.buttons[1][1].text()==self.buttons[2][2].text()=='o' or
           self.buttons[0][2].text()==self.buttons[1][1].text()==self.buttons[2][0].text()=='o' or
            self.buttons[0][0].text()==self.buttons[0][1].text()==self.buttons[0][2].text()=='o' or
            self.buttons[1][0].text()==self.buttons[1][1].text()==self.buttons[1][2].text()=='o' or
            self.buttons[2][0].text()==self.buttons[2][1].text()==self.buttons[2][2].text()=='o' or
            self.buttons[0][0].text()==self.buttons[1][0].text()==self.buttons[2][0].text()=='o' or
            self.buttons[0][1].text()==self.buttons[1][1].text()==self.buttons[2][1].text()=='o' or
            self.buttons[0][2].text()==self.buttons[1][2].text()==self.buttons[2][2].text()=='o'):

                self.vinner_in_cell = 'o'
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j].setText('o')
        else:
            return

        self.check_vinner_on_all_field()

    def check_vinner_on_all_field(self):
        cells=self._gameFieldPointer.cells
        if (cells[0][0].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][2].vinner_in_cell=='x' or
        cells[0][2].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][0].vinner_in_cell=='x' or
        cells[0][0].vinner_in_cell==cells[0][1].vinner_in_cell==cells[0][2].vinner_in_cell=='x' or
        cells[1][0].vinner_in_cell == cells[1][1].vinner_in_cell == cells[1][2].vinner_in_cell == 'x' or
        cells[2][0].vinner_in_cell == cells[2][1].vinner_in_cell == cells[2][2].vinner_in_cell == 'x' or
        cells[0][0].vinner_in_cell==cells[1][0].vinner_in_cell==cells[2][0].vinner_in_cell=='x' or
        cells[0][1].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][1].vinner_in_cell=='x' or
        cells[0][2].vinner_in_cell==cells[1][2].vinner_in_cell==cells[2][2].vinner_in_cell=='x'):
            print('1')
            return
        elif (cells[0][0].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][2].vinner_in_cell=='o' or
        cells[0][2].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][0].vinner_in_cell=='o' or
        cells[0][0].vinner_in_cell==cells[0][1].vinner_in_cell==cells[0][2].vinner_in_cell=='o' or
        cells[1][0].vinner_in_cell == cells[1][1].vinner_in_cell == cells[1][2].vinner_in_cell == 'o' or
        cells[2][0].vinner_in_cell == cells[2][1].vinner_in_cell == cells[2][2].vinner_in_cell == 'o' or
        cells[0][0].vinner_in_cell==cells[1][0].vinner_in_cell==cells[2][0].vinner_in_cell=='o' or
        cells[0][1].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][1].vinner_in_cell=='o' or
        cells[0][2].vinner_in_cell==cells[1][2].vinner_in_cell==cells[2][2].vinner_in_cell=='o'):
            print('2')
            return




class GameField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setAutoFillBackground(True)

        self.layout_ = QGridLayout()
        #self.layout_.setSpacing(10)
        self.layout_.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_)

        self.cells=[[GameFieldCell_wdg(self) for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.layout_.addWidget(self.cells[i][j], i, j)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("blue"))