import os

import numpy as np
import cv2
from _testcapi import FLT_MIN
from utils.util_url import ROOT
from models.face_detection import Detect
from utils.util_visualize import visualize


class SFace:  # 人脸识别
    def __init__(self, modelPath):
        self._model = cv2.dnn.readNet(modelPath)
        self._input_size = [112, 112]
        self._dst = np.array([
            [38.2946, 51.6963],
            [73.5318, 51.5014],
            [56.0252, 71.7366],
            [41.5493, 92.3655],
            [70.7299, 92.2041]
        ], dtype=np.float32)
        self._dst_mean = np.array([56.0262, 71.9008], dtype=np.float32)

    @property
    def name(self):
        return self.__class__.__name__

    def setBackend(self, backend_id):
        self._model.setPreferableBackend(backend_id)

    def setTarget(self, target_id):
        self._model.setPreferableTarget(target_id)

    def _preprocess(self, image, bbox):
        aligned_image = self._alignCrop(image, bbox)
        return cv2.dnn.blobFromImage(aligned_image)

    def infer(self, image, bbox):
        # Preprocess 预处理
        # inputBlob = self._preprocess(image, bbox)
        inputBlob = cv2.dnn.blobFromImage(self._alignCrop(image, bbox))
        # Forward
        self._model.setInput(inputBlob)
        outputBlob = self._model.forward()

        # Postprocess
        results = outputBlob / cv2.norm(outputBlob)
        return results

    def match_feature(self, feature, match_feature_image, match_feature_face, dis_type=0):

        feature2 = self.infer(match_feature_image, match_feature_face)

        if dis_type == 0:  # COSINE
            distance_ = np.sum(feature * feature2)
            threshold = 0.363
            msg_ = 1 if distance_ >= threshold else 0
            return distance_, msg_
        elif dis_type == 1:  # NORM_L2
            threshold = 1.128
            distance_ = cv2.norm(feature, feature2)
            msg_ = 1 if distance_ <= threshold else 0
            return distance_, msg_
        else:
            raise NotImplementedError()

    def match(self, image1, face1, image2, face2, dis_type=0):
        feature1 = self.infer(image1, face1)
        feature2 = self.infer(image2, face2)

        if dis_type == 0:  # COSINE
            distance = np.sum(feature1 * feature2)
            threshold = 0.363
            msg = 1 if distance >= threshold else 0
            return distance, msg
        elif dis_type == 1:  # NORM_L2
            threshold = 1.128
            distance = cv2.norm(feature1, feature2)
            msg = 1 if distance <= threshold else 0
            return distance, msg
        else:
            raise NotImplementedError()

    def _alignCrop(self, image, face):
        # Retrieve landmarks 检索地标
        if face.shape[-1] == (4 + 5 * 2):
            landmarks = face[4:].reshape(5, 2)
        else:
            raise NotImplementedError()
        warp_mat = self._getSimilarityTransformMatrix(landmarks)
        aligned_image = cv2.warpAffine(image, warp_mat, self._input_size, flags=cv2.INTER_LINEAR)
        return aligned_image

    def _getSimilarityTransformMatrix(self, src):
        # compute the mean of src and dst
        src_mean = np.array([np.mean(src[:, 0]), np.mean(src[:, 1])], dtype=np.float32)
        dst_mean = np.array([56.0262, 71.9008], dtype=np.float32)
        # subtract the means from src and dst
        src_demean = src.copy()
        src_demean[:, 0] = src_demean[:, 0] - src_mean[0]
        src_demean[:, 1] = src_demean[:, 1] - src_mean[1]
        dst_demean = self._dst.copy()
        dst_demean[:, 0] = dst_demean[:, 0] - dst_mean[0]
        dst_demean[:, 1] = dst_demean[:, 1] - dst_mean[1]

        A = np.array([[0., 0.], [0., 0.]], dtype=np.float64)
        for i in range(5):
            A[0][0] += dst_demean[i][0] * src_demean[i][0]
            A[0][1] += dst_demean[i][0] * src_demean[i][1]
            A[1][0] += dst_demean[i][1] * src_demean[i][0]
            A[1][1] += dst_demean[i][1] * src_demean[i][1]
        A = A / 5

        d = np.array([1.0, 1.0], dtype=np.float64)
        if A[0][0] * A[1][1] - A[0][1] * A[1][0] < 0:
            d[1] = -1

        T = np.array([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ], dtype=np.float64)

        s, u, vt = cv2.SVDecomp(A)
        smax = s[0][0] if s[0][0] > s[1][0] else s[1][0]
        tol = smax * 2 * FLT_MIN
        rank = int(0)
        if s[0][0] > tol:
            rank += 1
        if s[1][0] > tol:
            rank += 1
        det_u = u[0][0] * u[1][1] - u[0][1] * u[1][0]
        det_vt = vt[0][0] * vt[1][1] - vt[0][1] * vt[1][0]
        if rank == 1:
            if det_u * det_vt > 0:
                uvt = np.matmul(u, vt)
                T[0][0] = uvt[0][0]
                T[0][1] = uvt[0][1]
                T[1][0] = uvt[1][0]
                T[1][1] = uvt[1][1]
            else:
                temp = d[1]
                d[1] = -1
                D = np.array([[d[0], 0.0], [0.0, d[1]]], dtype=np.float64)
                Dvt = np.matmul(D, vt)
                uDvt = np.matmul(u, Dvt)
                T[0][0] = uDvt[0][0]
                T[0][1] = uDvt[0][1]
                T[1][0] = uDvt[1][0]
                T[1][1] = uDvt[1][1]
                d[1] = temp
        else:
            D = np.array([[d[0], 0.0], [0.0, d[1]]], dtype=np.float64)
            Dvt = np.matmul(D, vt)
            uDvt = np.matmul(u, Dvt)
            T[0][0] = uDvt[0][0]
            T[0][1] = uDvt[0][1]
            T[1][0] = uDvt[1][0]
            T[1][1] = uDvt[1][1]

        var1 = 0.0
        var2 = 0.0
        for i in range(5):
            var1 += src_demean[i][0] * src_demean[i][0]
            var2 += src_demean[i][1] * src_demean[i][1]
        var1 /= 5
        var2 /= 5

        scale = 1.0 / (var1 + var2) * (s[0][0] * d[0] + s[1][0] * d[1])
        TS = [
            T[0][0] * src_mean[0] + T[0][1] * src_mean[1],
            T[1][0] * src_mean[0] + T[1][1] * src_mean[1]
        ]
        T[0][2] = dst_mean[0] - scale * TS[0]
        T[1][2] = dst_mean[1] - scale * TS[1]
        T[0][0] *= scale
        T[0][1] *= scale
        T[1][0] *= scale
        T[1][1] *= scale
        return np.array([
            [T[0][0], T[0][1], T[0][2]],
            [T[1][0], T[1][1], T[1][2]]
        ], dtype=np.float64)


# 权重文件路径
weight_face_recognition = os.path.join(ROOT, "weights/face_recognition_sface.onnx")
# 人脸比较实例
recognizer = SFace(weight_face_recognition)


class Recognition:
    def __init__(self):
        self.recognizer = SFace(weight_face_recognition)
        # 特征号列表
        self.feature1_list = []

    # 计算特征号
    def infer(self, image, bbox):
        return self.recognizer.infer(image, bbox)

    # 计算特征号
    def infers(self, images, bboxs):
        self.feature1_list = []
        for image_, bbox_ in zip(images, bboxs):
            feature1 = self.infer(image_, bbox_[:-1])
            self.feature1_list.append(feature1)

    def match_feature(self, target_img, target_infos):

        # 源拷贝
        target_infos = target_infos.copy()

        result_map = np.full((len(target_infos), 2), -1.)

        for source_index, feature1 in enumerate(self.feature1_list):

            cos = 0
            img_index = 0
            img_cur = -1
            for target_info in target_infos:
                if target_info[-1] == -1.:
                    img_index += 1
                    continue
                distance_, msg_ = self.recognizer.match_feature(feature1, target_img, target_info[:-1])
                if msg_:  # 可能是同一个人
                    if cos < distance_:  # 选取最相似的
                        cos = distance_
                        img_cur = img_index

                img_index += 1
            # 排除已选择的图片和信息
            if img_cur != -1:
                result_map[img_cur][0] = source_index
                result_map[img_cur][1] = float(format(cos, ".2f"))
                target_info[-1] = -1.
        return result_map

    def match(self, target_img, target_info, source_img, source_info):
        # 返回相似度，是否同一人
        return self.recognizer.match(target_img, target_info[0][:-1], source_img, source_info[0][:-1])



from models.load_face_info import Faces_Info
# test
if __name__ == "__main__":

    # print("距离:", distance, "是否同一人:", msg)
    face_info = Faces_Info(r"D:\githubcode\wisdom_classroom\face_img\faces\names.txt")
    face_info.load_xywh_info(False)
    # 源数据
    det1 = Detect()
    det1.face_detectAll(face_info.face_img)
    # for x in range(4):
    #     cv2.imshow("wind", det1.one_face_list[x])
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    det2 = Detect()
    # 目标图片 r"D:\githubcode\wisdom_classroom\face_img\faces\face04.png"
    # r"D:\githubcode\wisdom_classroom\test_image\testface01.jpg"
    # r"D:\githubcode\wisdom_classroom\aobama_t.png"
    target_path = ROOT+"/face_img/class2/face04.jpg"
    target_img = cv2.imread(target_path)
    det2.face_detect(target_img)

    recog = Recognition()
    # 计算feature1s
    recog.infers(det1.one_face_list, det1.result_msg)

    res_map = recog.match_feature(det2.cur_img, det2.result_msg)
    show_text = []
    for idx, idx2 in enumerate(res_map):
        if idx2[0] != -1.:
            show_text.append(face_info.names[int(idx2[0])])
        else:
            show_text.append("未知")

    show_img = visualize(target_img, det2.result_msg, show_text, True)
    cv2.imshow("wind", show_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

