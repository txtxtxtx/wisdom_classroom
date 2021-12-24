import sys
from operation import Operation
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication

from UI.main import Ui_MainWindow
from windows.chart.line_chart import ChartView
from windows.window_class import Class_Window
from windows.window_emtion_analysis import Emotion_Analysis_Window
from windows.window_sign_in import Sign_in_Window


class Main_Window(QMainWindow):

    def __init__(self):
        super(Main_Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.class_management.clicked.connect(self.classManagement)

        self.ui.sign_in_management.clicked.connect(self.sign_inManagement)

        self.ui.emotion_analysis.clicked.connect(self.emotion_analysisManagement)

    """
    功能函数
    """
    # 跳转到班级管理
    def classManagement(self):
        class_w.show()
        self.close()

    # 跳转到签到
    def sign_inManagement(self):
        sign_in_w.show()
        self.close()

    # 跳转情绪分析
    def emotion_analysisManagement(self):
        emotion_analysis_w.show()
        self.close()

    def showMessage(self, msg_, time_):
        self.statusbar.showMessage(msg_, time_)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    opt = Operation()
    # 主窗口
    main_w = Main_Window()
    main_w.show()
    # 签到
    sign_in_w = Sign_in_Window(main_w, opt)

    # 情绪分析
    emotion_analysis_w = Emotion_Analysis_Window(main_w, opt)
    # 班级管理
    class_w = Class_Window(main_w, opt)

    sys.exit(app.exec_())

