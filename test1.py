# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 20, 596, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(122, 12, 401, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(500, 10, 62, 16))
        self.label_10.setObjectName("label_10")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(93, 32, 471, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(43, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_9.addWidget(self.checkBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_10.addWidget(self.checkBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_11.addWidget(self.checkBox_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_12.addWidget(self.checkBox_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_8)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_13.addWidget(self.checkBox_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(90, 330, 471, 80))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_15.addWidget(self.textEdit_2)
        self.layoutWidget.raise_()
        self.label_10.raise_()
        self.layoutWidget.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(110, 31, 391, 271))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_16.addWidget(self.label_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_16.addWidget(self.lineEdit_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_17.addWidget(self.label_13)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_17.addWidget(self.lineEdit_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_21.addWidget(self.label_14)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.horizontalLayout_21.addWidget(self.lineEdit_10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(80, 130, 431, 141))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_18.addWidget(self.label_16)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_18.addWidget(self.lineEdit_12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_20.addWidget(self.label_17)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_20.addWidget(self.lineEdit_13)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.layoutWidget5 = QtWidgets.QWidget(self.tab_5)
        self.layoutWidget5.setGeometry(QtCore.QRect(80, 120, 421, 101))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_19.addWidget(self.label_15)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_19.addWidget(self.lineEdit_11)
        self.tabWidget.addTab(self.tab_5, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 450, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(650, 20, 381, 411))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget6)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_14.setGeometry(QtCore.QRect(470, 0, 113, 21))
        self.lineEdit_14.setObjectName("lineEdit_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu1 = QtWidgets.QMenu(self.menu)
        self.menu1.setObjectName("menu1")
        self.menu1_1 = QtWidgets.QMenu(self.menu1)
        self.menu1_1.setObjectName("menu1_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu123 = QtWidgets.QMenu(self.menubar)
        self.menu123.setObjectName("menu123")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setObjectName("action3")
        self.action4 = QtWidgets.QAction(MainWindow)
        self.action4.setObjectName("action4")
        self.action5 = QtWidgets.QAction(MainWindow)
        self.action5.setObjectName("action5")
        self.action6 = QtWidgets.QAction(MainWindow)
        self.action6.setObjectName("action6")
        self.action1_2 = QtWidgets.QAction(MainWindow)
        self.action1_2.setObjectName("action1_2")
        self.action1_1_1 = QtWidgets.QAction(MainWindow)
        self.action1_1_1.setObjectName("action1_1_1")
        self.actionShuangxiang = QtWidgets.QAction(MainWindow)
        self.actionShuangxiang.setObjectName("actionShuangxiang")
        self.action3_2 = QtWidgets.QAction(MainWindow)
        self.action3_2.setObjectName("action3_2")
        self.action4_2 = QtWidgets.QAction(MainWindow)
        self.action4_2.setObjectName("action4_2")
        self.action5_2 = QtWidgets.QAction(MainWindow)
        self.action5_2.setObjectName("action5_2")
        self.menu1_1.addAction(self.action1_1_1)
        self.menu1.addAction(self.menu1_1.menuAction())
        self.menu1.addAction(self.action1_2)
        self.menu.addAction(self.menu1.menuAction())
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action3)
        self.menu.addSeparator()
        self.menu.addAction(self.action4)
        self.menu.addAction(self.action5)
        self.menu.addAction(self.action6)
        self.menu_2.addAction(self.actionShuangxiang)
        self.menu_2.addAction(self.action3_2)
        self.menu_2.addAction(self.action4_2)
        self.menu_2.addAction(self.action5_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu123.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.pushButton.clicked.connect(MainWindow.submit)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "问题"))
        self.label_2.setText(_translate("MainWindow", "答案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "问答题"))
        self.label_10.setText(_translate("MainWindow", "正确答案"))
        self.label_3.setText(_translate("MainWindow", " 问题 "))
        self.label_4.setText(_translate("MainWindow", "选项1"))
        self.checkBox.setText(_translate("MainWindow", "A"))
        self.label_5.setText(_translate("MainWindow", "选项2"))
        self.checkBox_2.setText(_translate("MainWindow", "B"))
        self.label_6.setText(_translate("MainWindow", "选项3"))
        self.checkBox_3.setText(_translate("MainWindow", "C"))
        self.label_7.setText(_translate("MainWindow", "选项4"))
        self.checkBox_4.setText(_translate("MainWindow", "D"))
        self.label_8.setText(_translate("MainWindow", "选项5"))
        self.checkBox_5.setText(_translate("MainWindow", "E"))
        self.label_11.setText(_translate("MainWindow", "答案描述"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "选择题"))
        self.label_12.setText(_translate("MainWindow", "标题"))
        self.label_13.setText(_translate("MainWindow", "图片"))
        self.label_14.setText(_translate("MainWindow", "链接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "banner"))
        self.label_16.setText(_translate("MainWindow", "标题"))
        self.label_17.setText(_translate("MainWindow", "链接"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "文字banner"))
        self.label_15.setText(_translate("MainWindow", "图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "图片"))
        self.pushButton.setText(_translate("MainWindow", "提交"))
        self.label_9.setText(_translate("MainWindow", "上一次提交的内容"))
        self.menu.setTitle(_translate("MainWindow", "问答题"))
        self.menu1.setTitle(_translate("MainWindow", "1"))
        self.menu1_1.setTitle(_translate("MainWindow", "1.1"))
        self.menu_2.setTitle(_translate("MainWindow", "选择题"))
        self.menu123.setTitle(_translate("MainWindow", "123"))
        self.action2.setText(_translate("MainWindow", "2"))
        self.action3.setText(_translate("MainWindow", "3"))
        self.action4.setText(_translate("MainWindow", "4"))
        self.action5.setText(_translate("MainWindow", "5"))
        self.action6.setText(_translate("MainWindow", "6"))
        self.action1_2.setText(_translate("MainWindow", "1.2"))
        self.action1_1_1.setText(_translate("MainWindow", "1.1.1"))
        self.actionShuangxiang.setText(_translate("MainWindow", "2"))
        self.action3_2.setText(_translate("MainWindow", "3"))
        self.action4_2.setText(_translate("MainWindow", "4"))
        self.action5_2.setText(_translate("MainWindow", "5"))

