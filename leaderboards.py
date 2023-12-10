from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import csv

class Leaderboards(QMainWindow):
    def __init__(self, parent):
        super(Leaderboards, self).__init__(parent)
        uic.loadUi("leaderboards.ui", self)

        self.easyTable = self.findChild(QTableView, "tableWidget")
        self.mediumTable = self.findChild(QTableView, "tableWidget_2")
        self.hardTable = self.findChild(QTableView, "tableWidget_3")
        self.backButton = self.findChild(QPushButton, "pushButton")

        self.backButton.clicked.connect(self.back)

        self.easyTable.setHorizontalHeaderLabels(('Name','Time'))
        self.mediumTable.setHorizontalHeaderLabels(('Name','Time'))
        self.hardTable.setHorizontalHeaderLabels(('Name','Time'))

        row_index1 = 0
        with open('easyLeaderboard.csv', 'r', newline='') as file:
            scores = list(csv.reader(file))
            for score in scores:
                self.easyTable.setItem(row_index1,0,QTableWidgetItem(score[0]))
                self.easyTable.setItem(row_index1,1,QTableWidgetItem(score[1]))
                row_index1 += 1
        
        row_index2 = 0
        with open('mediumLeaderboard.csv', 'r', newline='') as file:
            scores = list(csv.reader(file))
            for score in scores:
                self.mediumTable.setItem(row_index2,0,QTableWidgetItem(score[0]))
                self.mediumTable.setItem(row_index2,1,QTableWidgetItem(score[1]))
                row_index2 += 1
        
        row_index3 = 0
        with open('hardLeaderboard.csv', 'r', newline='') as file:
            scores = list(csv.reader(file))
            for score in scores:
                self.hardTable.setItem(row_index3,0,QTableWidgetItem(score[0]))
                self.hardTable.setItem(row_index3,1,QTableWidgetItem(score[1]))
                row_index3 += 1

    def back(self):
        self.close()
        self.parent().show()