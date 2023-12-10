from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic


class complete(QDialog):
    def __init__(self, parent):
        super(complete, self).__init__(parent)
        uic.loadUi("complete.ui", self)

        self.timeLabel = self.findChild(QLabel, "timeLabel")
        self.menuButton = self.findChild(QPushButton, "pushButton")
        self.restartButton = self.findChild(QPushButton, "pushButton_2")
        self.addButton = self.findChild(QPushButton, "addButton")
        self.name = self.findChild(QLineEdit, "lineEdit")
    

