import cv2
import numpy as np
from utils.ChineseText import ft


def visualize(image, results, texts=[], haveText=False,
              box_color=(0, 255, 0), text_color=(0, 0, 255),
              font_size=12):
    # 展示
    output = image.copy()

    # landmark_color = [
    #     (255, 0, 0),  # right eye
    #     (0, 0, 255),  # left eye
    #     (0, 255, 0),  # nose tip
    #     (255, 0, 255),  # right mouth corner
    #     (0, 255, 255)  # left mouth corner
    # ]

    for index, det in enumerate(results):
        # 画框
        bbox = det[0:4].astype(np.int32)
        cv2.rectangle(output, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), box_color, 2)
        # 画文字
        if haveText:
            output = ft.draw_text(output, bbox, texts[index], font_size)

        # if accuracy:
        #     conf = det[-1]
        #     cv2.putText(output, '{:.2f}'.format(conf), (bbox[0], bbox[1] + 12), cv2.FONT_HERSHEY_DUPLEX, 0.5,
        #                 text_color)

        # landmarks = det[4:14].astype(np.int32).reshape((5,2))
        # for idx, landmark in enumerate(landmarks):
        #     cv2.circle(output, landmark, 2, landmark_color[idx], 2)
    return output


def draw_text(image, str_list, h=4, w=4, font_size=12):
    pos = [w, h]
    for str_ in str_list:
        image = ft.draw_text(image, pos, str_, text_size=font_size, text_color=(255, 0, 0))
        pos = [w, (h + font_size)+pos[1]]
    return image
