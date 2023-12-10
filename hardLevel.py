from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
import csv
import operator
from completeWin import complete

class HardWindow(QMainWindow):
    def __init__(self, parent):
        super(HardWindow, self).__init__(parent)
        uic.loadUi("hard.ui", self)

        self.match = ["gengar","gengar","eevee","eevee","psyduck","psyduck","squirtle","squirtle",
                      "togepi","togepi","piplup","piplup","jigglypuff","jigglypuff","totodile","totodile",
                      "cubone","cubone","snorlax","snorlax","marill","marill","ditto","ditto",
                      "mudkip","mudkip", "froakie", "froakie", "gible","gible", "dragonite", "dragonite",
                      "bidoof","bidoof", "crustle", "crustle", "vaporeon", "vaporeon", "slowbro", "slowbro",
                      "pikachu","pikachu","sandshrew","sandshrew", "rattata","rattata", "shinx","shinx",
                      "oddish","oddish","meowth","meowth","morpeko","morpeko","scorbunny","scorbunny",
                      "absol","absol","articuno","articuno","machamp","machamp","pancham","pancham"]
        random.shuffle(self.match)

        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        self.button11 = self.findChild(QPushButton, "pushButton_11")
        self.button12 = self.findChild(QPushButton, "pushButton_12")
        self.button13 = self.findChild(QPushButton, "pushButton_13")
        self.button14 = self.findChild(QPushButton, "pushButton_14")
        self.button15 = self.findChild(QPushButton, "pushButton_15")
        self.button16 = self.findChild(QPushButton, "pushButton_16")
        self.button17 = self.findChild(QPushButton, "pushButton_17")
        self.button18 = self.findChild(QPushButton, "pushButton_18")
        self.button19 = self.findChild(QPushButton, "pushButton_19")
        self.button20 = self.findChild(QPushButton, "pushButton_20")
        self.button21 = self.findChild(QPushButton, "pushButton_21")
        self.button22 = self.findChild(QPushButton, "pushButton_22")
        self.button23 = self.findChild(QPushButton, "pushButton_23")
        self.button24 = self.findChild(QPushButton, "pushButton_24")
        self.button25 = self.findChild(QPushButton, "pushButton_25")
        self.button26 = self.findChild(QPushButton, "pushButton_26")
        self.button27 = self.findChild(QPushButton, "pushButton_27")
        self.button28 = self.findChild(QPushButton, "pushButton_28")
        self.button29 = self.findChild(QPushButton, "pushButton_29")
        self.button30 = self.findChild(QPushButton, "pushButton_30")
        self.button31 = self.findChild(QPushButton, "pushButton_31")
        self.button32 = self.findChild(QPushButton, "pushButton_32")
        self.button33 = self.findChild(QPushButton, "pushButton_33")
        self.button34 = self.findChild(QPushButton, "pushButton_34")
        self.button35 = self.findChild(QPushButton, "pushButton_35")
        self.button36 = self.findChild(QPushButton, "pushButton_36")
        self.button37 = self.findChild(QPushButton, "pushButton_37")
        self.button38 = self.findChild(QPushButton, "pushButton_38")
        self.button39 = self.findChild(QPushButton, "pushButton_39")
        self.button40 = self.findChild(QPushButton, "pushButton_40")
        self.button41 = self.findChild(QPushButton, "pushButton_41")
        self.button42 = self.findChild(QPushButton, "pushButton_42")
        self.button43 = self.findChild(QPushButton, "pushButton_43")
        self.button44 = self.findChild(QPushButton, "pushButton_44")
        self.button45 = self.findChild(QPushButton, "pushButton_45")
        self.button46 = self.findChild(QPushButton, "pushButton_46")
        self.button47 = self.findChild(QPushButton, "pushButton_47")
        self.button48 = self.findChild(QPushButton, "pushButton_48")
        self.button49 = self.findChild(QPushButton, "pushButton_49")
        self.button50 = self.findChild(QPushButton, "pushButton_50")
        self.button51 = self.findChild(QPushButton, "pushButton_51")
        self.button52 = self.findChild(QPushButton, "pushButton_52")
        self.button53 = self.findChild(QPushButton, "pushButton_53")
        self.button54 = self.findChild(QPushButton, "pushButton_54")
        self.button55 = self.findChild(QPushButton, "pushButton_55")
        self.button56 = self.findChild(QPushButton, "pushButton_56")
        self.button57 = self.findChild(QPushButton, "pushButton_57")
        self.button58 = self.findChild(QPushButton, "pushButton_58")
        self.button59 = self.findChild(QPushButton, "pushButton_59")
        self.button60 = self.findChild(QPushButton, "pushButton_60")
        self.button61 = self.findChild(QPushButton, "pushButton_61")
        self.button62 = self.findChild(QPushButton, "pushButton_62")
        self.button63 = self.findChild(QPushButton, "pushButton_63")
        self.button64 = self.findChild(QPushButton, "pushButton_64")

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
        self.button17.clicked.connect(lambda: self.button_onClick(self.button17, 16))
        self.button18.clicked.connect(lambda: self.button_onClick(self.button18, 17))
        self.button19.clicked.connect(lambda: self.button_onClick(self.button19, 18))
        self.button20.clicked.connect(lambda: self.button_onClick(self.button20, 19))
        self.button21.clicked.connect(lambda: self.button_onClick(self.button21, 20))
        self.button22.clicked.connect(lambda: self.button_onClick(self.button22, 21))
        self.button23.clicked.connect(lambda: self.button_onClick(self.button23, 22))
        self.button24.clicked.connect(lambda: self.button_onClick(self.button24, 23))
        self.button25.clicked.connect(lambda: self.button_onClick(self.button25, 24))
        self.button26.clicked.connect(lambda: self.button_onClick(self.button26, 25))
        self.button27.clicked.connect(lambda: self.button_onClick(self.button27, 26))
        self.button28.clicked.connect(lambda: self.button_onClick(self.button28, 27))
        self.button29.clicked.connect(lambda: self.button_onClick(self.button29, 28))
        self.button30.clicked.connect(lambda: self.button_onClick(self.button30, 29))
        self.button31.clicked.connect(lambda: self.button_onClick(self.button31, 30))
        self.button32.clicked.connect(lambda: self.button_onClick(self.button32, 31))
        self.button33.clicked.connect(lambda: self.button_onClick(self.button33, 32))
        self.button34.clicked.connect(lambda: self.button_onClick(self.button34, 33))
        self.button35.clicked.connect(lambda: self.button_onClick(self.button35, 34))
        self.button36.clicked.connect(lambda: self.button_onClick(self.button36, 35))
        self.button37.clicked.connect(lambda: self.button_onClick(self.button37, 36))
        self.button38.clicked.connect(lambda: self.button_onClick(self.button38, 37))
        self.button39.clicked.connect(lambda: self.button_onClick(self.button39, 38))
        self.button40.clicked.connect(lambda: self.button_onClick(self.button40, 39))
        self.button41.clicked.connect(lambda: self.button_onClick(self.button41, 40))
        self.button42.clicked.connect(lambda: self.button_onClick(self.button42, 41))
        self.button43.clicked.connect(lambda: self.button_onClick(self.button43, 42))
        self.button44.clicked.connect(lambda: self.button_onClick(self.button44, 43))
        self.button45.clicked.connect(lambda: self.button_onClick(self.button45, 44))
        self.button46.clicked.connect(lambda: self.button_onClick(self.button46, 45))
        self.button47.clicked.connect(lambda: self.button_onClick(self.button47, 46))
        self.button48.clicked.connect(lambda: self.button_onClick(self.button48, 47))
        self.button49.clicked.connect(lambda: self.button_onClick(self.button49, 48))
        self.button50.clicked.connect(lambda: self.button_onClick(self.button50, 49))
        self.button51.clicked.connect(lambda: self.button_onClick(self.button51, 50))
        self.button52.clicked.connect(lambda: self.button_onClick(self.button52, 51))
        self.button53.clicked.connect(lambda: self.button_onClick(self.button53, 52))
        self.button54.clicked.connect(lambda: self.button_onClick(self.button54, 53))
        self.button55.clicked.connect(lambda: self.button_onClick(self.button55, 54))
        self.button56.clicked.connect(lambda: self.button_onClick(self.button56, 55))
        self.button57.clicked.connect(lambda: self.button_onClick(self.button57, 56))
        self.button58.clicked.connect(lambda: self.button_onClick(self.button58, 57))
        self.button59.clicked.connect(lambda: self.button_onClick(self.button59, 58))
        self.button60.clicked.connect(lambda: self.button_onClick(self.button60, 59))
        self.button61.clicked.connect(lambda: self.button_onClick(self.button61, 60))
        self.button62.clicked.connect(lambda: self.button_onClick(self.button62, 61))
        self.button63.clicked.connect(lambda: self.button_onClick(self.button63, 62))
        self.button64.clicked.connect(lambda: self.button_onClick(self.button64, 63))
        
        self.button_list = [self.button1, self.button2, self.button3, self.button4, 
                            self.button5, self.button6, self.button7, self.button8, 
                            self.button9, self.button10, self.button11, self.button12,
                            self.button13, self.button14, self.button15, self.button16,
                            self.button17, self.button18, self.button19, self.button20,
                            self.button21, self.button22, self.button23, self.button24, 
                            self.button25, self.button26, self.button27, self.button28, 
                            self.button29, self.button30, self.button31, self.button32,
                            self.button33, self.button34, self.button35, self.button36,
                            self.button37, self.button38, self.button39, self.button40,
                            self.button41, self.button42, self.button43, self.button44, 
                            self.button45, self.button46, self.button47, self.button48, 
                            self.button49, self.button50, self.button51, self.button52,
                            self.button53, self.button54, self.button55, self.button56,
                            self.button57, self.button58, self.button59, self.button60,
                            self.button61, self.button62, self.button63, self.button64]
        
        self.topScore = self.findChild(QLabel, "topScore")

        with open('hardLeaderboard.csv', 'r', newline='') as file:
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
                if self.flipped == 32:
                    self.timer.stop()

                    timerec = self.time.text()
                    self.done.timeLabel.setText(timerec)
                    self.done.exec_()
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
        with open('hardLeaderboard.csv', 'r', newline='') as file:
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

            with open('hardLeaderboard.csv','a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)

            self.done.addButton.setEnabled(False)
            self.sortNewData()

    def sortNewData(self):
        data = csv.reader(open('hardLeaderboard.csv'),delimiter=',')
        data = sorted(data, key=operator.itemgetter(1), reverse=False)

        with open('hardLeaderboard.csv','w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)