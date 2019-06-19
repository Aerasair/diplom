import sys
# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QDialog, QApplication
from mainscreen import Ui_mainWindow
from settingswin import Ui_FormSet
import cv2
import numpy as np
from playerscreen import *
from users_window import *
import sqlite3
from PyQt5.QtMultimedia import (QAbstractVideoBuffer, QMediaContent,
        QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, Q_ARG, QAbstractItemModel,
        QFileInfo, qFuzzyCompare, QMetaObject, QModelIndex, QObject, Qt,
QThread, QTime, QUrl)
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from os import listdir
import random
from datetime import datetime
import shutil
import hashlib

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # self.showMaximized()
        self.show()
        # self.showFullScreen()
        # self.setWindowFlags(Qt.WindowTitleHint)
        self.setWindowFlags(Qt.CustomizeWindowHint)

        # create a timer
        self.timer = QTimer()
        self.timer2 = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(lambda: self.viewCam2(self.ui.label_5))
        self.timer.timeout.connect(lambda: self.viewCam(self.ui.label_4))
        self.controlTimer(1)
        self.controlTimer2(0)
        self.ui.btn_grid1.clicked.connect(self.win1)
        self.ui.btn_grid9.clicked.connect(self.win9)
        # self.ui.btn_rec1.clicked.connect(self.record)
        # self.ui.btn_stop1.clicked.connect(self.stoprecord)
        self.ui.pushButton.clicked.connect(self.openplayer)
        self.ui.login_text.textChanged.connect(self.login)
        self.ui.password_text.textChanged.connect(self.login)
        self.ui.btn_users.hide()#убираем кнопку пользователей
        self.ui.btn_users.clicked.connect(self.openuserswindows)
        self.ui.groupBox.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox_3.hide()
        self.ui.btn_name2.clicked.connect(self.openbox1)
        self.ui.btn_add_cam.clicked.connect(self.openbox3)
        self.ui.btn_open_gridbox.clicked.connect(self.openbox2)
        self.ui.btn_exit.clicked.connect(self.exitprogram)

        now = datetime.now()
        self.ui.texttimedate.setText(str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")))
        self.ui.pushButton_2.clicked.connect(self.opensettings)
        print(hashlib.md5("guest".encode('utf-8')).hexdigest())
        # self.ui.group_auth.hide()
        self.connection = sqlite3.connect('mydb.db')


    def viewCam(self, a):
        # read image in BGR format
        ret, image = self.cap.read()
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # a = self.ui.label_4
        a.setPixmap(QPixmap.fromImage(qImg))


    def controlTimer(self, num):
        self.cap = cv2.VideoCapture(num)  # выбор камеры
        if not self.timer.isActive():
            self.timer.start(20)
        else:
            self.timer.stop()

    def controlTimer2(self,num):
        self.cap2 = cv2.VideoCapture(num)  # выбор камеры
        if not self.timer2.isActive():
            self.timer2.start(20)
        else:
            self.timer2.stop()

    def viewCam2(self, a):
        # read image in BGR format
        ret, image = self.cap2.read()
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        # a = self.ui.label_4
        a.setPixmap(QPixmap.fromImage(qImg))

    def record(self):
        self.out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 24, (3, 4))
        while(True):
            self.out.write(self.frame)
        self.cap.release()
        self.out.release()

    def stoprecord(self):
        print
        "pressed End"
        self.capturing = False
        # cv2.destroyAllWindows(

    def win1(self):
        self.ui.label_4.setFixedWidth(900)
        self.ui.label_4.setFixedHeight(700)
        self.ui.label_5.hide()
        self.ui.label_6.hide()
        self.ui.label_7.hide()
        self.ui.label_8.hide()
        self.ui.label_9.hide()
        self.ui.label_11.hide()
        self.ui.label_14.hide()
        self.ui.label_15.hide()

    def win9(self):
        self.ui.label_4.setFixedSize(351,251)
        self.ui.label_4.show()
        self.ui.label_5.show()
        self.ui.label_6.show()
        self.ui.label_7.show()
        self.ui.label_8.show()
        self.ui.label_9.show()
        self.ui.label_11.show()
        self.ui.label_14.show()
        self.ui.label_15.show()

    def openplayer(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO history(id,login,time,action) VALUES('" + str("1") + "','" + str(
            self.ui.login_text.text()) + "','" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")) + "','Open player')")
        self.connection.commit()
        z.show()
        # self.ui.label_2.setText(str(z.ui.horizontalSlider.value()))

    def login(self):
        # query = "SELECT * FROM users WHERE login='admin' and password='admin'"
        # result = connection.execute(query)
        # countrows = result.fetchall().__len__()

        logform = self.ui.login_text.text()
        passform = hashlib.md5(str(self.ui.password_text.text()).encode('utf-8')).hexdigest()

        if(self.connection.execute("SELECT * FROM users WHERE login='" + logform + "' and password='" + passform + "'").fetchall().__len__() == 1):
            self.ui.login_text.hide()
            self.ui.group_auth.hide()
            self.ui.btn_name2.setText(logform)
            print((self.connection.execute("SELECT access FROM users WHERE login='" + logform+"'").fetchone()[0]))
            if(self.connection.execute("SELECT access FROM users WHERE login='" + logform+"'").fetchone()[0] == "root"):
                print("Вы зашли под админом")
                self.ui.btn_users.show()
            else:
                print("Вы не админ")
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO history(id,login,time,action) VALUES('" + str("1")  + "','" + str(logform) + "','" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")) +  "','Authorization')")
            self.connection.commit()



    def openuserswindows(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO history(id,login,time,action) VALUES('" + str("1") + "','" + str(
            self.ui.login_text.text()) + "','" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")) + "','Open user window')")
        self.connection.commit()
        u.show()




    def openbox1(self):
        if(self.ui.groupBox.isVisible()):
            self.ui.groupBox.hide()
        else:
            self.ui.groupBox.show()

    def openbox2(self):
        if (self.ui.groupBox_2.isVisible()):
            self.ui.groupBox_2.hide()
        else:
            self.ui.groupBox_2.show()


    def openbox3(self):
        if (self.ui.groupBox_3.isVisible()):
            self.ui.groupBox_3.hide()
        else:
            self.ui.groupBox_3.show()

    def exitprogram(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO history(id,login,time,action) VALUES('" + str("1") + "','" + str(self.ui.login_text.text()) + "','" + str(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M")) + "','Exit')")
        self.connection.commit()
        QApplication.closeAllWindows()

    def opensettings(self):
        if (self.connection.execute("SELECT access FROM users WHERE login='" + str(self.ui.login_text.text()) + "'").fetchone()[0] != "root"):
            QMessageBox.about(self, "Ошибка", "<font color='white'>У вас нет необходимых прав доступа</font>")
        else:
            s.show()



class Player(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.show()
        self.ui.btn_play.clicked.connect(self.playvideo) #включить видео
        self.ui.btn_stop.clicked.connect(self.stopvideo) #остановить видео
        self.ui.btn_pause.clicked.connect(self.pausevideo) #пауза
        self.ui.btn_back.clicked.connect(self.hidewindow) #скрыть окно плеера
        self.ui.verticalSlider.valueChanged.connect(self.setvolume) #громкость
        # self.ui.horizontalSlider.valueChanged.connect(self.settimevideo) #перемотка - починить функцию
        self.ui.listWidget.addItems(listdir("records")) #генерация списка файлов в папке records
        self.ui.listWidget.itemClicked.connect(self.playthis) #выбор видео


        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.setvideoonslider)#автодвижение ползунка
        self.video = QVideoWidget(self.ui.label)
        self.video.resize(621, 451)
        self.video.move(0, 0)
        self.player.setVideoOutput(self.video)
        self.video.show()

        self.ui.label.customContextMenuRequested.connect(self.testfun) #ПРАВАЯ КНОПКА МЫШИ

    def testfun(self):
        print("Тест успешен")

    def playvideo(self):
        self.player.play()
        self.ui.horizontalSlider.setMaximum(self.player.duration())
        self.ui.horizontalSlider.setPageStep(self.player.duration() / 10)

    def stopvideo(self):
        self.player.stop()

    def pausevideo(self):
        self.player.pause()

    def hidewindow(self):
        self.hide()

    def setvolume(self):
        self.player.setVolume(self.ui.verticalSlider.value())

    def settimevideo(self):
        self.player.setPosition(self.ui.horizontalSlider.value())

    def playthis(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("records/" + str(self.ui.listWidget.currentItem().text()))))

    def setvideoonslider(self):
        self.ui.horizontalSlider.setValue(self.player.position())
        self.ui.lbl_time.setText(str(int(self.player.position() / 1000)) + "/" + str(int(self.player.duration() / 1000)))

    def test(self):
        print("Тест пройден")

class UsersWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # self.show()
        self.loaddata()
        self.ui.btn_adduser.clicked.connect(self.adduser)
        # self.ui.tableWidget.itemSelectionChanged.connect(self.deluser)
        self.ui.btn_deleteuser.clicked.connect(self.deluser)
        self.ui.btn_canceldel.clicked.connect(self.canceldel)
        self.ui.btn_back.clicked.connect(self.closewin)

    def loaddata(self):
        connection = sqlite3.connect('mydb.db')
        query = "SELECT * FROM users"
        result = connection.execute(query)
        self.ui.tableWidget.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        # connection.close()

    def adduser(self):
        name=self.ui.line_name.text()
        password=self.ui.line_pass.text()
        passwordr=self.ui.line_passr.text()
        role = self.ui.comboBox.currentText()
        if(password==passwordr and role!="Права доступа"):
            self.ui.lbl_alert.setText("")
            connection = sqlite3.connect('mydb.db')
            cursor = connection.cursor()
            cursor.execute("INSERT INTO users(id,login,password,access,visible) VALUES('"+str(random.randint(1000,99999))+"','"+str(name)+"','"+str(password)+"','"+str(role)+"','yes')")
            connection.commit()
            self.loaddata()
        if(passwordr!=password):
            self.ui.lbl_alert.setText("Пароли не совпадают")
        if(role=="Права доступа"):
            self.ui.lbl_alert.setText("Выберите права пользователя")
        if(password=="" or passwordr=="" or name==""):
            self.ui.lbl_alert.setText("Одно из полей пустое")

    def deluser(self):
        element = self.ui.tableWidget.currentItem().text()
        connection = sqlite3.connect('mydb.db')
        cursor = connection.cursor()
        # cursor.execute("DELETE FROM users where id='"+ str(element) + "'")
        cursor.execute("UPDATE users SET visible='no' where id='"+ str(element) + "'")
        connection.commit()
        self.loaddata()

    def canceldel(self):
        element = self.ui.tableWidget.currentItem().text()
        connection = sqlite3.connect('mydb.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET visible='yes' where id='" + str(element) + "'")
        connection.commit()
        self.loaddata()

    def closewin(self):
        u.close()



class Settings(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FormSet()
        self.ui.setupUi(self)
        self.diskusage()

    def diskusage(self):
        total, used, free = shutil.disk_usage("\\")
        self.ui.label_5.setText(str(int(used/1024/1024/1024))+"/"+str(int(total/1024/1024/1024))+"ГБ")
        self.ui.progressBar.setValue(int((used/total)*100))


app = QApplication(sys.argv)
w = AppWindow()
w.show() #its mainwindows
z = Player()
u = UsersWindow()
s = Settings()
sys.exit(app.exec_())

