import cv2
import sys
sys.path.append(r".\face")
import numpy as np
import os
from label_pre import label_pre_one_hot
import math


def read_rawdata(channels, path, image_name_list):
    assert os.path.exists(path)

    img_list = []

    for name in image_name_list:
        full_path = os.path.join(path, name)
        if not os.path.exists(full_path):
            print("数据缺失：", name)
            img_list.append(None)
            continue
        img = np.fromfile(full_path, dtype='uint8')
        n = int(math.sqrt(img.shape[0]))
        img = img.reshape(n, n, channels)
        img_list.append(img)
    return img_list


if __name__ == '__main__':
    channels = 1  # 图像的通道数，灰度图为1
    path_rawdata = r"../face/rawdata"
    path_label = r"../face/faceDR"
    label_one_hot, img_name = label_pre_one_hot(path_label)
    img_list = read_rawdata(channels, path_rawdata, img_name) #图片矩阵
    for img in img_list:
        if img is not None:
            cv2.imshow("asdf", img)
            cv2.waitKey(1)
    print(img_list)



