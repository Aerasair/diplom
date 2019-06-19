# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'users_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 615)
        Form.setStyleSheet("background:#1C1E1B;")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 591, 391))
        self.tableWidget.setStyleSheet("QWidget {\n"
"    background-color: #333333;\n"
"    color: #fffff8;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #646464;\n"
"    padding: 4px;\n"
"    border: 1px solid #fffff8;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid #fffff8;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("background:none;\n"
"color:#fff;")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(20, 460, 311, 141))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"  background: gray;\n"
"  color: #000;\n"
"  padding: 10px;\n"
" }\n"
" QTabBar::tab:selected {\n"
"  background: lightgray;\n"
" }\n"
"QTabWidget::pane { \n"
"   border: 1px solid #fff;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.line_name = QtWidgets.QLineEdit(self.tab)
        self.line_name.setGeometry(QtCore.QRect(1, 1, 311, 20))
        self.line_name.setStyleSheet("QLineEdit{\n"
"color:#fff;\n"
"background:#1C1E1B;\n"
"border:1px solid #fff;\n"
"}\n"
"QLineEdit:hover{\n"
"border:red;\n"
"}")
        self.line_name.setObjectName("line_name")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(0, 60, 311, 22))
        self.comboBox.setStyleSheet("color:#fff;\n"
"border:red;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_adduser = QtWidgets.QPushButton(self.tab)
        self.btn_adduser.setGeometry(QtCore.QRect(0, 80, 141, 31))
        self.btn_adduser.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_adduser.setObjectName("btn_adduser")
        self.line_pass = QtWidgets.QLineEdit(self.tab)
        self.line_pass.setGeometry(QtCore.QRect(1, 21, 311, 20))
        self.line_pass.setStyleSheet("QLineEdit{\n"
"color:#fff;\n"
"background:#1C1E1B;\n"
"border:1px solid #fff;\n"
"}\n"
"QLineEdit:hover{\n"
"border:red;\n"
"}")
        self.line_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_pass.setObjectName("line_pass")
        self.line_passr = QtWidgets.QLineEdit(self.tab)
        self.line_passr.setGeometry(QtCore.QRect(1, 41, 311, 20))
        self.line_passr.setStyleSheet("QLineEdit{\n"
"color:#fff;\n"
"background:#1C1E1B;\n"
"border:1px solid #fff;\n"
"}\n"
"QLineEdit:hover{\n"
"border:red;\n"
"}")
        self.line_passr.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_passr.setObjectName("line_passr")
        self.lbl_alert = QtWidgets.QLabel(self.tab)
        self.lbl_alert.setGeometry(QtCore.QRect(150, 80, 161, 21))
        self.lbl_alert.setStyleSheet("color:red;")
        self.lbl_alert.setText("")
        self.lbl_alert.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_alert.setObjectName("lbl_alert")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_edituser = QtWidgets.QPushButton(self.tab_2)
        self.btn_edituser.setGeometry(QtCore.QRect(0, 0, 311, 23))
        self.btn_edituser.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_edituser.setObjectName("btn_edituser")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.btn_deleteuser = QtWidgets.QPushButton(self.tab_3)
        self.btn_deleteuser.setGeometry(QtCore.QRect(0, 0, 151, 23))
        self.btn_deleteuser.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_deleteuser.setObjectName("btn_deleteuser")
        self.btn_canceldel = QtWidgets.QPushButton(self.tab_3)
        self.btn_canceldel.setGeometry(QtCore.QRect(160, 0, 151, 23))
        self.btn_canceldel.setStyleSheet("QPushButton{\n"
"color:#fff;\n"
"border:1px solid #fff;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border:1px solid #f00;\n"
"}")
        self.btn_canceldel.setObjectName("btn_canceldel")
        self.tabWidget.addTab(self.tab_3, "")
        self.btn_back = QtWidgets.QPushButton(Form)
        self.btn_back.setGeometry(QtCore.QRect(450, 550, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton{\n"
"border:1px solid #fff;\n"
"color:#fff;\n"
"}\n"
"QPushButton:hover{\n"
"background:#ccc;\n"
"color:#000;\n"
"}")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "Новая строка"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "Новая строка"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Имя пользователя"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Пароль"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Статус"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Видимый"))
        self.label.setText(_translate("Form", "Панель администрирования - Пользовтели"))
        self.line_name.setPlaceholderText(_translate("Form", "Имя пользователя"))
        self.comboBox.setItemText(0, _translate("Form", "Права доступа"))
        self.comboBox.setItemText(1, _translate("Form", "Модератор"))
        self.comboBox.setItemText(2, _translate("Form", "Пользователь"))
        self.btn_adduser.setText(_translate("Form", "Добавить"))
        self.line_pass.setPlaceholderText(_translate("Form", "Пароль"))
        self.line_passr.setPlaceholderText(_translate("Form", "Повтор пароля"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Добавить"))
        self.btn_edituser.setText(_translate("Form", "Редактировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Редактировать"))
        self.btn_deleteuser.setText(_translate("Form", "Удалить"))
        self.btn_canceldel.setText(_translate("Form", "Вернуть"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Удалить"))
        self.btn_back.setText(_translate("Form", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

