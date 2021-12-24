import sys

import cv2
import yaml
from PySide2.QtCore import QStringListModel, QTimer, SIGNAL
from PySide2.QtGui import QPixmap, QImage

from UI.class_management import Ui_Class
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication, QLabel, QWidget

from utils.util_visualize import draw_text


class Class_Window(QMainWindow):
    def __init__(self, main_w, opt):
        super(Class_Window, self).__init__()

        self.main_w = main_w
        self.opt = opt

        self.ui = Ui_Class()
        self.ui.setupUi(self)

        self.cur_class = 0
        # 成员名称列表
        self.names = self.opt.face_info.names
        # 脸照片
        self.faces = self.opt.face_info.face_img
        # 坐标信息
        self.result_info = self.opt.face_info.xywh_info
        # 人数
        self.numbers = self.opt.face_info.number_of_people

        # 成员列表模型
        self.slm = QStringListModel()
        self.slm.setStringList(self.names)
        self.ui.names.setModel(self.slm)

        self.ui.new_class.clicked.connect(self.newClass)

        self.ui.del_class.clicked.connect(self.delClass)

        self.ui.cur_class.addItems(self.opt.class_list)
        self.ui.cur_class.currentIndexChanged.connect(self.choose_class)

        self.ui.label_4.setText(str(self.opt.face_info.number_of_people))

        self.suoluetu()

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

        self.ui.label_4.setText(str(self.numbers))

        self.suoluetu()

    def choose_class(self):
        index = self.ui.cur_class.currentIndex()
        self.process(index)

    # 创建班级
    def newClass(self):
        frame, format_ = QFileDialog.getOpenFileName(self, '打开文件', '', "Text Files (*.txt)")

        if frame:
            # 创建一个班级
            self.opt.class_list.append(str(frame))
            self.showMessage("班级创建成功", 3000)
            self.ui.cur_class.addItem(str(frame))
        else:
            self.showMessage("创建失败", 3000)

    # 删除班级
    def delClass(self):
        class_idx = self.cur_class
        del self.opt.class_list[class_idx]
        self.ui.cur_class.removeItem(class_idx)
        self.showMessage("删除成功", 3000)

    def showMessage(self, msg_, time_):
        self.ui.statusbar.showMessage(msg_, time_)

    def suoluetu(self):
        positions = [(i, j) for i in range(4) for j in range(30)]

        self.ui.filewidget = QWidget()
        self.ui.filewidget.setMinimumSize(150, 1800)
        idx = 0
        for position, img_ in zip(positions, self.opt.face_info.face_img):
            lab = QLabel(self.ui.filewidget)
            lab.setFixedSize(100, 150)
            img_ = cv2.cvtColor(img_, cv2.COLOR_BGR2RGB)
            img_ = cv2.resize(img_, (100, 150))
            img_ = draw_text(img_, self.opt.face_info.names[idx], font_size=14)
            idx += 1
            QtImg = QImage(img_.data,
                                      img_.shape[1],
                                      img_.shape[0],
                                      img_.shape[1] * 3,
                                      QImage.Format_RGB888)

            lab.setPixmap(QPixmap.fromImage(QtImg))
            lab.move(100 * position[0] + 50, 150 * position[1] + 70)
        self.ui.scrollArea.setWidget(self.ui.filewidget)

    # 关闭当前窗口的事件
    def closeEvent(self, event):
        classes = ""
        len_list = len(self.opt.class_list) - 1
        for index, class_ in enumerate(self.opt.class_list):
            if len_list > index:
                classes = classes + class_ + " "
            else:
                classes = classes + class_
        self.opt.config_yaml["face_name_txt_path"] = classes
        # 写入到yaml文件
        with open(self.opt.config_path, "w", encoding="utf-8") as f:
            yaml.dump(self.opt.config_yaml, f)
        # 打开主窗口
        self.main_w.show()
        # 关闭当前窗口
        event.accept()
