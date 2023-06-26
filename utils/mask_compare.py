import os
import time

import cv2
import numpy as np


def mask_compare(image_path, mask_path):
    # 读取图像和掩码
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # 将掩码应用于图像
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # 创建一个空的比较结果图像
    comparison = np.hstack((image, masked_image))

    # 显示图像和掩码的比较结果
    cv2.imshow("Image and Mask Comparison", comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = '../original_data/train/images/'
mask_path = '../original_data/train/masks/'

images = os.listdir(image_path)
for image in images:
    print(image_path + image)
    mask_compare(image_path+image, mask_path+image)
    time.sleep(0.1)
