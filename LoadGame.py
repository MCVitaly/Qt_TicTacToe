from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLabel
from PyQt6.QtGui import QPixmap
import json

parent=None
gameField=None
playerX=None
playerY=None
def getGameComponetsToLoad(_parent, _gameField, _playerX, _playerY):
    global parent, gameField, playerX, playerY
    parent=_parent
    gameField = _gameField
    playerX=_playerX
    playerY=_playerY

def loadGame():
    with open('test_file.json', 'r') as file:
        dataToLoad=json.load(file)

    global parent, gameField, playerX, playerY

    playerX.playerName.setText(dataToLoad['playerX']['name'])
    playerX.pixmap = QPixmap(dataToLoad['playerX']['picturePath'])
    playerX.pixmap = playerX.pixmap.scaled(300, 300)
    playerX.playerPicture.setPixmap(playerX.pixmap)
    playerX.label.setStyleSheet(dataToLoad['playerX']['styleSheet'])

    playerY.playerName.setText(dataToLoad['playerY']['name'])
    playerY.pixmap = QPixmap(dataToLoad['playerY']['picturePath'])
    playerY.pixmap = playerY.pixmap.scaled(300, 300)
    playerY.playerPicture.setPixmap(playerY.pixmap)
    playerY.label.setStyleSheet(dataToLoad['playerY']['styleSheet'])


    gameField.currentPlayer=dataToLoad['gameField']['currentPlayer']
    gameField.accessToAllButtons_flag=dataToLoad['gameField']['accessToAllButtons_flag']
    gameField.didFirstClickBe= dataToLoad['gameField']['didFirstClickBe']
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    gameField.cells[i][j].buttons[k][l].access=dataToLoad['gameField']['cells'][i][j][k][l]['access']
                    gameField.cells[i][j].buttons[k][l].setText(dataToLoad['gameField']['cells'][i][j][k][l]['text'])
                    gameField.cells[i][j].buttons[k][l].setStyleSheet(dataToLoad['gameField']['cells'][i][j][k][l]['styleSheet'])
                    gameField.cells[i][j].buttons[k][l].isEnabled = dataToLoad['gameField']['cells'][i][j][k][l]['isEnabled']

    for i in range(3):
        for j in range(3):
            if dataToLoad['gameField']['bigCrossAndZero_matrix'][i][j] is None:
                gameField.bigCrossAndZero_matrix[i][j]=None
            else:
                gameField.bigCrossAndZero_matrix[i][j].symbol=dataToLoad['gameField']['bigCrossAndZero_matrix'][i][j]