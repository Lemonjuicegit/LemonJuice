# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '导出工具2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self,MainWindow):

        # self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName(u"centralwidget")
        # self.gridLayoutWidget = QWidget(self.centralwidget)
        # self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        # self.gridLayoutWidget.setGeometry(QRect(10, 10, 341, 411))
        self.gridLayout = QGridLayout(MainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)


        #按钮生成
        self.pushButton = QPushButton(MainWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(MainWindow)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(MainWindow)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(MainWindow)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(MainWindow)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(MainWindow)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(MainWindow)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(MainWindow)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 3, 1, 1)

        #   标签和文本框
        self.horizontalLayout_1 = QHBoxLayout()# 水平布局
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.horizontalLayout_1.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(MainWindow)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.horizontalLayout_1.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.horizontalLayout_1, 2, 0, 1, 4)

        self.horizontalLayout_2 = QHBoxLayout() #   水平布局
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(MainWindow)
        self.label_2.setObjectName(u"label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(MainWindow)
        self.lineEdit.setObjectName(u"lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 4)

        self.horizontalLayout_3= QHBoxLayout()# 水平布局
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(MainWindow)
        self.label_4.setObjectName(u"label_4")

        self.lineEdit_3 = QLineEdit(MainWindow)
        self.lineEdit_3.setObjectName(u"lineEdit")
        self.horizontalLayout_3.addWidget(self.label_4 )
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 4)

        #   消息提醒标签
        self.label_3 = QLabel(MainWindow)
        self.label_3.setObjectName(u"label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 4)

        #   编辑框
        self.plainTextEdit = QPlainTextEdit(MainWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 6, 0, 1, 4)




        self.retranslateUi(MainWindow)


        return self.gridLayout
    # setupUi


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6e1d\u5317\u9879\u76ee\u8d44\u6599\u5bfc\u51fa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6302\u63a5\u8868\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"exf\u5bfc\u51fa", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u754c\u5740\u8868\u5bfc\u51fa", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5230\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6c47\u603b\u8868\u5bfc\u51fa", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\uff1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u7b97\u8bf4\u660e\u4e66", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8fdc/\u8fd1\u666f", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939\u751f\u6210", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u7ed8\u6280\u672f\u8bf4\u660e", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8bb0\u5f55\u8868", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u952e\u5168\u5bfc", None))
    # retranslateUi
