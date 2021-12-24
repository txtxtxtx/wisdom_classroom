import os.path

import cv2
import numpy as np
import yaml
from utils.util_url import ROOT
# 模型
from models.load_face_info import Faces_Info
from models.face_detection import Detect
from models.face_recognition import Recognition
from models.face_emotion import Emotion

from utils.util_visualize import draw_text, visualize


class Operation:

    def __init__(self):
        # 班级
        self.cur_class = 0
        self.config_yaml = ''
        # 加载配置文件 (一个 dict)
        self.config_path = os.path.join(ROOT, "config.yaml")
        with open(self.config_path, "r", encoding="utf-8") as config:
            cont = config.read()

        self.config_yaml = yaml.safe_load(cont)

        self.cur_class = self.config_yaml["baseconfig"]["cur_class"]
        '''
        需要回写的配置
        '''

        # 班级描述信息路径
        self.class_list = list(self.config_yaml['face_name_txt_path'].split(" "))

        # 班级脸信息及图片loader
        '''
            班级成员姓名列表 names
            班级成员图片列表 face_img
            图片人脸所在    xywh_info
            人数           number_of_people
            加载是否完成    loaded_info
        '''
        self.face_info = None

        '''
            检测结果信息         result_msg
            [ [x,y,w,h], ...]  xywh_list
            人脸列表            one_face_list
            检测到的人脸数       num_of_face
        '''

        # 人脸检测器
        self.det = None

        '''
        特征号列表   feature1_list
        '''
        # 人脸识别器
        self.recog = None

        # 情绪识别器
        self.emo = None

        # 初始化
        self.init_process(self.cur_class)

    def init_process(self, cur_class=0):
        """
        初始化过程
        :param cur_class: 当前班级
        :return:
        """
        # 配置文件修改
        self.config_yaml["baseconfig"]["cur_class"] = cur_class

        # 班级相关信息初始化
        self.face_info = Faces_Info(self.class_list[cur_class])
        self.face_info.load_xywh_info(self.config_yaml["baseconfig"]["base_face_changed"])

        # 人脸检测器
        self.det = Detect()

        # 人脸识别器
        self.recog = Recognition()
        self.recog.infers(self.face_info.face_img, np.array(self.face_info.xywh_info))
        # 情绪识别器
        self.emo = Emotion()

    def re_load_yaml(self):

        with open(self.config_path, "r", encoding="utf-8") as config:
            cont = config.read()

        self.config_yaml = yaml.safe_load(cont)

        self.cur_class = self.config_yaml["baseconfig"]["cur_class"]
        '''
        需要回写的配置
        '''

        # 班级描述信息路径
        self.class_list = list(self.config_yaml['face_name_txt_path'].split(" "))

    # 系统功能函数==============================================================

    # 签到==
    def sign_in(self, sign_in_img):
        # 1.检测图片人脸
        self.det.face_detect(sign_in_img)
        # 2.人脸比对
        res_map = self.recog.match_feature(sign_in_img, self.det.result_msg)
        # 班级缺勤名单
        list_absent = self.face_info.names.copy()
        # 名字对应
        show_names = []
        # 对应的人数
        number_of_check = 0
        for idx, idx2 in enumerate(res_map):
            if idx2[0] != -1.:
                number_of_check += 1
                info_ = self.face_info.names[int(idx2[0])]  # +":"+str(idx2[1])
                # 排除已到成员
                list_absent.remove(self.face_info.names[int(idx2[0])])
                show_names.append(info_)
            else:
                show_names.append("未知")


        # 班级人数
        num_of_class = self.face_info.number_of_people
        num_of_absent = num_of_class - number_of_check
        # 绘制文本
        text_ = ["班级人数：" + str(num_of_class),
                 "已到人数：" + str(number_of_check),
                 "未到人数：" + str(num_of_absent), "==未到名单=="]
        # 展示的字符串数组
        text_ = text_ + list_absent
        img_src = visualize(sign_in_img, self.det.result_msg, show_names, True)
        img_src = draw_text(img_src, text_)

        # 返回结果dict
        sign_msg = {
            'num_of_class': num_of_class,  # 班级人数
            'num_of_arrived': number_of_check,  # 到了的人数
            'num_of_detected': self.det.num_of_face,  # 图片中存在的人数
            'num_of_absent': num_of_absent,  # 缺勤的人数
            'show_names': show_names,  # 展示的名单
            'absent_names': list_absent,  # 缺勤名单
            'show_img': img_src  # 展示的图片
        }
        return sign_msg



if __name__ == "__main__":

    '''
    test_img
    "test_image/testface01.jpg"
    "test_image/aobama_t.png"
    "test_image/face/face04.jpg"
    "face_img/faces/face04.png"
    "test_image/12_Group_Group_12_Group_Group_12_36.jpg"
    "test_image/aobama_01.png"
    '''
    test_image_path = "face_img/class2/face04.jpg"
    test_image_path = os.path.join(ROOT, test_image_path)
    test_img = cv2.imread(test_image_path)
    ope = Operation()
    sign_msg = ope.sign_in(test_img)
    cv2.imshow("sign_in", sign_msg['show_img'])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


