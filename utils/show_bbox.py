import os
import time

import cv2
import numpy as np


def draw_bounding_boxes(image_path, label_path):
    # 加载图像
    image = cv2.imread(image_path)

    # 读取标签文件
    with open(label_path, 'r') as file:
        lines = file.readlines()

    # 绘制边界框
    for line in lines:
        # 提取边界框坐标和类别信息
        line = line.strip().split()
        class_id = int(line[0])
        x, y, w, h = map(float, line[1:])

        # 计算边界框的坐标
        left = int((x - w / 2) * image.shape[1])
        top = int((y - h / 2) * image.shape[0])
        right = int((x + w / 2) * image.shape[1])
        bottom = int((y + h / 2) * image.shape[0])

        # 绘制边界框矩形和类别标签
        color = (0, 255, 0)  # 绿色边界框
        thickness = 2
        cv2.rectangle(image, (left, top), (right, bottom), color, thickness)
        cv2.putText(image, str(class_id), (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

    # 显示图像
    cv2.imshow("Image with Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# # 示例用法
# image_path = 'path/to/image.jpg'
# label_path = 'path/to/label.txt'
# draw_bounding_boxes(image_path, label_path)


image_path = '../original_data/detection/train/images/'
label_path = '../original_data/detection/train/labels/'

images = os.listdir(image_path)
for image in images:
    label = image[:-4] + '.txt'
    print(image_path + image)
    print(label_path + label)
    draw_bounding_boxes(image_path + image, label_path + label)



# mask_path = '../original_data/detection/train/masks/20150919_174730_apple161.jpg'
# image_path = '../original_data/detection/train/images/20150919_174730_apple161.jpg'
# label_path = '../original_data/detection/train/labels/20150919_174730_apple161.txt'
# draw_bounding_boxes(image_path, label_path)

