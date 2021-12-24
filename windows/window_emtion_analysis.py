import sys
import threading

import cv2
from PySide2.QtCore import QStringListModel, QTimer, SIGNAL
from PySide2.QtGui import QPixmap, QImage

from UI.emotion_analysis import Ui_Emotion_Analysis
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication

from utils.util_visualize import visualize
from windows.chart.line_chart import ChartView, ChartView_


class Emotion_Analysis_Window(QMainWindow):
    def __init__(self, main_w, opt):
        super(Emotion_Analysis_Window, self).__init__()

        self.main_w = main_w
        self.opt = opt
        self.cur_emotions = []
        self.ui = Ui_Emotion_Analysis()
        self.ui.setupUi(self)

        cur_class = opt.config_yaml["baseconfig"]["cur_class"]
        self.ui.cur_class.setText(self.opt.class_list[cur_class])

        self.cur_img = None

        # 视频帧获取计时器 41 1秒24帧
        self.timer_camera = QTimer(self)
        self.timer_camera.timeout.connect(self.get_one_camera_img)

        self.baseS = 10
        self.countS = 0

        self.camera_opened = False
        self.camera = None

        self.ui.open_camera.clicked.connect(self.open_camera)
        self.ui.qx_view.clicked.connect(self.show_view)

        self.cur_emotions = [0, 0, 0, 0, 0, 0]
        self.close_thread = False

    def open_camera(self):
        if self.camera_opened:
            self.timer_camera.stop()
            self.ui.open_camera.setText("打开摄像头")
            self.camera_opened = False
            # 销毁摄像头
            self.camera.release()
            self.cur_emotions = [0, 0, 0, 0, 0, 0]
        else:
            self.camera = cv2.VideoCapture(self.opt.config_yaml["baseconfig"]["camera"])
            self.timer_camera.start(50)
            self.ui.open_camera.setText("关闭摄像头")
            self.camera_opened = True

    # 图片连续显示
    def get_one_camera_img(self):
        flag, img = self.camera.read()
        if flag:
            self.cur_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.opt.det.face_detect(self.cur_img)

            yydxxd = self.opt.det.xywh_to_yydxxd()

            show_img = self.cur_img

            emo_list = []
            if len(yydxxd) > 0:
                for yxd in yydxxd:
                    one_emo = self.opt.emo.face_emotion(self.cur_img, yxd, True)  # 需要剪裁
                    emo_list.append(one_emo)
                show_img = visualize(self.cur_img, self.opt.det.xywh_list, emo_list, True)

            img = QImage(show_img.data, show_img.shape[1], show_img.shape[0], QImage.Format_RGB888)
            self.ui.img_show.setPixmap(QPixmap.fromImage(img))
            self.countS += 1

            if self.countS % self.baseS == 0:
                self.countS = 0
                # 检测人数更新
                self.ui.label_15.setText(str(len(yydxxd)))
                # 更新情绪
                angry_0 = 0
                hate_1 = 0
                fear_2 = 0
                happy_3 = 0
                suprise_4 = 0
                calm_5 = 0
                if len(emo_list) > 0:
                    for emo_ in emo_list:
                        if emo_ == "生气":
                            angry_0 += 1
                        elif emo_ == "厌恶":
                            hate_1 += 1
                        elif emo_ == "恐惧":
                            fear_2 += 1
                        elif emo_ == "开心":
                            happy_3 += 1
                        elif emo_ == "惊喜":
                            suprise_4 += 1
                        elif emo_ == "平静":
                            calm_5 += 1
                    self.cur_emotions[0] = angry_0
                    self.cur_emotions[1] = hate_1
                    self.cur_emotions[2] = fear_2
                    self.cur_emotions[3] = happy_3
                    self.cur_emotions[4] = suprise_4
                    self.cur_emotions[5] = calm_5

                self.ui.label_9.setText(str(angry_0))
                self.ui.label_10.setText(str(hate_1))
                self.ui.label_11.setText(str(fear_2))
                self.ui.label_12.setText(str(happy_3))
                self.ui.label_13.setText(str(suprise_4))
                self.ui.label_14.setText(str(calm_5))

    def show_view(self):
        self.close_thread = False
        self.this_thread = threading.Thread(target=ChartView_, args=[self])
        self.this_thread.start()

    # 关闭当前窗口的事件
    def closeEvent(self, event):
        self.close_thread = True
        # 判读摄像头是否关闭
        if self.camera_opened:
            self.timer_camera.stop()
            self.ui.open_camera.setText("打开摄像头")
            self.camera_opened = False
            # 销毁摄像头
            self.camera.release()
        # 打开主窗口
        self.main_w.show()
        # 关闭当前窗口
        event.accept()
