"""
Исходный код
Author: Berrouba.A
Last edited: 21 Feb 2018
Доработка и использование данного кода  + глобальное дописание функционала - я, Onixilium
"""
# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QDrag

# import Opencv module
import cv2
import numpy as np

import mainscreen
from mainscreen import *


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)


class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)  # кнопка - Start - начинает показ видео с вебкамеры
        self.ui.pushButton.clicked.connect(self.record)  # кнопка - Record - начинает запись

        # переключение вебкамеры в реалтайме c помощью комбо бокса КОСТЫЛИЩЕ - функция проверяет
        # изменение комбо бокса и нажимает ВЫКЛЮЧИТЬ текущую камеру, потом включить, поэтому 2 строки
        # работает только если нажат старт
        self.ui.comboBox.currentIndexChanged.connect(self.controlTimer)
        self.ui.comboBox.currentIndexChanged.connect(self.controlTimer)
        self.flagrecord = False  # Флаг для проверки состояния кнопки - Record

        self.ui.pushButton_2.clicked.connect(self.newcam)


    # view camera
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB30)
        # show image in img_label
        a=self.ui.image_label2
        a.setPixmap(QPixmap.fromImage(qImg))
       # self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))
       # self.ui.image_label2.setPixmap(QPixmap.fromImage(qImg)) #подключение второго окна

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(self.ui.comboBox.currentIndex()) #выбор камеры через комбобокс
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            # self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")

    def record(self):
        if self.flagrecord == False:
            self.ui.pushButton.setText("Stop record")
            self.flagrecord = True

            if (self.cap.isOpened() == False):
                print("Unable to read camera feed")
            else:
                print("Camera start record")

            frame_width = int(self.cap.get(3))
            frame_height = int(self.cap.get(4))

            self.out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 24, (frame_width, frame_height))

            while (True):
                ret, frame = self.cap.read()
                if (ret == True):
                    self.out.write(frame)
                if cv2.waitKey(1) & 0xFF == ord('q') or 0xFF == ord('Q'):
                    break

        else:
            self.ui.pushButton.setText("Record")
            print("Camera stop record")
            self.flagrecord = False
            # self.cap.release()
            self.out.release()

    def newcam(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(555, 333)

    def initUI(self):
        self.setAcceptDrops(True)
        self.button =  Button('pushButton_5', self)
        self.button.move(0, 0)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create and show mainWindow
    mainWindow = Ui_Form()
    sys.exit(app.exec_())