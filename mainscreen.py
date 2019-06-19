# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1051, 915)
        mainWindow.setStyleSheet("background:#1C1E1B;")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.bg1 = QtWidgets.QLabel(self.centralwidget)
        self.bg1.setEnabled(False)
        self.bg1.setGeometry(QtCore.QRect(-10, 830, 1061, 101))
        self.bg1.setStyleSheet("background:#0B0B0B;")
        self.bg1.setText("")
        self.bg1.setObjectName("bg1")
        self.bgtop = QtWidgets.QLabel(self.centralwidget)
        self.bgtop.setGeometry(QtCore.QRect(0, 0, 5, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bgtop.sizePolicy().hasHeightForWidth())
        self.bgtop.setSizePolicy(sizePolicy)
        self.bgtop.setStyleSheet("background:#0B0B0B;\n"
"width:100%;")
        self.bgtop.setText("")
        self.bgtop.setObjectName("bgtop")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(40, 10, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("background:#0B0B0B;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/icons/profile.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 840, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setStyleSheet("QPushButton {background:#0B0B0B;border: none;}\n"
"\n"
"QPushButton:hover{\n"
"background:#009CAD;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/video-player.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setShortcut("")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.btn_add_cam = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_cam.setGeometry(QtCore.QRect(30, 840, 51, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_cam.sizePolicy().hasHeightForWidth())
        self.btn_add_cam.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_add_cam.setFont(font)
        self.btn_add_cam.setStyleSheet("QPushButton {background:#0B0B0B;border: none;}\n"
"\n"
"QPushButton:hover{\n"
"background:#009CAD;\n"
"}")
        self.btn_add_cam.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/security.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_cam.setIcon(icon1)
        self.btn_add_cam.setIconSize(QtCore.QSize(45, 45))
        self.btn_add_cam.setShortcut("")
        self.btn_add_cam.setAutoRepeat(False)
        self.btn_add_cam.setAutoExclusive(False)
        self.btn_add_cam.setObjectName("btn_add_cam")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 0, 1051, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background:#0B0B0B;\n"
"color:#fff;\n"
"border:0px;")
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 890, 51, 16))
        self.label.setStyleSheet("QLabel{\n"
"background:#0B0B0B;\n"
"color:#fff;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 890, 51, 16))
        self.label_2.setStyleSheet("QLabel{\n"
"background:#0B0B0B;\n"
"color:#fff;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 80, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 80, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 330, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setLineWidth(1)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 80, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setLineWidth(1)
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 330, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setLineWidth(1)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(700, 330, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setLineWidth(1)
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(0, 580, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setLineWidth(1)
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(350, 580, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setLineWidth(1)
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(700, 580, 351, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet("background:#44465D;\n"
"color:#fff;\n"
"padding: 3px;\n"
"border:1px solid #fff;")
        self.label_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setLineWidth(1)
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(120, 60, 201, 81))
        self.groupBox.setStyleSheet("border-top:4px solid #fff;\n"
"border-bottom:4px solid #fff;\n"
"border-left:1px solid #fff;\n"
"border-right:1px solid #fff;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.btn_users_2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_users_2.setGeometry(QtCore.QRect(0, 10, 201, 31))
        self.btn_users_2.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_users_2.setObjectName("btn_users_2")
        self.btn_users = QtWidgets.QPushButton(self.groupBox)
        self.btn_users.setGeometry(QtCore.QRect(0, 40, 201, 31))
        self.btn_users.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_users.setObjectName("btn_users")
        self.texttimedate = QtWidgets.QLineEdit(self.centralwidget)
        self.texttimedate.setGeometry(QtCore.QRect(840, 850, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.texttimedate.setFont(font)
        self.texttimedate.setStyleSheet("color:#fff;\n"
"border:none;\n"
"background:#0B0B0B;")
        self.texttimedate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.texttimedate.setObjectName("texttimedate")
        self.btn_name2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_name2.setGeometry(QtCore.QRect(130, 10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.btn_name2.setFont(font)
        self.btn_name2.setStyleSheet("QPushButton{\n"
"background:#0B0B0B;\n"
"color:#fff;\n"
"border:0px;\n"
"text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"}")
        self.btn_name2.setObjectName("btn_name2")
        self.btn_open_gridbox = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_gridbox.setGeometry(QtCore.QRect(700, 840, 51, 51))
        self.btn_open_gridbox.setStyleSheet("QPushButton {\n"
"background:#0B0B0B;\n"
"border: none;\n"
"}")
        self.btn_open_gridbox.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/table-grid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_gridbox.setIcon(icon2)
        self.btn_open_gridbox.setIconSize(QtCore.QSize(45, 45))
        self.btn_open_gridbox.setObjectName("btn_open_gridbox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(700, 690, 201, 141))
        self.groupBox_2.setStyleSheet("border-top:4px solid #fff;\n"
"border-bottom:4px solid #fff;\n"
"border-left:1px solid #fff;\n"
"border-right:1px solid #fff;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_grid1 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_grid1.setGeometry(QtCore.QRect(0, 10, 201, 31))
        self.btn_grid1.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_grid1.setObjectName("btn_grid1")
        self.btn_grid9 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_grid9.setGeometry(QtCore.QRect(0, 40, 201, 31))
        self.btn_grid9.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_grid9.setObjectName("btn_grid9")
        self.btn_grid18 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_grid18.setGeometry(QtCore.QRect(0, 70, 201, 31))
        self.btn_grid18.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_grid18.setObjectName("btn_grid18")
        self.btn_grid36 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_grid36.setGeometry(QtCore.QRect(0, 100, 201, 31))
        self.btn_grid36.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_grid36.setObjectName("btn_grid36")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 640, 201, 191))
        self.groupBox_3.setStyleSheet("border-top:4px solid #fff;\n"
"border-bottom:4px solid #fff;\n"
"border-left:1px solid #fff;\n"
"border-right:1px solid #fff;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 181, 21))
        self.label_3.setStyleSheet("color:#fff;\n"
"border:0px;\n"
"padding-left:10px;\n"
"border-left:1px solid #fff;")
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 70, 121, 22))
        self.comboBox_2.setStyleSheet("color:#fff; border:1px solid #fff;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(0, 100, 201, 20))
        self.lineEdit.setStyleSheet("color:#fff; border:1px solid #fff;\n"
"padding-left:10px;")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 160, 201, 23))
        self.pushButton_5.setStyleSheet("color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(0, 40, 201, 22))
        self.comboBox.setStyleSheet("color:#fff; border:1px solid #fff;")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 130, 201, 23))
        self.pushButton_6.setStyleSheet("color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(0, 10, 141, 21))
        self.label_12.setStyleSheet("color:#fff;\n"
"border:0px;\n"
"padding-left:10px;\n"
"border-left:1px solid #fff;")
        self.label_12.setObjectName("label_12")
        self.group_auth = QtWidgets.QGroupBox(self.centralwidget)
        self.group_auth.setGeometry(QtCore.QRect(-10, -10, 1061, 931))
        self.group_auth.setMouseTracking(False)
        self.group_auth.setFocusPolicy(QtCore.Qt.TabFocus)
        self.group_auth.setTitle("")
        self.group_auth.setObjectName("group_auth")
        self.password_text = QtWidgets.QLineEdit(self.group_auth)
        self.password_text.setGeometry(QtCore.QRect(330, 460, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.password_text.setFont(font)
        self.password_text.setFocusPolicy(QtCore.Qt.TabFocus)
        self.password_text.setStyleSheet("QLineEdit {\n"
"border:2px solid #fff;\n"
"color:#fff;\n"
"text-align:center;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border:2px solid #ff0000;\n"
"}\n"
"")
        self.password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_text.setAlignment(QtCore.Qt.AlignCenter)
        self.password_text.setObjectName("password_text")
        self.login_text = QtWidgets.QLineEdit(self.group_auth)
        self.login_text.setGeometry(QtCore.QRect(330, 399, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.login_text.setFont(font)
        self.login_text.setFocusPolicy(QtCore.Qt.TabFocus)
        self.login_text.setStyleSheet("QLineEdit {\n"
"border:2px solid #fff;\n"
"color:#fff;\n"
"text-align:center;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border:2px solid #ff0000;\n"
"}\n"
"")
        self.login_text.setAlignment(QtCore.Qt.AlignCenter)
        self.login_text.setObjectName("login_text")
        self.btn_guest = QtWidgets.QPushButton(self.group_auth)
        self.btn_guest.setGeometry(QtCore.QRect(330, 370, 271, 23))
        self.btn_guest.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px dashed #fff;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_guest.setObjectName("btn_guest")
        self.login_text.raise_()
        self.btn_guest.raise_()
        self.password_text.raise_()
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(980, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:0px;\n"
"background:none;\n"
"}\n"
"QPushButton:hover{\n"
"background:#333;\n"
"}\n"
"")
        self.btn_exit.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon3)
        self.btn_exit.setIconSize(QtCore.QSize(45, 45))
        self.btn_exit.setObjectName("btn_exit")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(700, 890, 51, 16))
        self.label_13.setStyleSheet("QLabel{\n"
"background:#0B0B0B;\n"
"color:#fff;\n"
"}")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(900, 10, 61, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background:none;\n"
"color:#fff;\n"
"border:none;\n"
"}")
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(900, 60, 61, 16))
        self.label_16.setStyleSheet("QLabel{\n"
"background:none;\n"
"color:#fff;\n"
"border:none;\n"
"}")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.pushButton_10.raise_()
        self.btn_name2.raise_()
        self.label_4.raise_()
        self.bg1.raise_()
        self.bgtop.raise_()
        self.pushButton.raise_()
        self.btn_add_cam.raise_()
        self.label_10.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.groupBox.raise_()
        self.texttimedate.raise_()
        self.btn_open_gridbox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.label_13.raise_()
        self.pushButton_2.raise_()
        self.label_16.raise_()
        self.group_auth.raise_()
        self.btn_exit.raise_()
        # mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.login_text, self.password_text)
        mainWindow.setTabOrder(self.password_text, self.pushButton)
        mainWindow.setTabOrder(self.pushButton, self.btn_add_cam)
        mainWindow.setTabOrder(self.btn_add_cam, self.btn_users)
        mainWindow.setTabOrder(self.btn_users, self.pushButton_10)
        mainWindow.setTabOrder(self.pushButton_10, self.btn_guest)
        mainWindow.setTabOrder(self.btn_guest, self.btn_users_2)
        mainWindow.setTabOrder(self.btn_users_2, self.texttimedate)
        mainWindow.setTabOrder(self.texttimedate, self.btn_name2)
        mainWindow.setTabOrder(self.btn_name2, self.btn_open_gridbox)
        mainWindow.setTabOrder(self.btn_open_gridbox, self.btn_grid1)
        mainWindow.setTabOrder(self.btn_grid1, self.btn_grid9)
        mainWindow.setTabOrder(self.btn_grid9, self.btn_grid18)
        mainWindow.setTabOrder(self.btn_grid18, self.btn_grid36)
        mainWindow.setTabOrder(self.btn_grid36, self.comboBox_2)
        mainWindow.setTabOrder(self.comboBox_2, self.lineEdit)
        mainWindow.setTabOrder(self.lineEdit, self.pushButton_5)
        mainWindow.setTabOrder(self.pushButton_5, self.comboBox)
        mainWindow.setTabOrder(self.comboBox, self.pushButton_6)
        mainWindow.setTabOrder(self.pushButton_6, self.group_auth)
        mainWindow.setTabOrder(self.group_auth, self.btn_exit)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Система видеонаблюдения"))
        self.label.setText(_translate("mainWindow", "Добавить"))
        self.label_2.setText(_translate("mainWindow", "Плеер"))
        self.label_4.setText(_translate("mainWindow", "Главный коридор"))
        self.label_5.setText(_translate("mainWindow", "Название камеры"))
        self.label_6.setText(_translate("mainWindow", "Название камеры"))
        self.label_7.setText(_translate("mainWindow", "Название камеры"))
        self.label_8.setText(_translate("mainWindow", "Название камеры"))
        self.label_9.setText(_translate("mainWindow", "Название камеры"))
        self.label_11.setText(_translate("mainWindow", "Название камеры"))
        self.label_14.setText(_translate("mainWindow", "Название камеры"))
        self.label_15.setText(_translate("mainWindow", "Название камеры"))
        self.btn_users_2.setText(_translate("mainWindow", "Сменить пользователя"))
        self.btn_users.setText(_translate("mainWindow", "Администрирование"))
        self.texttimedate.setText(_translate("mainWindow", "12:34 20.05.2019"))
        self.btn_name2.setText(_translate("mainWindow", "name"))
        self.btn_grid1.setText(_translate("mainWindow", "1"))
        self.btn_grid9.setText(_translate("mainWindow", "9"))
        self.btn_grid18.setText(_translate("mainWindow", "18"))
        self.btn_grid36.setText(_translate("mainWindow", "36"))
        self.label_3.setText(_translate("mainWindow", "Качество"))
        self.lineEdit.setPlaceholderText(_translate("mainWindow", "Название камеры"))
        self.pushButton_5.setText(_translate("mainWindow", "отмена"))
        self.pushButton_6.setText(_translate("mainWindow", "Добавить в систему"))
        self.label_12.setText(_translate("mainWindow", "Список камер"))
        self.password_text.setPlaceholderText(_translate("mainWindow", "Пароль"))
        self.login_text.setPlaceholderText(_translate("mainWindow", "Логин"))
        self.btn_guest.setText(_translate("mainWindow", "Гостевой режим"))
        self.label_13.setText(_translate("mainWindow", "Сетка"))
        self.label_16.setText(_translate("mainWindow", "Настройки"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

