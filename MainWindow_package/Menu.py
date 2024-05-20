from PyQt6.QtWidgets import QMenuBar, QMenu, QColorDialog
from PyQt6.QtGui import QAction

class Menu(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)

        self.stateMItem=QMenu('State')
        self.editMItem=QMenu('Edit')
        self.fileMItem=QMenu('File')
        self.addMenu(self.stateMItem)
        self.addMenu(self.editMItem)
        self.addMenu(self.fileMItem)

        self.loadMenuAction=QAction('&Load')
        self.stateMItem.addAction(self.loadMenuAction)

        self.saveMenuAction=QAction('&Save')
        self.stateMItem.addAction(self.saveMenuAction)

        # self.dropdownMenu=QMenu('&Dropdown')
        # self.dropdownMenu.addAction('&Option 1')
        # self.dropdownMenu.addAction('&Option 2')
        # self.dropdownMenu.addAction('&Option 3')
        #
        # self.editMItem.addMenu(self.dropdownMenu)

        self.openFileAction=QAction('&Open')
        self.fileMItem.addAction(self.openFileAction)

        self.editColorAction=QAction('Edit color')
        self.editMItem.addAction(self.editColorAction)
        self.editColorAction.triggered.connect(self.editColor)

    def editColor(self):
        self.dialog=QColorDialog(parent=self)
        self.dialog.open()








