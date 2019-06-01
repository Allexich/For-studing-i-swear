#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qw
import time

class MainWindow(qw.QWidget):
    cnt = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('( ͡° ͜ʖ ͡°)')

        self.goBtn = qw.QPushButton('Increase count', self)
        self.goBtn.move(50, 50)
        self.goBtn.clicked.connect(self.inc)

        self.goBtn = qw.QPushButton('Decrease count', self)
        self.goBtn.move(50, 100)
        self.goBtn.clicked.connect(self.dec)

        self.goBtn = qw.QPushButton('Print', self)
        self.goBtn.move(50, 150)
        self.goBtn.clicked.connect(self.out)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(50, 200)
        self.quitBtn.clicked.connect(self.close)

    def inc(self):
        self.cnt += 1

    def dec(self):
        self.cnt -= 1

    def out(self):
        print(self.cnt);
        



if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
