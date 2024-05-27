from PyQt6.QtWidgets import QMenuBar, QMenu, QColorDialog
from PyQt6.QtGui import QAction, QColor
from .GameField import rgb_field_list, rgb_crosseAndZero_list

class Menu(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        #self.stateMItem=QMenu('State')
        self.editMItem=QMenu('Edit color')
        self.restartMItem=QMenu('Restart')
        #self.fileMItem=QMenu('File')

        #self.addMenu(self.stateMItem)
        self.addMenu(self.restartMItem)
        self.addMenu(self.editMItem)
        #self.addMenu(self.fileMItem)

        # self.loadMenuAction=QAction('&Load')
        # self.stateMItem.addAction(self.loadMenuAction)
        #
        # self.saveMenuAction=QAction('&Save')
        # self.stateMItem.addAction(self.saveMenuAction)

        # self.dropdownMenu=QMenu('&Dropdown')
        # self.dropdownMenu.addAction('&Option 1')
        # self.dropdownMenu.addAction('&Option 2')
        # self.dropdownMenu.addAction('&Option 3')
        #
        # self.editMItem.addMenu(self.dropdownMenu)

        # self.openFileAction=QAction('&Open')
        # self.fileMItem.addAction(self.openFileAction)

        self.editColorOfFieldAction=QAction('Color of field')
        self.editMItem.addAction(self.editColorOfFieldAction)
        self.editColorOfFieldAction.triggered.connect(self.editFieldColor)

        self.restartAction=QAction('Restart game')
        self.restartMItem.addAction(self.restartAction)
        #self.restartAction.triggered.connect(self.restartGame)

        self.editColorOfCrossAndZero=QAction('Color of cross and zero')
        self.editMItem.addAction(self.editColorOfCrossAndZero)
        self.editColorOfCrossAndZero.triggered.connect(self.editColorOfCrAndZe)

    def editFieldColor(self):
        self.dialog=QColorDialog(parent=self)
        #self.dialog.open()
        color = QColor(self.dialog.getColor())

        global rgb_field_list
        rgb_field_list[0] = color.red()
        rgb_field_list[1] = color.green()
        rgb_field_list[2] = color.blue()

    def editColorOfCrAndZe(self):
        self.dialog=QColorDialog(parent=self)
        color=QColor(self.dialog.getColor())
        global rgb_crosseAndZero_list
        rgb_crosseAndZero_list[0] =color.red()
        rgb_crosseAndZero_list[1] = color.green()
        rgb_crosseAndZero_list[2] = color.blue()

    def restartGameAction(self, handler):
        self.restartAction.triggered.connect(handler)






