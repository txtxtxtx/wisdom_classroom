import sys

import cv2
from PySide2.QtCore import QStringListModel, QTimer, SIGNAL
from PySide2.QtGui import QPixmap, QImage

from UI.sign_in import Ui_Sign_in_Window
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication


class Sign_in_Window(QMainWindow):
    def __init__(self, main_w, opt):
        super(Sign_in_Window, self).__init__()
        self.main_w = main_w
        self.opt = opt

        # 视频帧获取计时器 41 1秒24帧
        self.timer_camera = QTimer(self)
        self.timer_camera.timeout.connect(self.get_one_camera_img)
        self.cur_img = ""
        # 摄像头是否打开
        self.opened_camera = False
        self.camera = None

        self.ui = Ui_Sign_in_Window()
        self.ui.setupUi(self)

        # 当前页基本参数
        self.cur_class = opt.cur_class
        # 成员名称列表
        self.names = self.opt.face_info.names
        # 脸照片
        self.faces = self.opt.face_info.face_img
        # 坐标信息
        self.result_info = self.opt.face_info.xywh_info
        # 人数
        self.numbers = self.opt.face_info.number_of_people

        # 信息绑定

        # 选择班级
        self.ui.comboBox_2.addItems(self.opt.class_list)
        self.ui.comboBox_2.currentIndexChanged.connect(self.choose_class)

        # 成员列表模型
        self.slm = QStringListModel()
        self.slm.setStringList(self.names)
        self.ui.class_number_list.setModel(self.slm)

        # 缺勤成员列表模型
        self.absent_names = QStringListModel()
        self.ui.absent_list.setModel(self.absent_names)
        # 双击删除
        # self.connect(self.ui.absent_list, SIGNAL('doubleClicked()'), self.del_name)
        self.ui.absent_list.doubleClicked.connect(self.del_name)
        # 照片选取
        self.ui.choose_image.clicked.connect(self.choose_img)
        self.ui.open_camera_2.clicked.connect(self.open_camera)

    # 初始化
    def process(self, cur_class):
        self.opt.init_process(cur_class)
        # 当前班级
        self.cur_class = cur_class
        # 成员名称列表
        self.names = self.opt.face_info.names
        # 脸照片
        self.faces = self.opt.face_info.face_img
        # 坐标信息
        self.result_info = self.opt.face_info.xywh_info
        # 人数
        self.numbers = self.opt.face_info.number_of_people
        self.slm.setStringList(self.names)

    def choose_class(self):
        index = self.ui.comboBox_2.currentIndex()
        self.process(index)

    # 选取照片
    def choose_img(self):
        if self.opened_camera:
            self.open_camera()
            img = QImage(self.cur_img.data, self.cur_img.shape[1], self.cur_img.shape[0], QImage.Format_RGB888)
            self.ui.img_show.setPixmap(QPixmap.fromImage(img))
            self.sign_in()
        else:
            cur_img, format_ = QFileDialog.getOpenFileName(self, '打开图片文件', '', "*.jpg;;*.png;;*jpeg;;All Files(*)")
            show_img = QPixmap(cur_img).scaled(self.ui.img_show.width(), self.ui.img_show.height())
            self.ui.img_show.setPixmap(show_img)

            if cur_img != "":
                self.cur_img = cv2.imread(cur_img)
                self.cur_img = cv2.resize(self.cur_img, (640, 480))
                self.cur_img = cv2.cvtColor(self.cur_img, cv2.COLOR_BGR2RGB)
                self.sign_in()

    # 打开关闭摄像头
    def open_camera(self):
        if self.opened_camera:
            self.timer_camera.stop()
            self.ui.open_camera_2.setText("打开摄像头")
            self.opened_camera = False
            # 销毁摄像头
            self.camera.release()
        else:
            self.camera = cv2.VideoCapture(self.opt.config_yaml["baseconfig"]["camera"])
            self.timer_camera.start(30)
            self.ui.open_camera_2.setText("关闭摄像头")
            self.opened_camera = True

    # 图片连续显示
    def get_one_camera_img(self):
        flag, img = self.camera.read()
        if flag:
            self.cur_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = QImage(self.cur_img.data, self.cur_img.shape[1], self.cur_img.shape[0], QImage.Format_RGB888)
            self.ui.img_show.setPixmap(QPixmap.fromImage(img))
            # QPixmap(self.cur_img).scaled(self.ui.img_show.width(), self.ui.img_show.height())
            # self.ui.img_show.setPixmap(self.cur_img)

    # 签到
    def sign_in(self):
        # 签到
        sign_msg = self.opt.sign_in(self.cur_img)
        img = QImage(sign_msg["show_img"].data, sign_msg["show_img"].shape[1],
                     sign_msg["show_img"].shape[0], QImage.Format_RGB888)
        self.ui.img_show.setPixmap(QPixmap.fromImage(img))
        self.absent_names.setStringList(sign_msg["absent_names"])

    def del_name(self):
        index = self.ui.absent_list.currentIndex()
        if index:
            self.absent_names.removeRow(index.row())

    # 关闭当前窗口的事件
    def closeEvent(self, event):
        # 判读摄像头是否关闭
        if self.opened_camera:
            self.timer_camera.stop()
            self.ui.open_camera_2.setText("打开摄像头")
            self.opened_camera = False
            # 销毁摄像头
            self.camera.release()
        # 打开主窗口
        self.main_w.show()
        # 关闭当前窗口
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Sign_in_Window()
    ex.show()
    sys.exit(app.exec_())