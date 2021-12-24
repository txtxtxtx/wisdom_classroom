# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowTJziLy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1080, 720)
        self.createclass = QAction(MainWindow)
        self.createclass.setObjectName(u"createclass")
        self.createclass.setCheckable(False)
        self.createclass.setVisible(True)
        self.createclass.setMenuRole(QAction.TextHeuristicRole)
        self.chooseclass = QAction(MainWindow)
        self.chooseclass.setObjectName(u"chooseclass")
        self.numberofpeple = QAction(MainWindow)
        self.numberofpeple.setObjectName(u"numberofpeple")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 161, 41))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.sign_in_management = QPushButton(self.widget_4)
        self.sign_in_management.setObjectName(u"sign_in_management")
        self.sign_in_management.setGeometry(QRect(140, 80, 251, 91))
        font1 = QFont()
        font1.setPointSize(20)
        self.sign_in_management.setFont(font1)

        self.gridLayout.addWidget(self.widget_4, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.tools = QToolBox(self.widget_6)
        self.tools.setObjectName(u"tools")
        self.tools.setGeometry(QRect(150, 10, 241, 241))
        font2 = QFont()
        font2.setPointSize(7)
        self.tools.setFont(font2)
        self.tools.setFrameShadow(QFrame.Sunken)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 241, 187))
        font3 = QFont()
        font3.setPointSize(8)
        self.page_3.setFont(font3)
        self.tools.addItem(self.page_3, u"\u5c55\u5f00")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 241, 187))
        self.tools.addItem(self.page_4, u"\u5173\u95ed")

        self.gridLayout.addWidget(self.widget_6, 1, 1, 1, 1)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.emotion_analysis = QPushButton(self.widget_5)
        self.emotion_analysis.setObjectName(u"emotion_analysis")
        self.emotion_analysis.setGeometry(QRect(120, 70, 251, 91))
        self.emotion_analysis.setFont(font1)

        self.gridLayout.addWidget(self.widget_5, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.class_management = QPushButton(self.widget_3)
        self.class_management.setObjectName(u"class_management")
        self.class_management.setGeometry(QRect(120, 80, 251, 91))
        self.class_management.setFont(font1)

        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tools.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.createclass.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u73ed\u7ea7", None))
#if QT_CONFIG(statustip)
        self.createclass.setStatusTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u63cf\u8ff0\u6587\u4ef6\uff0c\u521b\u5efa\u73ed\u7ea7", None))
#endif // QT_CONFIG(statustip)
        self.chooseclass.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u73ed\u7ea7", None))
        self.numberofpeple.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u6570\u68c0\u6d4b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u667a\u6167\u8bfe\u5802", None))
        self.sign_in_management.setText(QCoreApplication.translate("MainWindow", u"\u7b7e\u5230\u7ba1\u7406", None))
        self.tools.setItemText(self.tools.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u5c55\u5f00", None))
        self.tools.setItemText(self.tools.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.emotion_analysis.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u7eea\u5206\u6790", None))
        self.class_management.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7\u7ba1\u7406", None))
    # retranslateUi

