import os
import cv2
from models.face_detection import detector
from utils.util_url import ROOT


class Faces_Info:  # 迭代获取[name,img_name],[face_img]
    def __init__(self, info_txt):  # 描述信息文件名
        self.info_txt = info_txt
        # 脸所在的文件夹名字
        self.imgs_path = os.path.dirname(info_txt)

        self.face_info_list = []
        # 人脸
        self.face_img = []
        # 名字
        self.names = []
        # 人数
        self.number_of_people = 0

        # 坐标宽高等信息 [[x,y,w,h,...
        self.xywh_info = []

        # 加载是否完成
        self.loaded_info = []

        try:
            face_info = open(self.info_txt, 'r', encoding='utf-8')
            while True:
                infos = face_info.readline()
                if infos == "end" or infos == "\n":
                    break
                infolist = infos.split(" ")
                infolist[1] = infolist[1][:-1]
                self.face_info_list.append(infolist)
        except IOError:
            self.loaded_info.append("打开["+self.info_txt+"]失败")
        else:
            face_info.close()

        self.names = [info[0] for info in self.face_info_list]
        self.number_of_people = len(self.face_info_list)

        self.__loadImg__()

    def __loadImg__(self):
        for name, imgpath in self.face_info_list:
            imgpath = os.path.join(self.imgs_path, imgpath)

            load_img = cv2.imread(imgpath)
            if load_img is None:
                self.loaded_info.append("图片["+imgpath+"]加载失败")
            else:
                self.face_img.append(load_img)

    def load_xywh_info(self, info_change=True):
        """
        加载人脸坐标宽高等信息 [[x,y,w,h,...
        :param info_change: 消息是否改变
        :return:
        """
        xywh_info_path = os.path.join(self.imgs_path, 'xywh_info.info')
        # 有坐标信息&&信息没有改变直接读
        if os.path.exists(xywh_info_path) and not info_change:
            try:
                xywh_info_reader = open(xywh_info_path, "r", encoding="utf-8")
                while True:
                    line = xywh_info_reader.readline()
                    if not line:
                        break
                    row = [float(i) for i in line.split(" ")]
                    self.xywh_info.append(row)
            except IOError:
                self.loaded_info.append("坐标信息文件打开失败")
            else:
                xywh_info_reader.close()
        # 没有就去检测，并创建该文件
        else:
            for img_ in self.face_img:
                # 设置宽长 [h, w]
                detector.setInputSize([img_.shape[1], img_.shape[0]])
                # 检测结果添加进 xywh_info 数组
                self.xywh_info.append(detector.infer(img_)[0])
            # print(str(self.xywh_info))
            try:
                file = open(xywh_info_path, 'w', encoding="utf-8")
                for list_ in self.xywh_info:
                    last = len(list_) - 1
                    for index_, num in enumerate(list_):
                        if last == index_:
                            file.write(str(num) + "\n")
                        else:
                            file.write(str(num) + " ")
            except IOError:
                self.loaded_info.append("坐标文件创建失败")
            else:
                file.close()
                if len(self.loaded_info) == 0:
                    self.loaded_info = True
                else:
                    self.loaded_info = False


if __name__ == "__main__":
    # test
    fi = Faces_Info(r"D:\githubcode\wisdom_classroom\face_img\faces\names.txt")
    xywh_info_path = os.path.join(ROOT, "face_img/xywh_info.txt")
    fi.load_xywh_info()
    for index in range(fi.number_of_people):
        print(fi.names[index])

        cv2.imshow("111", fi.face_img[index])
        cv2.waitKey(0)
        cv2.destroyAllWindows()


