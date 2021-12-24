import sys
import random
from PyQt5.QtChart import QDateTimeAxis, QValueAxis, QSplineSeries, QChart, QChartView, QLineSeries
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QDateTime, Qt, QTimer


class ChartView(QChartView):
    def __init__(self, main_w):
        super(ChartView, self).__init__()
        self.main_w = main_w
        self.cur_emotions = main_w.cur_emotions

        self.resize(1080, 720)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart_init()
        self.timer_init()

    def timer_init(self):
        # 使用QTimer，1秒触发一次，更新数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine)
        self.timer.start(2000)

    def chart_init(self):
        self.chart = QChart()
        '''
                angry_0 = 0
                hate_1 = 0
                fear_2 = 0
                happy_3 = 0
                suprise_4 = 0
                calm_5 = 0
        '''
        self.series0 = QSplineSeries()  # 曲线QSplineSeries 折线QlineSeries
        self.series1 = QSplineSeries()
        self.series2 = QSplineSeries()
        self.series3 = QSplineSeries()
        self.series4 = QSplineSeries()
        self.series5 = QSplineSeries()

        self.series_list = []
        self.series_list.append(self.series0)
        self.series_list.append(self.series1)
        self.series_list.append(self.series2)
        self.series_list.append(self.series3)
        self.series_list.append(self.series4)
        self.series_list.append(self.series5)
        # 设置曲线名称
        self.series0.setName("生气")
        self.series1.setName("厌恶")
        self.series2.setName("恐惧")
        self.series3.setName("高兴")
        self.series4.setName("惊喜")
        self.series5.setName("平静")
        # 把曲线添加到QChart的实例中
        self.chart.addSeries(self.series0)
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)
        self.chart.addSeries(self.series3)
        self.chart.addSeries(self.series4)
        self.chart.addSeries(self.series5)
        # 声明并初始化X轴，Y轴
        self.dtaxisX = QDateTimeAxis()
        self.vlaxisY = QValueAxis()
        # 设置坐标轴显示范围
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-30 * 1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY.setMin(0)
        self.vlaxisY.setMax(20)
        # 设置X轴时间样式
        self.dtaxisX.setFormat("mm:ss")
        # 设置坐标轴上的格点
        self.dtaxisX.setTickCount(11)
        self.vlaxisY.setTickCount(11)
        # 设置坐标轴名称
        self.dtaxisX.setTitleText("时间")
        self.vlaxisY.setTitleText("情绪人数")
        # 设置网格不显示
        self.vlaxisY.setGridLineVisible(False)
        # 把坐标轴添加到chart中
        self.chart.addAxis(self.dtaxisX, Qt.AlignBottom)
        self.chart.addAxis(self.vlaxisY, Qt.AlignLeft)
        # 把曲线关联到坐标轴
        self.series0.attachAxis(self.dtaxisX)
        self.series0.attachAxis(self.vlaxisY)

        self.series1.attachAxis(self.dtaxisX)
        self.series1.attachAxis(self.vlaxisY)

        self.series2.attachAxis(self.dtaxisX)
        self.series2.attachAxis(self.vlaxisY)

        self.series3.attachAxis(self.dtaxisX)
        self.series3.attachAxis(self.vlaxisY)

        self.series4.attachAxis(self.dtaxisX)
        self.series4.attachAxis(self.vlaxisY)

        self.series5.attachAxis(self.dtaxisX)
        self.series5.attachAxis(self.vlaxisY)

        self.setChart(self.chart)

    def drawLine(self):
        if self.main_w.close_thread:
            self.close()
        # 获取当前时间
        bjtime = QDateTime.currentDateTime()
        # 更新X轴坐标
        self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-30 * 1))
        self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
        # 当曲线上的点超出X轴的范围时，移除最早的点
        for series, count_emotion in zip(self.series_list, self.cur_emotions):
            if series.count() > 149:
                series.removePoints(0, series.count() - 149)
            yint = count_emotion
            # 添加数据到曲线末端
            series.append(bjtime.toMSecsSinceEpoch(), yint)

    def closeEvent(self, event):
        # self.main_w.show()
        event.accept()


def ChartView_(main_w):
    app = QApplication(sys.argv)
    view = ChartView(main_w)
    view.show()
    sys.exit(app.exec_())
