# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign_inhKxhVF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Sign_in_Window(object):
    def setupUi(self, Sign_in_Window):
        if not Sign_in_Window.objectName():
            Sign_in_Window.setObjectName(u"Sign_in_Window")
        Sign_in_Window.resize(1080, 720)
        Sign_in_Window.setMaximumSize(QSize(1080, 720))
        self.centralwidget = QWidget(Sign_in_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.comboBox_2 = QComboBox(self.widget_6)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.horizontalSpacer = QSpacerItem(656, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.choose_image = QPushButton(self.widget_6)
        self.choose_image.setObjectName(u"choose_image")

        self.horizontalLayout_2.addWidget(self.choose_image)

        self.open_camera_2 = QPushButton(self.widget_6)
        self.open_camera_2.setObjectName(u"open_camera_2")

        self.horizontalLayout_2.addWidget(self.open_camera_2)


        self.verticalLayout_3.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.scrollArea_3 = QScrollArea(self.widget_8)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 182, 245))
        self.class_number_list = QListView(self.scrollAreaWidgetContents_3)
        self.class_number_list.setObjectName(u"class_number_list")
        self.class_number_list.setEnabled(True)
        self.class_number_list.setGeometry(QRect(0, 0, 181, 251))
        font1 = QFont()
        font1.setPointSize(10)
        self.class_number_list.setFont(font1)
        self.class_number_list.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.class_number_list.setProperty("isWrapping", True)
        self.class_number_list.setItemAlignment(Qt.AlignLeading)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_3)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.scrollArea_4 = QScrollArea(self.widget_8)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 182, 245))
        self.absent_list = QListView(self.scrollAreaWidgetContents_4)
        self.absent_list.setObjectName(u"absent_list")
        self.absent_list.setGeometry(QRect(0, 1, 181, 251))
        self.absent_list.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_4.addWidget(self.scrollArea_4)


        self.horizontalLayout_3.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_7)
        self.widget_9.setObjectName(u"widget_9")
        self.img_show = QLabel(self.widget_9)
        self.img_show.setObjectName(u"img_show")
        self.img_show.setGeometry(QRect(70, 60, 640, 480))
        self.img_show.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.widget_9)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 9)
        Sign_in_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Sign_in_Window)
        self.statusbar.setObjectName(u"statusbar")
        Sign_in_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Sign_in_Window)

        QMetaObject.connectSlotsByName(Sign_in_Window)
    # setupUi

    def retranslateUi(self, Sign_in_Window):
        Sign_in_Window.setWindowTitle(QCoreApplication.translate("Sign_in_Window", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("Sign_in_Window", u"\u5f53\u524d\u73ed\u7ea7: ", None))
        self.choose_image.setText(QCoreApplication.translate("Sign_in_Window", u"\u9009\u53d6\u7167\u7247", None))
        self.open_camera_2.setText(QCoreApplication.translate("Sign_in_Window", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.label_4.setText(QCoreApplication.translate("Sign_in_Window", u"\u73ed\u7ea7\u6210\u5458\u540d\u5355", None))
        self.label_5.setText(QCoreApplication.translate("Sign_in_Window", u"\u7f3a\u52e4\u540d\u5355", None))
        self.img_show.setText(QCoreApplication.translate("Sign_in_Window", u"\u56fe\u7247\u663e\u793a\u533a", None))
    # retranslateUi

