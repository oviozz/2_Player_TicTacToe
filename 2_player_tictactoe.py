from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Made by Prajwal")
        MainWindow.resize(476, 688)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-10, -30, 491, 711))
        self.stackedWidget.setStyleSheet("background-color: rgb(27, 27, 77);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.player_onename = QtWidgets.QLineEdit(self.page)
        self.player_onename.setGeometry(QtCore.QRect(130, 270, 271, 41))
        self.player_onename.setStyleSheet("""

        background-color: rgb(16, 16, 50);
        font: 12pt "MS Shell Dlg 2";
        color: rgb(255, 255, 255);
        border-style: outset;
        border-width: 1px;
        border-radius: 7px;
        border-color: white;

                """)
        self.player_onename.setInputMask("")
        self.player_onename.setText("")
        self.player_onename.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.player_onename.setDragEnabled(False)
        self.player_onename.setReadOnly(False)
        self.player_onename.setObjectName("player_onename")

        self.player_twoname = QtWidgets.QLineEdit(self.page)
        self.player_twoname.setGeometry(QtCore.QRect(130, 320, 271, 41))
        self.player_twoname.setStyleSheet("""

                background-color: rgb(16, 16, 50);
                font: 12pt "MS Shell Dlg 2";
                color: rgb(255, 255, 255);
                border-style: outset;
                border-width: 1px;
                border-radius: 7px;
                border-color: white;

                        """)
        self.player_twoname.setObjectName("player_twoname")

        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(90, 270, 31, 41))
        self.label_2.setStyleSheet("font: 75 25pt \"Century Gothic\";\n"
                                   "color: rgb(255, 77, 64);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(90, 320, 31, 41))
        self.label_3.setStyleSheet("font: 75 25pt \"Century Gothic\";\n"
                                   "color: rgb(247, 205, 67)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.startbutton = QtWidgets.QPushButton(self.page)
        self.startbutton.setGeometry(QtCore.QRect(150, 380, 231, 51))
        self.startbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startbutton.setStyleSheet("background-color: rgb(0, 153, 203);\n"
                                       "font: 75 15pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255, 255, 255)\n"
                                       "")
        self.startbutton.setObjectName("startbutton")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(110, 210, 291, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 75 25pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.secondplayer = QtWidgets.QLabel(self.page_2)
        self.secondplayer.setGeometry(QtCore.QRect(300, 100, 91, 81))
        self.secondplayer.setStyleSheet("font: 75 50pt \"Century Gothic\";\n"
                                        "color: rgb(247, 205, 67);\n"
                                        "background-color: rgb(16, 16, 50);\n"
                                        "border: 2px solid dark purple;")
        self.secondplayer.setAlignment(QtCore.Qt.AlignCenter)
        self.secondplayer.setObjectName("secondplayer")
        self.firstplayer = QtWidgets.QLabel(self.page_2)
        self.firstplayer.setGeometry(QtCore.QRect(110, 100, 91, 81))
        self.firstplayer.setStyleSheet("font: 75 35pt \"Century Gothic\";\n"
                                       "background-color: rgb(16, 16, 50);\n"
                                       "color: rgb(231, 28, 76);"
                                       "border: 2px solid dark red;")
        self.firstplayer.setAlignment(QtCore.Qt.AlignCenter)
        self.firstplayer.setObjectName("firstplayer")
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 230, 391, 381))
        self.gridLayoutWidget.setMinimumSize(QtCore.QSize(100, 120))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.four = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.four.setMinimumSize(QtCore.QSize(100, 120))
        self.four.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "font: 75 35pt \"Century Gothic\";\n"
                                "")
        self.four.setObjectName("four")
        self.gridLayout.addWidget(self.four, 1, 0, 1, 1)
        self.two = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.two.setMinimumSize(QtCore.QSize(100, 120))
        self.two.setStyleSheet(
                               "color: rgb(247, 205, 67);\n"
                               "font: 75 35pt \"Century Gothic\";\n"
                               "")
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 0, 1, 1, 1)
        self.five = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.five.setMinimumSize(QtCore.QSize(100, 120))
        self.five.setStyleSheet(
                                "color: rgb(255, 255, 255);\n"
                                "font: 75 35pt \"Century Gothic\";\n"
                                "")
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 1, 1, 1, 1)
        self.three = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.three.setMinimumSize(QtCore.QSize(100, 120))
        self.three.setStyleSheet(
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 35pt \"Century Gothic\";\n"
                                 "")
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 0, 2, 1, 1)
        self.one = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.one.setMinimumSize(QtCore.QSize(100, 120))
        self.one.setAutoFillBackground(False)
        self.one.setStyleSheet("font: 75 35pt \"Century Gothic\";\n"
                               "color:  rgb(231, 28, 76);\n"
                               "")
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 0, 0, 1, 1)
        self.six = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.six.setMinimumSize(QtCore.QSize(100, 120))
        self.six.setStyleSheet(
                               "color: rgb(255, 255, 255);\n"
                               "font: 75 35pt \"Century Gothic\";\n"
                               "")
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 1, 2, 1, 1)
        self.seven = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.seven.setMinimumSize(QtCore.QSize(100, 120))
        self.seven.setStyleSheet(
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 35pt \"Century Gothic\";\n"
                                 "")
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 2, 0, 1, 1)
        self.eight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eight.setMinimumSize(QtCore.QSize(100, 120))
        self.eight.setStyleSheet(
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 75 35pt \"Century Gothic\";\n"
                                 "")
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 2, 1, 1, 1)
        self.nine = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nine.setMinimumSize(QtCore.QSize(100, 120))
        self.nine.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "font: 75 35pt \"Century Gothic\";\n"
                                "")
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 2, 2, 1, 1)
        self.playerone_label = QtWidgets.QLabel(self.page_2)
        self.playerone_label.setGeometry(QtCore.QRect(90, 70, 131, 20))
        self.playerone_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 75 13pt \"MS Sans Serif\";")
        self.playerone_label.setAlignment(QtCore.Qt.AlignCenter)
        self.playerone_label.setObjectName("playerone_label")
        self.playertwo_label = QtWidgets.QLabel(self.page_2)
        self.playertwo_label.setGeometry(QtCore.QRect(280, 70, 131, 20))
        self.playertwo_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                           "font: 75 13pt \"MS Sans Serif\";")
        self.playertwo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.playertwo_label.setObjectName("playertwo_label")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 411, 401))
        self.label_4.setStyleSheet("background-color: rgb(33, 33, 103);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.secondplayer.raise_()
        self.firstplayer.raise_()
        self.gridLayoutWidget.raise_()
        self.playerone_label.raise_()
        self.playertwo_label.raise_()
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startbutton.clicked.connect(self.change_screen)
        self.startbutton.clicked.connect(self.name_update)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Made by Prajwal"))
        self.player_twoname.setPlaceholderText(_translate("MainWindow", "   Player Two"))
        self.player_onename.setPlaceholderText(_translate("MainWindow", "   Player One"))
        self.label_2.setText(_translate("MainWindow", "X"))
        self.label_3.setText(_translate("MainWindow", "O"))
        self.startbutton.setText(_translate("MainWindow", "Start "))
        self.label.setText(_translate("MainWindow", "Enter Player Names"))
        self.secondplayer.setText(_translate("MainWindow", "O"))
        self.firstplayer.setText(_translate("MainWindow", "X"))
        self.four.setText(_translate("MainWindow", ""))
        self.two.setText(_translate("MainWindow", ""))
        self.five.setText(_translate("MainWindow", ""))
        self.three.setText(_translate("MainWindow", ""))
        self.one.setText(_translate("MainWindow", ""))
        self.six.setText(_translate("MainWindow", ""))
        self.seven.setText(_translate("MainWindow", ""))
        self.eight.setText(_translate("MainWindow", ""))
        self.nine.setText(_translate("MainWindow", ""))
        self.playerone_label.setText(_translate("MainWindow", "Player One"))
        self.playertwo_label.setText(_translate("MainWindow", "Player Two"))

        self.one.clicked.connect(partial(self.x, 'one'))

        self.two.clicked.connect(partial(self.x, 'two'))

        self.three.clicked.connect(partial(self.x, 'three'))

        self.four.clicked.connect(partial(self.x, 'four'))

        self.five.clicked.connect(partial(self.x, 'five'))

        self.six.clicked.connect(partial(self.x, 'six'))

        self.seven.clicked.connect(partial(self.x, 'seven'))

        self.eight.clicked.connect(partial(self.x, 'eight'))

        self.nine.clicked.connect(partial(self.x, 'nine'))

        self.turn = 1
        self.already_store = []

    def change_screen(self):
        self.stackedWidget.setCurrentIndex(1)

    def name_update(self):
        self.playerone_label.setText(self.player_onename.text())
        self.playertwo_label.setText(self.player_twoname.text())

    def x(self, button):
        if button not in self.already_store:

            self.already_store.append(button)
            self.check_Xbutton_pressed(button)

            if self.turn == 1:
                self.firstplayer.setStyleSheet("font: 75 35pt \"Century Gothic\";\n"
                                               "background-color: rgb(16, 16, 50);\n"
                                               "color: rgb(231, 28, 76);"
                                               )

                self.secondplayer.setStyleSheet("font: 75 35pt \"Century Gothic\";\n"
                                                "background-color: rgb(16, 16, 50);\n"
                                                "color: rgb(247, 205, 67);"
                                                "border: 2px solid dark purple;")

                self.check_Xbutton_pressed(button)
                self.win_x()
                self.end_game()
                self.turn = 2

            else:
                self.firstplayer.setStyleSheet("font: 75 35pt \"Century Gothic\";\n"
                                               "background-color: rgb(16, 16, 50);\n"
                                               "color: rgb(231, 28, 76);"
                                               "border: 2px solid dark red;")

                self.secondplayer.setStyleSheet("font: 75 35pt \"Century Gothic\";\n"
                                                "background-color: rgb(16, 16, 50);\n"
                                                "color: rgb(247, 205, 67);"
                                                )

                self.check_Obutton_pressed(button)
                self.win_o()
                self.end_game()
                self.turn = 1

    def check_Xbutton_pressed(self, value):
        if self.turn == 1:
            if value == 'one':
                self.one.setText('X')
                self.one.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                       "color:  rgb(231, 28, 76);\n"
                                       "font: 75 50pt \"Century Gothic\";\n"
                                       "")
            if value == 'two':
                self.two.setText('X')
                self.two.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                       "color:  rgb(231, 28, 76);\n"
                                       "font: 75 50pt \"Century Gothic\";\n"
                                       "")
            if value == 'three':
                self.three.setText('X')
                self.three.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                         "color:  rgb(231, 28, 76);\n"
                                         "font: 75 50pt \"Century Gothic\";\n"
                                         "")
            if value == 'four':
                self.four.setText('X')
                self.four.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                        "color:  rgb(231, 28, 76);\n"
                                        "font: 75 50pt \"Century Gothic\";\n"
                                        "")
            if value == 'five':
                self.five.setText('X')
                self.five.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                        "color:  rgb(231, 28, 76);\n"
                                        "font: 75 50pt \"Century Gothic\";\n"
                                        "")
            if value == 'six':
                self.six.setText('X')
                self.six.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                       "color:  rgb(231, 28, 76);\n"
                                       "font: 75 50pt \"Century Gothic\";\n"
                                       "")
            if value == 'seven':
                self.seven.setText('X')
                self.seven.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                         "color:  rgb(231, 28, 76);\n"
                                         "font: 75 50pt \"Century Gothic\";\n"
                                         "")
            if value == 'eight':
                self.eight.setText('X')
                self.eight.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                         "color:  rgb(231, 28, 76);\n"
                                         "font: 75 50pt \"Century Gothic\";\n"
                                         "")
            if value == 'nine':
                self.nine.setText('X')
                self.nine.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                        "color:  rgb(231, 28, 76);\n"
                                        "font: 75 50pt \"Century Gothic\";\n"
                                        "")

    def check_Obutton_pressed(self, value):
        if value == 'one':
            self.one.setText('O')
            return self.one.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                          "color:   rgb(247, 205, 67);\n"
                                          "font: 75 50pt \"Century Gothic\";\n"
                                          "")
        if value == 'two':
            self.two.setText('O')
            return self.two.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                          "color:   rgb(247, 205, 67);\n"
                                          "font: 75 50pt \"Century Gothic\";\n"
                                          "")
        if value == 'three':
            self.three.setText('O')
            return self.three.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                            "color:   rgb(247, 205, 67);\n"
                                            "font: 75 50pt \"Century Gothic\";\n"
                                            "")
        if value == 'four':
            self.four.setText('O')
            return self.four.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                           "color:   rgb(247, 205, 67);\n"
                                           "font: 75 50pt \"Century Gothic\";\n"
                                           "")
        if value == 'five':
            self.five.setText('O')
            return self.five.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                           "color:   rgb(247, 205, 67);\n"
                                           "font: 75 50pt \"Century Gothic\";\n"
                                           "")
        if value == 'six':
            self.six.setText('O')
            return self.six.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                          "color:   rgb(247, 205, 67);\n"
                                          "font: 75 50pt \"Century Gothic\";\n"
                                          "")
        if value == 'seven':
            self.seven.setText('O')
            return self.seven.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                            "color:   rgb(247, 205, 67);\n"
                                            "font: 75 50pt \"Century Gothic\";\n"
                                            "")
        if value == 'eight':
            self.eight.setText('O')
            return self.eight.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                            "color:   rgb(247, 205, 67);\n"
                                            "font: 75 50pt \"Century Gothic\";\n"
                                            "")
        if value == 'nine':
            self.nine.setText('O')
            return self.nine.setStyleSheet("background-color: rgb(16, 16, 50);\n"
                                           "color:   rgb(247, 205, 67);\n"
                                           "font: 75 50pt \"Century Gothic\";\n"
                                           "")

    def win_x(self):
        if (self.one.text() == 'X' and self.two.text() == 'X' and self.three.text() == 'X'):
            self.one.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.two.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.three.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")

            return self.win_game()

        elif (self.four.text() == 'X' and self.five.text() == 'X' and self.six.text() == 'X'):
            self.four.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.six.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            return self.win_game()


        elif (self.seven.text() == 'X' and self.eight.text() == 'X' and self.nine.text() == 'X'):
            self.seven.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.eight.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.nine.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            return self.win_game()


        elif (self.one.text() == 'X' and self.four.text() == 'X' and self.seven.text() == 'X'):
            self.one.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.four.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.seven.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            return self.win_game()


        elif (self.two.text() == 'X' and self.five.text() == 'X' and self.eight.text() == 'X'):
            self.two.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.eight.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            return self.win_game()


        elif (self.three.text() == 'X' and self.six.text() == 'X' and self.nine.text() == 'X'):
            self.three.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.six.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.nine.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            return self.win_game()


        elif (self.one.text() == 'X' and self.five.text() == 'X' and self.nine.text() == 'X'):
            self.one.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.nine.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            return self.win_game()


        elif (self.three.text() == 'X' and self.five.text() == 'X' and self.seven.text() == 'X'):
            self.three.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.seven.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            return self.win_game()

    def win_o(self):
        if (self.one.text() == 'O' and self.two.text() == 'O' and self.three.text() == 'O'):
            self.one.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.two.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.three.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")

            return self.win_game()


        elif (self.four.text() == 'O' and self.five.text() == 'O' and self.six.text() == 'O'):
            self.four.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.six.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")

            return self.win_game()



        elif (self.seven.text() == 'O' and self.eight.text() == 'O' and self.nine.text() == 'O'):
            self.seven.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.eight.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.nine.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")

            return self.win_game()


        elif (self.one.text() == 'O' and self.four.text() == 'O' and self.seven.text() == 'O'):
            self.one.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.four.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.seven.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")

            return self.win_game()



        elif (self.two.text() == 'O' and self.five.text() == 'O' and self.eight.text() == 'O'):
            self.two.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.eight.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            return self.win_game()


        elif (self.three.text() == 'O' and self.six.text() == 'O' and self.nine.text() == 'O'):
            self.three.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.six.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.nine.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            return self.win_game()

        elif (self.one.text() == 'O' and self.five.text() == 'O' and self.nine.text() == 'O'):
            self.one.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                   "color:   rgb(255, 255, 255);\n"
                                   "font: 75 50pt \"Century Gothic\";\n"
                                   "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.nine.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            return self.win_game()

        elif (self.three.text() == 'O' and self.five.text() == 'O' and self.seven.text() == 'O'):
            self.three.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            self.five.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                    "color:   rgb(255, 255, 255);\n"
                                    "font: 75 50pt \"Century Gothic\";\n"
                                    "")
            self.seven.setStyleSheet("background-color: rgb(89, 89, 255);\n"
                                     "color:   rgb(255, 255, 255);\n"
                                     "font: 75 50pt \"Century Gothic\";\n"
                                     "")
            return self.win_game()

            # add win last

    def win_game(self):
        msg = QtWidgets.QMessageBox()

        msg.setIcon(msg.Information)
        msg.setWindowTitle("Congratulation")
        msg.setText("Want to play Again? ")
        button1 = msg.addButton("Play Again ", QtWidgets.QMessageBox.YesRole)
        button2 = msg.addButton("Quit", QtWidgets.QMessageBox.AcceptRole)
        msg.setDefaultButton(button1)

        x = msg.exec_()

        if msg.clickedButton() == button1:
            return self.reboot()
        elif msg.clickedButton() == button2:
            return exit()


    def reboot(self):
        Ui_MainWindow.setupUi(self, MainWindow)


    def end_game(self):

        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Ehhhh")
        msg.setText("Want to play Again? ")
        button1 = msg.addButton("Play Again ", QtWidgets.QMessageBox.YesRole)
        button2 = msg.addButton("Quit", QtWidgets.QMessageBox.AcceptRole)
        msg.setDefaultButton(button1)

        if len(self.already_store) == 9:
            x = msg.exec_()
            if msg.clickedButton() == button1:
                return self.reboot()
            elif msg.clickedButton() == button2:
                return exit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
