import numpy as np
import cv2
from itertools import product
import os
from utils.util_url import ROOT

from utils.util_visualize import visualize


class YuNet:  # 人脸检测模型
    # 1. 模型，2.网络输入尺寸 3.配置阈值 4.非极大值抑制 5.在 NMS 之前保留 top_k 个边界框 6.在 NMS 之后保留 keep_top_k 个边界框
    def __init__(self, modelPath, inputSize=[640, 480], confThreshold=0.9, nmsThreshold=0.3, topK=5000, keepTopK=750):
        self._model = cv2.dnn.readNet(modelPath)
        self._inputNames = ''
        self._outputNames = ['loc', 'conf', 'iou']
        self._inputSize = inputSize  # [w, h]
        self._confThreshold = confThreshold
        self._nmsThreshold = nmsThreshold
        self._topK = topK
        self._keepTopK = keepTopK
        self._min_sizes = [[10, 16, 24], [32, 48], [64, 96], [128, 192, 256]]
        self._steps = [8, 16, 32, 64]
        self._variance = [0.1, 0.2]

        # Generate priors 生成先验
        self._priorGen()

    @property
    def name(self):
        return self.__class__.__name__

    def setBackend(self, backend):
        self._model.setPreferableBackend(backend)

    def setTarget(self, target):
        self._model.setPreferableTarget(target)

    def setInputSize(self, input_size):
        self._inputSize = input_size  # [w, h]
        # Regenerate priors 重新生成先验
        self._priorGen()

    def infer(self, image):  # 分析图片得到分析信息
        assert image.shape[0] == self._inputSize[1], '{} (height of input image) != {} (preset height)'.format(image.shape[0], self._inputSize[1])
        assert image.shape[1] == self._inputSize[0], '{} (width of input image) != {} (preset width)'.format(image.shape[1], self._inputSize[0])

        # Preprocess 预处理 包括减均值，比例缩放，裁剪，交换通道等，返回一个4通道的blob(blob可以简单理解为一个N维的数组，用于神经网络的输入)
        inputBlob = cv2.dnn.blobFromImage(image)

        # Forward 向前
        self._model.setInput(inputBlob, self._inputNames)
        outputBlob = self._model.forward(self._outputNames)

        # Postprocess 后期过程
        results = self._postprocess(outputBlob)
        # for result in results:
        #     print(result[:4])
        return results

    def _postprocess(self, outputBlob):
        # Decode 解码
        dets = self._decode(outputBlob)

        # NMS 非极大值抑制
        keepIdx = cv2.dnn.NMSBoxes(
            bboxes=dets[:, 0:4].tolist(),
            scores=dets[:, -1].tolist(),
            score_threshold=self._confThreshold,
            nms_threshold=self._nmsThreshold,
            top_k=self._topK
        )  # box_num x class_num
        if len(keepIdx) > 0:
            dets = dets[keepIdx]
            # dets = np.squeeze(dets, axis=1)
            return dets[:self._keepTopK]
        else:
            return np.empty(shape=(0, 15))

    def _priorGen(self):
        w, h = self._inputSize
        feature_map_2th = [int(int((h + 1) / 2) / 2),
                           int(int((w + 1) / 2) / 2)]
        feature_map_3th = [int(feature_map_2th[0] / 2),
                           int(feature_map_2th[1] / 2)]
        feature_map_4th = [int(feature_map_3th[0] / 2),
                           int(feature_map_3th[1] / 2)]
        feature_map_5th = [int(feature_map_4th[0] / 2),
                           int(feature_map_4th[1] / 2)]
        feature_map_6th = [int(feature_map_5th[0] / 2),
                           int(feature_map_5th[1] / 2)]

        feature_maps = [feature_map_3th, feature_map_4th,
                        feature_map_5th, feature_map_6th]

        priors = []
        for k, f in enumerate(feature_maps):
            min_sizes = self._min_sizes[k]
            for i, j in product(range(f[0]), range(f[1])):  # i->h, j->w
                for min_size in min_sizes:
                    s_kx = min_size / w
                    s_ky = min_size / h

                    cx = (j + 0.5) * self._steps[k] / w
                    cy = (i + 0.5) * self._steps[k] / h

                    priors.append([cx, cy, s_kx, s_ky])
        self.priors = np.array(priors, dtype=np.float32)

    def _decode(self, outputBlob):
        loc, conf, iou = outputBlob
        # get score
        cls_scores = conf[:, 1]  # cls 分数
        iou_scores = iou[:, 0]  # IoU 计算的是 “预测的边框” 和 “真实的边框” 的交集和并集的比值
        # clamp
        _idx = np.where(iou_scores < 0.)  # 输出满足条件 (即非0) 元素的坐标
        iou_scores[_idx] = 0.
        _idx = np.where(iou_scores > 1.)
        iou_scores[_idx] = 1.
        scores = np.sqrt(cls_scores * iou_scores)
        scores = scores[:, np.newaxis]

        scale = np.array(self._inputSize)

        # get bboxes
        bboxes = np.hstack((
            (self.priors[:, 0:2] + loc[:, 0:2] * self._variance[0] * self.priors[:, 2:4]) * scale,
            (self.priors[:, 2:4] * np.exp(loc[:, 2:4] * self._variance)) * scale
        ))
        # (x_c, y_c, w, h) -> (x1, y1, w, h)
        bboxes[:, 0:2] -= bboxes[:, 2:4] / 2

        # get landmarks
        landmarks = np.hstack((
            (self.priors[:, 0:2] + loc[:,  4: 6] * self._variance[0] * self.priors[:, 2:4]) * scale,
            (self.priors[:, 0:2] + loc[:,  6: 8] * self._variance[0] * self.priors[:, 2:4]) * scale,
            (self.priors[:, 0:2] + loc[:,  8:10] * self._variance[0] * self.priors[:, 2:4]) * scale,
            (self.priors[:, 0:2] + loc[:, 10:12] * self._variance[0] * self.priors[:, 2:4]) * scale,
            (self.priors[:, 0:2] + loc[:, 12:14] * self._variance[0] * self.priors[:, 2:4]) * scale
        ))
        # 水平拼接
        dets = np.hstack((bboxes, landmarks, scores))  # 坐标，特征标记，得分
        return dets


# 权重文件路径
weight_face_detection = os.path.join(ROOT, "weights/face_detection_yunet.onnx")
# 人脸检测实例
detector = YuNet(weight_face_detection, confThreshold=0.9, nmsThreshold=0.3, topK=5000, keepTopK=750)


class Detect:
    """
    人脸检测
        # 检测结果信息
        result_msg
        # [ [x,y,w,h], ...]
        xywh_list
        # 单人人脸图片
        one_face_list = []
        # 检测到的人脸数
        num_of_face = 0
    """
    def __init__(self):

        # 人脸检测器
        self.detector = YuNet(weight_face_detection, confThreshold=0.9, nmsThreshold=0.3, topK=5000, keepTopK=750)

        # cur
        self.cur_img = None
        # 检测结果信息
        self.result_msg = []
        # [ [x,y,w,h], ...]
        self.xywh_list = []
        # 单人人脸图片
        self.one_face_list = []
        # 检测到的人脸数
        self.num_of_face = 0

    def face_detect(self, face_detect_img):
        # w,h
        self.detector.setInputSize([face_detect_img.shape[1], face_detect_img.shape[0]])
        self.result_msg = self.detector.infer(face_detect_img)
        # [[x,y,w,h
        self.xywh_list = self.result_msg[:, 0:4].astype(np.int32)
        # face imgs
        self.cur_img = face_detect_img

        # 脸数
        self.num_of_face = len(self.xywh_list)

    def face_detectAll(self, face_detectAll_imgs):
        # 初始化
        self.result_msg = []
        self.xywh_list = []
        self.one_face_list = []

        for face_detectAll_img in face_detectAll_imgs:
            self.detector.setInputSize([face_detectAll_img.shape[1], face_detectAll_img.shape[0]])
            one_face_result = self.detector.infer(face_detectAll_img)[0]
            self.result_msg.append(one_face_result)

            xywh = one_face_result[0:4].astype(np.int32)
            self.xywh_list.append(xywh)

        self.one_face_list = face_detectAll_imgs.copy()
        self.num_of_face = len(self.xywh_list)

    def xywh_to_yydxxd(self):
        """
        图片三维 (h,w,RGB),方便裁剪图片
        :return: [[y,yend,x,xend
        """
        return [(y, y+h, x, x+w) for x, y, w, h in self.xywh_list]


if __name__ == "__main__":
    img = os.path.join(ROOT, "test_image/address.jpg")  # test_image/12_Group_Group_12_Group_Group_12_36.jpg
    print("权重文件路径:", weight_face_detection)
    print("测试图片路径", img)
    src_img = cv2.imread(img)

    src_img_resize = cv2.resize(src_img, (640, 480), interpolation=cv2.INTER_AREA)
    # detector.setInputSize([src_img.shape[1], src_img.shape[0]])
    # results = detector.infer(src_img)
    # src_img = visualize(src_img, results)
    #
    # winName = 'test_detection'
    # cv2.namedWindow(winName, 0)
    # cv2.imshow(winName, src_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    det = Detect()
    det.face_detect(src_img_resize)
    # print(det.xywh_list)
    print(len(det.result_msg))
    img_ = visualize(det.cur_img, det.result_msg)
    cv2.imshow("detect", img_)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

