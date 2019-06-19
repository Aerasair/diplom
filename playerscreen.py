# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playerscreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 601)
        MainWindow.setStyleSheet("background:#1C1E1B;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setGeometry(QtCore.QRect(10, 550, 41, 41))
        self.btn_play.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#111;\n"
"}")
        self.btn_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/player/player2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon)
        self.btn_play.setIconSize(QtCore.QSize(40, 40))
        self.btn_play.setObjectName("btn_play")
        self.btn_forwardplayer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_forwardplayer.setGeometry(QtCore.QRect(130, 550, 41, 41))
        self.btn_forwardplayer.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#111;\n"
"}")
        self.btn_forwardplayer.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/player/player3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_forwardplayer.setIcon(icon1)
        self.btn_forwardplayer.setIconSize(QtCore.QSize(40, 40))
        self.btn_forwardplayer.setObjectName("btn_forwardplayer")
        self.btn_backplayer = QtWidgets.QPushButton(self.centralwidget)
        self.btn_backplayer.setGeometry(QtCore.QRect(70, 550, 41, 41))
        self.btn_backplayer.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#111;\n"
"}")
        self.btn_backplayer.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/player/player5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_backplayer.setIcon(icon2)
        self.btn_backplayer.setIconSize(QtCore.QSize(40, 40))
        self.btn_backplayer.setObjectName("btn_backplayer")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 520, 621, 22))
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(50000)
        self.horizontalSlider.setPageStep(5000)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(310, 540, 22, 51))
        self.verticalSlider.setAutoFillBackground(False)
        self.verticalSlider.setStyleSheet("QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: #aaa;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: #fff;\n"
"    position: absolute; \n"
"}")
        self.verticalSlider.setInputMethodHints(QtCore.Qt.ImhNone)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(99)
        self.verticalSlider.setProperty("value", 99)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider.setTickInterval(0)
        self.verticalSlider.setObjectName("verticalSlider")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(640, 530, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton{\n"
"border:1px solid #fff;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background:#ccc;\n"
"}")
        self.btn_back.setObjectName("btn_back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 621, 491))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label.setStyleSheet("border:1px solid #fff;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 570, 47, 21))
        self.label_2.setStyleSheet("color:#fff;")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(250, 550, 41, 41))
        self.btn_stop.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#111;\n"
"}")
        self.btn_stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/player/player1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon3)
        self.btn_stop.setIconSize(QtCore.QSize(40, 40))
        self.btn_stop.setObjectName("btn_stop")
        self.btn_pause = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pause.setGeometry(QtCore.QRect(190, 550, 41, 41))
        self.btn_pause.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#111;\n"
"}")
        self.btn_pause.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/player/playe4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pause.setIcon(icon4)
        self.btn_pause.setIconSize(QtCore.QSize(40, 40))
        self.btn_pause.setObjectName("btn_pause")
        self.lbl_time = QtWidgets.QLabel(self.centralwidget)
        self.lbl_time.setGeometry(QtCore.QRect(530, 470, 71, 20))
        self.lbl_time.setStyleSheet("color:#fff;")
        self.lbl_time.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.lbl_time.setObjectName("lbl_time")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(640, 150, 271, 351))
        self.listWidget.setStyleSheet("color:#fff;")
        self.listWidget.setObjectName("listWidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(640, 10, 271, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("QCalendarWidget QToolButton {\n"
"      height: 10px;\n"
"      width: 30px;\n"
"      color: white;\n"
"      font-size: 12px;\n"
"      icon-size: 56px, 56px;\n"
"      background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"      width: 100px;\n"
"      left: 20px;\n"
"      color: green;\n"
"      font-size: 18px;\n"
"      background-color: rgb(100, 100, 100);\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"      width: 100px; \n"
"      font-size:12px; \n"
"      color: white; \n"
"      background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"      selection-background-color: rgb(136, 136, 136);\n"
"      selection-color: rgb(255, 255, 255);\n"
"  }\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"  QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; }\n"
"  QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; }\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"      font-size:10px;  \n"
"      color: rgb(180, 180, 180);  \n"
"      background-color: black;  \n"
"      selection-background-color: rgb(64, 64, 64); \n"
"      selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(640, 150, 271, 22))
        self.timeEdit.setStyleSheet("color:#fff;")
        self.timeEdit.setObjectName("timeEdit")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.verticalSlider.sliderMoved['int'].connect(self.label_2.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проигрыватель"))
        self.btn_back.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "100"))
        self.lbl_time.setText(_translate("MainWindow", "time/time"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

