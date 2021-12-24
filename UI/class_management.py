# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'class_UqyBDt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Class(object):
    def setupUi(self, Class):
        if not Class.objectName():
            Class.setObjectName(u"Class")
        Class.resize(1080, 720)
        Class.setMaximumSize(QSize(1080, 720))
        self.centralwidget = QWidget(Class)
        self.centralwidget.setObjectName(u"centralwidget")
        self.new_class = QPushButton(self.centralwidget)
        self.new_class.setObjectName(u"new_class")
        self.new_class.setGeometry(QRect(30, 70, 93, 28))
        self.del_class = QPushButton(self.centralwidget)
        self.del_class.setObjectName(u"del_class")
        self.del_class.setGeometry(QRect(30, 110, 93, 28))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(770, 60, 221, 591))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 219, 589))
        self.img_area = QWidget(self.scrollAreaWidgetContents)
        self.img_area.setObjectName(u"img_area")
        self.img_area.setGeometry(QRect(0, 0, 221, 591))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.cur_class = QComboBox(self.centralwidget)
        self.cur_class.setObjectName(u"cur_class")
        self.cur_class.setGeometry(QRect(140, 30, 571, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 71, 21))
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(160, 70, 551, 571))
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 181, 51))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 100, 72, 15))
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 100, 72, 15))
        self.scrollArea_2 = QScrollArea(self.widget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(40, 190, 131, 371))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 129, 369))
        self.names = QListView(self.scrollAreaWidgetContents_2)
        self.names.setObjectName(u"names")
        self.names.setGeometry(QRect(0, 0, 131, 371))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 160, 72, 15))
        Class.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Class)
        self.statusbar.setObjectName(u"statusbar")
        Class.setStatusBar(self.statusbar)

        self.retranslateUi(Class)

        QMetaObject.connectSlotsByName(Class)
    # setupUi

    def retranslateUi(self, Class):
        Class.setWindowTitle(QCoreApplication.translate("Class", u"MainWindow", None))
        self.new_class.setText(QCoreApplication.translate("Class", u"\u521b\u5efa\u73ed\u7ea7", None))
        self.del_class.setText(QCoreApplication.translate("Class", u"\u5220\u9664\u73ed\u7ea7", None))
        self.label.setText(QCoreApplication.translate("Class", u"\u5f53\u524d\u73ed\u7ea7:", None))
        self.label_2.setText(QCoreApplication.translate("Class", u"\u73ed\u7ea7\u57fa\u672c\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("Class", u"\u4eba\u6570:", None))
        self.label_4.setText(QCoreApplication.translate("Class", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Class", u"\u6210\u5458\u5217\u8868", None))
    # retranslateUi

