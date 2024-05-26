from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPalette
# from big_zero_or_cross import bigZeroOrCross
player = 1

rgb_field_list=[0, 0, 139]
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
        rect = QRect(5, 9, self.width()-12, self.height())
        painter.fillRect(rect, QColor("black"))

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
        self.set_access_to_game_field(x_of_button, y_of_button)




    def check_vinner_in_cells(self):
        if(self.buttons[0][0].text()==self.buttons[1][1].text()==self.buttons[2][2].text()=='x' or
           self.buttons[0][2].text()==self.buttons[1][1].text()==self.buttons[2][0].text()=='x' or
            self.buttons[0][0].text()==self.buttons[0][1].text()==self.buttons[0][2].text()=='x' or
            self.buttons[1][0].text()==self.buttons[1][1].text()==self.buttons[1][2].text()=='x' or
            self.buttons[2][0].text()==self.buttons[2][1].text()==self.buttons[2][2].text()=='x' or
            self.buttons[0][0].text()==self.buttons[1][0].text()==self.buttons[2][0].text()=='x' or
            self.buttons[0][1].text()==self.buttons[1][1].text()==self.buttons[2][1].text()=='x' or
            self.buttons[0][2].text()==self.buttons[1][2].text()==self.buttons[2][2].text()=='x'):
            self.vinner_in_cell='x'
            for i in range(3):
                for j in range(3):
                    if(self._gameFieldPointer.cells[i][j]==self):
                        self._gameFieldPointer.layout_.addWidget(bigZeroOrCross('x'), i, j)

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
                    if (self._gameFieldPointer.cells[i][j] == self):
                        self._gameFieldPointer.layout_.addWidget(bigZeroOrCross('o'), i, j)
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
            self.dialog=QMessageBox()
            self.dialog.setText("Player 1 won")
            self.dialog.exec()
            return
        elif (cells[0][0].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][2].vinner_in_cell=='o' or
        cells[0][2].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][0].vinner_in_cell=='o' or
        cells[0][0].vinner_in_cell==cells[0][1].vinner_in_cell==cells[0][2].vinner_in_cell=='o' or
        cells[1][0].vinner_in_cell == cells[1][1].vinner_in_cell == cells[1][2].vinner_in_cell == 'o' or
        cells[2][0].vinner_in_cell == cells[2][1].vinner_in_cell == cells[2][2].vinner_in_cell == 'o' or
        cells[0][0].vinner_in_cell==cells[1][0].vinner_in_cell==cells[2][0].vinner_in_cell=='o' or
        cells[0][1].vinner_in_cell==cells[1][1].vinner_in_cell==cells[2][1].vinner_in_cell=='o' or
        cells[0][2].vinner_in_cell==cells[1][2].vinner_in_cell==cells[2][2].vinner_in_cell=='o'):
            self.dialog = QMessageBox()
            self.dialog.setText("Player 2 won")
            self.dialog.exec()
            return

    def set_access_to_game_field(self, x_of_button, y_of_button):
        if (self == self._gameFieldPointer.cells[x_of_button][y_of_button] and (self.vinner_in_cell is None)):
            return
        elif(self == self._gameFieldPointer.cells[x_of_button][y_of_button] and not (self.vinner_in_cell is None)):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if(self._gameFieldPointer.cells[i][j].buttons[k][l].access==True):
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(True)
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet(
                                "background-color: white; font-size: 24px; min-width: 40px; min-height: 40px; ")



        if( not (self._gameFieldPointer.cells[x_of_button][y_of_button].vinner_in_cell is None)):
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if (self._gameFieldPointer.cells[i][j].buttons[k][l].access == True):
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(True)
                                self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet(
                                    "background-color: white; font-size: 24px; min-width: 40px; min-height: 40px; ")

        else:
            if(self._gameFieldPointer.accessToAllButtons_flag):
                for i in range(3):
                    for j in range(3):
                            for k in range(3):
                                for l in range(3):
                                    self._gameFieldPointer.cells[i][j].buttons[k][l].setEnabled(False)
                                    self._gameFieldPointer.cells[i][j].buttons[k][l].setStyleSheet("background-color: #D3D3D3; font-size: 24px; min-width: 40px; min-height: 40px; ")

            else:
                for button in self.buttons:
                    button.setEnabled(False)

            for i in range(3):
                for j in range(3):
                    if (self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].access == True):
                        self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].setEnabled(True)
                        self._gameFieldPointer.cells[x_of_button][y_of_button].buttons[i][j].setStyleSheet("background-color: white; font-size: 24px; min-width: 40px; min-height: 40px; ")






class GameField(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.accessToAllButtons_flag=True

        self.setAutoFillBackground(True)

        self.layout_ = QGridLayout()
        self.layout_.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout_)

        self.cells=[[GameFieldCell_wdg(self) for _ in range(3)] for _ in range(3)]


        for i in range(3):
            for j in range(3):
                self.layout_.addWidget(self.cells[i][j], i, j)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = QRect(1, 1, self.width(), self.height()+2)

        global rgb_field_list

        painter.fillRect(rect, QColor(rgb_field_list[0], rgb_field_list[1], rgb_field_list[2]))



class bigZeroOrCross(QLabel):
    def __init__(self, symbol):
        super().__init__()


        self.setGeometry(3, 0, 143, 143)
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