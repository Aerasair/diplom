# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingswin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FormSet(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 480)
        Form.setStyleSheet("background:#1C1E1B;\n"
"color:#fff;")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 651, 491))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"  background: gray;\n"
"  color: #000;\n"
"  padding: 10px;\n"
"\n"
" }\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
" }\n"
"QTabWidget::pane { \n"
"   border-left: 1px solid #fff;\n"
"background:#1C1E1B;\n"
"    color:#fff\n"
"}\n"
"QTabWidget{\n"
"    background:#1C1E1B;\n"
"    color:#fff;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(340, 60, 75, 31))
        self.pushButton.setStyleSheet("background:#1C1E1B;\n"
"color:#fff;\n"
"border:1px solid #fff;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background:#1C1E1B;\n"
"color:#fff;\n"
"}\n"
"QLineEdit:hover{\n"
"background:none;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background:none;")
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 120, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background:none;")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(20, 170, 311, 23))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("background:red;")
        self.progressBar.setProperty("value", 41)
        self.progressBar.setObjectName("progressBar")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(340, 160, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:none;")
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:none;")
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background:none;")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 30, 231, 41))
        self.pushButton_2.setStyleSheet("background:#1C1E1B;\n"
"color:#fff;\n"
"border:1px solid #fff;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 30, 231, 41))
        self.pushButton_3.setStyleSheet("background:#1C1E1B;\n"
"color:#fff;\n"
"border:1px solid #fff;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Выбрать"))
        self.lineEdit.setText(_translate("Form", "S:\\videorecords"))
        self.label_4.setText(_translate("Form", "Местоположение видеофайлов"))
        self.label.setText(_translate("Form", "Объем жесткого диска"))
        self.label_5.setText(_translate("Form", "512/1250 GB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Хранилище"))
        self.label_2.setText(_translate("Form", "Всего видео: 15"))
        self.label_3.setText(_translate("Form", "Всего пользователей: 9"))
        self.label_6.setText(_translate("Form", "Общая длительность видео: 2 часов"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Статистика"))
        self.pushButton_2.setText(_translate("Form", "Сделать резервную копию"))
        self.pushButton_3.setText(_translate("Form", "Восстановить из резервной копии"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Backup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormSet()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

