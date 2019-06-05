#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtWidgets as qw
import time

from requests import get


class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Get IP')

        self.goBtn = qw.QPushButton('Go', self)
        self.goBtn.move(50, 50)
        self.goBtn.clicked.connect(self.get_ip)

        self.label = qw.QLabel(' ' * 40, self)
        self.label.move(50,100)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(50, 150)
        self.quitBtn.clicked.connect(self.close)
    
    def get_ip(self, evt):
        ip = get('https://ident.me').text
        self.label.setText(str(ip))


if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
