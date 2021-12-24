# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emotionhPnFwE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Emotion_Analysis(object):
    def setupUi(self, Emotion_Analysis):
        if not Emotion_Analysis.objectName():
            Emotion_Analysis.setObjectName(u"Emotion_Analysis")
        Emotion_Analysis.resize(1080, 720)
        Emotion_Analysis.setMaximumSize(QSize(1080, 720))
        self.centralwidget = QWidget(Emotion_Analysis)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1130, 695))
        self.tabWidget.setMinimumSize(QSize(1080, 695))
        self.emotion_analysis = QWidget()
        self.emotion_analysis.setObjectName(u"emotion_analysis")
        self.emotion_analysis.setMinimumSize(QSize(1080, 695))
        self.verticalLayout = QVBoxLayout(self.emotion_analysis)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.emotion_analysis)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(1050, 0))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.qx_view = QPushButton(self.widget)
        self.qx_view.setObjectName(u"qx_view")

        self.horizontalLayout.addWidget(self.qx_view)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.cur_class = QLabel(self.widget)
        self.cur_class.setObjectName(u"cur_class")
        font1 = QFont()
        font1.setPointSize(10)
        self.cur_class.setFont(font1)
        self.cur_class.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.cur_class)

        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 8)

        self.verticalLayout_2.addWidget(self.widget)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(1080, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 6, -1)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.gridLayout = QGridLayout(self.widget_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.open_camera = QPushButton(self.widget_4)
        self.open_camera.setObjectName(u"open_camera")

        self.gridLayout.addWidget(self.open_camera, 0, 0, 1, 1)

        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 0, 1, 1, 1)

        self.number_of_people = QLabel(self.widget_4)
        self.number_of_people.setObjectName(u"number_of_people")
        self.number_of_people.setFont(font)

        self.gridLayout.addWidget(self.number_of_people, 1, 0, 1, 1)

        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout.addWidget(self.label_15, 1, 1, 1, 1)

        self.angry_0 = QLabel(self.widget_4)
        self.angry_0.setObjectName(u"angry_0")
        self.angry_0.setFont(font)

        self.gridLayout.addWidget(self.angry_0, 2, 0, 1, 1)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1)

        self.hate_1 = QLabel(self.widget_4)
        self.hate_1.setObjectName(u"hate_1")
        self.hate_1.setFont(font)

        self.gridLayout.addWidget(self.hate_1, 3, 0, 1, 1)

        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.fear_2 = QLabel(self.widget_4)
        self.fear_2.setObjectName(u"fear_2")
        self.fear_2.setFont(font)

        self.gridLayout.addWidget(self.fear_2, 4, 0, 1, 1)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 4, 1, 1, 1)

        self.happy_3 = QLabel(self.widget_4)
        self.happy_3.setObjectName(u"happy_3")
        self.happy_3.setFont(font)

        self.gridLayout.addWidget(self.happy_3, 5, 0, 1, 1)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 5, 1, 1, 1)

        self.suprise_4 = QLabel(self.widget_4)
        self.suprise_4.setObjectName(u"suprise_4")
        self.suprise_4.setFont(font)

        self.gridLayout.addWidget(self.suprise_4, 6, 0, 1, 1)

        self.label_13 = QLabel(self.widget_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout.addWidget(self.label_13, 6, 1, 1, 1)

        self.calm_5 = QLabel(self.widget_4)
        self.calm_5.setObjectName(u"calm_5")
        self.calm_5.setFont(font)

        self.gridLayout.addWidget(self.calm_5, 7, 0, 1, 1)

        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout.addWidget(self.label_14, 7, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.img_show = QLabel(self.widget_5)
        self.img_show.setObjectName(u"img_show")
        self.img_show.setGeometry(QRect(50, 40, 640, 480))
        self.img_show.setMinimumSize(QSize(640, 480))
        self.img_show.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.widget_5)

        self.horizontalLayout_2.setStretch(1, 7)

        self.verticalLayout_2.addWidget(self.widget_3)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 9)

        self.verticalLayout.addWidget(self.widget_2)

        self.verticalLayout.setStretch(0, 9)
        self.tabWidget.addTab(self.emotion_analysis, "")
        Emotion_Analysis.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Emotion_Analysis)
        self.statusbar.setObjectName(u"statusbar")
        Emotion_Analysis.setStatusBar(self.statusbar)

        self.retranslateUi(Emotion_Analysis)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Emotion_Analysis)
    # setupUi

    def retranslateUi(self, Emotion_Analysis):
        Emotion_Analysis.setWindowTitle(QCoreApplication.translate("Emotion_Analysis", u"MainWindow", None))
        self.qx_view.setText(QCoreApplication.translate("Emotion_Analysis", u"\u66f2\u7ebf\u56fe", None))
        self.label_2.setText(QCoreApplication.translate("Emotion_Analysis", u"\u5f53\u524d\u73ed\u7ea7", None))
        self.cur_class.setText("")
        self.open_camera.setText(QCoreApplication.translate("Emotion_Analysis", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.label_16.setText("")
        self.number_of_people.setText(QCoreApplication.translate("Emotion_Analysis", u"\u68c0\u6d4b\u4eba\u6570", None))
        self.label_15.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.angry_0.setText(QCoreApplication.translate("Emotion_Analysis", u"\u751f\u6c14", None))
        self.label_9.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.hate_1.setText(QCoreApplication.translate("Emotion_Analysis", u"\u538c\u6076", None))
        self.label_10.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.fear_2.setText(QCoreApplication.translate("Emotion_Analysis", u"\u6050\u60e7", None))
        self.label_11.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.happy_3.setText(QCoreApplication.translate("Emotion_Analysis", u"\u5f00\u5fc3", None))
        self.label_12.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.suprise_4.setText(QCoreApplication.translate("Emotion_Analysis", u"\u60ca\u559c", None))
        self.label_13.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.calm_5.setText(QCoreApplication.translate("Emotion_Analysis", u"\u5e73\u9759", None))
        self.label_14.setText(QCoreApplication.translate("Emotion_Analysis", u"0", None))
        self.img_show.setText(QCoreApplication.translate("Emotion_Analysis", u"\u56fe\u7247\u663e\u793a\u533a\u57df", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.emotion_analysis), QCoreApplication.translate("Emotion_Analysis", u"\u60c5\u7eea\u5206\u6790", None))
    # retranslateUi

