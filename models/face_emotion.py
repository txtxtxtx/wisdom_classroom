import os
# 在import tensorflow之前
# import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'  # 用cpu
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # log等级
from utils.util_url import ROOT
from utils.util_visualize import visualize
from models.face_detection import Detect
# 表情识别
import cv2
from keras.models import load_model
import numpy as np


class Emotion:
    def __init__(self):

        self.emotion_classifier = load_model(ROOT + "/weights/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5")

        self.emotion_labels = {
            0: '生气',
            1: '厌恶',
            2: '恐惧',
            3: '开心',
            4: '难过',
            5: '惊喜',
            6: '平静'
        }
        # 默认情绪
        self.cur_emotion = '平静'

    def face_emotion(self, face_emotion_img, yydxxd=[], cut=False):
        yxd = []
        if cut:
            yxd = yydxxd
        else:
            img_shape = face_emotion_img.shape
            yxd = [0, img_shape[0], 0, img_shape[1]]

        # 转为灰度图片
        gray_face = cv2.cvtColor(face_emotion_img, cv2.COLOR_BGR2GRAY)
        # 人脸图片裁取
        gray_face = gray_face[yxd[0]:yxd[1], yxd[2]:yxd[3]]

        gray_face = cv2.resize(gray_face, (64, 64))
        gray_face = gray_face / 255.0
        gray_face = np.expand_dims(gray_face, 0)
        gray_face = np.expand_dims(gray_face, -1)

        emotion_label_index = np.argmax(self.emotion_classifier.predict(gray_face))
        self.cur_emotion = self.emotion_labels[emotion_label_index]
        return self.cur_emotion


if __name__ == "__main__":
    img_path = os.path.join(ROOT, "test_image/aobama_t.png")

    img_ = cv2.imread(img_path)

    emo = Emotion()
    det = Detect()

    det.face_detect(img_)
    yydxxd = det.xywh_to_yydxxd()

    emo_list = []
    for yxd in yydxxd:
        one_emo = emo.face_emotion(img_, yxd, True)  # 需要剪裁
        emo_list.append(one_emo)

    show_img = visualize(img_, det.xywh_list, emo_list, True)
    cv2.imshow('emotion', show_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# def face_emotion():
#
#     emotion_classifier = load_model(ROOT + "/weights/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5")
#
#     emotion_labels = {
#         0: '生气',
#         1: '厌恶',
#         2: '恐惧',
#         3: '开心',
#         4: '难过',
#         5: '惊喜',
#         6: '平静'
#     }
#     ap.load_img(ROOT + "/test_image/face/emotion_fear.png")
#     img = ap.cur_img
#     ans = ap.detect_of_one()
#     dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     face_res = ans[0:4].astype(np.int32)
#
#     gray_face = dst[(face_res[1]):(face_res[1] + face_res[3]), (face_res[0]):(face_res[0] + face_res[2])]
#     gray_face = cv2.resize(gray_face, (64, 64))
#     gray_face = gray_face / 255.0
#     gray_face = np.expand_dims(gray_face, 0)
#     gray_face = np.expand_dims(gray_face, -1)
#
#     emotion_label_arg = np.argmax(emotion_classifier.predict(gray_face))
#     print(emotion_labels[emotion_label_arg])
#     img = visualize(img, [face_res])
#     img = ft.draw_text(img, face_res, emotion_labels[emotion_label_arg], 24)
#
#     cv2.imshow('ss', img)
#     cv2.waitKey(0)
#     pass
