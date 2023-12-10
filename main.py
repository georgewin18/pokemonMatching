import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from easyLevel import EasyWindow
from mediumLevel import MediumWindow
from hardLevel import HardWindow
from leaderboards import Leaderboards

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("menu.ui", self)

        self.easyButton = self.findChild(QPushButton, "easyButton")
        self.mediumButton = self.findChild(QPushButton, "mediumButton")
        self.hardButton = self.findChild(QPushButton, "hardButton")
        self.leaderboardButton = self.findChild(QPushButton, "leaderboardButton")

        self.easyButton.clicked.connect(self.startEasy)
        self.mediumButton.clicked.connect(self.startMedium)
        self.hardButton.clicked.connect(self.startHard)
        self.leaderboardButton.clicked.connect(self.showLeaderboard)

        self.show()

    def startEasy(self):
        self.hide()
        self.easy = EasyWindow(self)
        self.easy.show()
    
    def startMedium(self):
        self.hide()
        self.medium = MediumWindow(self)
        self.medium.show()
    
    def startHard(self):
        self.hide()
        self.hard = HardWindow(self)
        self.hard.show()

    def showLeaderboard(self):
        self.hide()
        self.leaderboards = Leaderboards(self)
        self.leaderboards.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=MainWindow()
    sys.exit(app.exec_())