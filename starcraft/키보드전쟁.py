import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import pandas as pd
import mpl_finance as matfin
import matplotlib.ticker as ticker

import numpy as np
from time import sleep
import pyautogui
import threading

import win32com.shell.shell as shell

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(r"키보드전쟁.ui")[0]

#화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_loop_flag = False

        self.pushButton_start.clicked.connect(self.pushButton_start_clicked)
        self.pushButton_stop.clicked.connect(self.pushButton_stop_clicked)
        self.str_list = []

       # self.pushButton_Re.clicked.connect(self.pushButton_Re_clicked)
        # TR ID를 저장해놓고 처리할 딕셔너리 생성

    def pushButton_stop_clicked(self):
        self.start_loop_flag = False

    def pushButton_start_clicked(self):
        self.start_loop_flag = True
        self.str_list = list(map(str, self.lineEdit_input.text()))
        list_tmp = []
        for item in self.str_list:

            #문자열 치환
            item_mod = item.replace(" ", "space")

            # 새로운 리스트에 추가
            list_tmp.append(item_mod)
        self.str_list = list_tmp
        t = threading.Thread(target=self.auto_chat)
        t.start()

    def auto_chat(self):
        while self.start_loop_flag:
            sleep(0.9)
            pyautogui.typewrite(['enter'])
            pyautogui.typewrite(self.str_list)
            pyautogui.typewrite(['enter'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
