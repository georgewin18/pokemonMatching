from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
import csv
import operator
from completeWin import complete

class EasyWindow(QMainWindow):
    def __init__(self, parent):
        super(EasyWindow, self).__init__(parent)
        uic.loadUi("easy.ui", self)

        self.match = ["gengar","gengar","eevee","eevee","psyduck","psyduck","squirtle","squirtle",
                      "togepi","togepi","piplup","piplup","jigglypuff","jigglypuff","totodile","totodile"]
        random.shuffle(self.match)

        self.button1 = self.findChild(QPushButton, "button1")
        self.button2 = self.findChild(QPushButton, "button2")
        self.button3 = self.findChild(QPushButton, "button3")
        self.button4 = self.findChild(QPushButton, "button4")
        self.button5 = self.findChild(QPushButton, "button5")
        self.button6 = self.findChild(QPushButton, "button6")
        self.button7 = self.findChild(QPushButton, "button7")
        self.button8 = self.findChild(QPushButton, "button8")
        self.button9 = self.findChild(QPushButton, "button9")
        self.button10 = self.findChild(QPushButton, "button10")
        self.button11 = self.findChild(QPushButton, "button11")
        self.button12 = self.findChild(QPushButton, "button12")
        self.button13 = self.findChild(QPushButton, "button13")
        self.button14 = self.findChild(QPushButton, "button14")
        self.button15 = self.findChild(QPushButton, "button15")
        self.button16 = self.findChild(QPushButton, "button16")

        self.time = self.findChild(QLabel, "timer")

        self.button1.clicked.connect(lambda: self.button_onClick(self.button1, 0))
        self.button2.clicked.connect(lambda: self.button_onClick(self.button2, 1))
        self.button3.clicked.connect(lambda: self.button_onClick(self.button3, 2))
        self.button4.clicked.connect(lambda: self.button_onClick(self.button4, 3))
        self.button5.clicked.connect(lambda: self.button_onClick(self.button5, 4))
        self.button6.clicked.connect(lambda: self.button_onClick(self.button6, 5))
        self.button7.clicked.connect(lambda: self.button_onClick(self.button7, 6))
        self.button8.clicked.connect(lambda: self.button_onClick(self.button8, 7))
        self.button9.clicked.connect(lambda: self.button_onClick(self.button9, 8))
        self.button10.clicked.connect(lambda: self.button_onClick(self.button10, 9))
        self.button11.clicked.connect(lambda: self.button_onClick(self.button11, 10))
        self.button12.clicked.connect(lambda: self.button_onClick(self.button12, 11))
        self.button13.clicked.connect(lambda: self.button_onClick(self.button13, 12))
        self.button14.clicked.connect(lambda: self.button_onClick(self.button14, 13))
        self.button15.clicked.connect(lambda: self.button_onClick(self.button15, 14))
        self.button16.clicked.connect(lambda: self.button_onClick(self.button16, 15))

        self.button_list = [self.button1, self.button2, self.button3, self.button4, 
                            self.button5, self.button6, self.button7, self.button8, 
                            self.button9, self.button10, self.button11, self.button12,
                            self.button13, self.button14, self.button15, self.button16]

        self.topScore = self.findChild(QLabel, "topScore")

        with open('easyLeaderboard.csv', 'r', newline='') as file:
            leaderBoard = list(csv.reader(file))
            self.topScore.setText(f"{leaderBoard[0][0]}-{leaderBoard[0][1]}")

        self.count = 0
        self.ans_list = []
        self.ans_dict = {}
        self.flipped = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.c = 1

        self.seconds = 0
        self.minutes = 0
        self.hours = 0

        self.done = complete(self)
        self.done.menuButton.clicked.connect(self.backToMain)
        self.done.restartButton.clicked.connect(self.restart)
        self.done.addButton.clicked.connect(self.addRecord)

        self.show()

    def button_onClick(self, button, num):
        if (self.count < 2):
            button.setStyleSheet(f"background-image : url(images/{self.match[num]}.png); background-repeat : no repeat; background-position : center;")
            self.ans_list.append(num)
            self.ans_dict[button] = self.match[num]
            button.setEnabled(False)
            self.count += 1
        
        if len(self.ans_dict) == 2:
            if self.match[self.ans_list[0]] == self.match[self.ans_list[1]]:
                for key in self.ans_dict:
                    key.setEnabled(False)
                self.flipped += 1
                self.count = 0
                self.ans_list = []
                self.ans_dict = {}
                if self.flipped == 8:
                    self.timer.stop()

                    timerec = self.time.text()
                    self.done.timeLabel.setText(timerec)
                    self.done.show()
            else:
                self.timer2 = QTimer()
                self.timer2.timeout.connect(self.wait)
                self.timer2.start(1000)

    def wait(self):
        self.c -= 1
        if self.c <= 0:
            self.flipback()
            self.timer2.stop()
    
    def flipback(self):
        for key in self.ans_dict:
            key.setStyleSheet("")
            key.setEnabled(True)
        self.count = 0
        self.ans_list = []
        self.ans_dict = {}

    def updateTime(self):
        self.time.setText(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
        
        self.seconds += 1

        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
        
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1

    def backToMain(self):
        self.close()
        self.done.close()
        self.parent().show()

    def restart(self):
        random.shuffle(self.match)
        self.time.setText("00:00:00")
        self.timer.start(1000)
        self.count = 0
        self.ans_list = []
        self.ans_dict = {}
        self.flipped = 0
        self.c = 1
        for button in self.button_list:
            button.setStyleSheet("")
            button.setEnabled(True)
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        with open('easyLeaderboard.csv', 'r', newline='') as file:
            leaderBoard = list(csv.reader(file))
            self.topScore.setText(f"{leaderBoard[0][0]}-{leaderBoard[0][1]}")
        self.done.name.setText("")
        self.done.addButton.setEnabled(True)
        self.done.close()
    
    def addRecord(self):
        if self.done.name.text() != "":
            name = self.done.name.text()
            time = self.time.text()
            new_data = [[name, time]]

            with open('easyLeaderboard.csv','a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)

            self.done.addButton.setEnabled(False)
            self.sortNewData()

    def sortNewData(self):
        data = csv.reader(open('easyLeaderboard.csv'),delimiter=',')
        data = sorted(data, key=operator.itemgetter(1), reverse=False)

        with open('easyLeaderboard.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        