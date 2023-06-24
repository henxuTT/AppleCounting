import cv2
import numpy as np
import os


def convert_mask_to_bbox(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    bboxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        bbox = (x, y, w, h)
        bboxes.append(bbox)
    return bboxes


def normalize_bbox(bbox, image_width, image_height):
    x, y, w, h = bbox
    normalized_bbox = (x / image_width, y / image_height, w / image_width, h / image_height)
    return normalized_bbox


def save_yolo_labels(image_file, bboxes, class_index, label_file):
    image = cv2.imread(image_file)
    image_height, image_width, _ = image.shape
    with open(label_file, 'w') as f:
        for bbox in bboxes:
            normalized_bbox = normalize_bbox(bbox, image_width, image_height)
            label_line = f"{class_index} {normalized_bbox[0]} {normalized_bbox[1]} {normalized_bbox[2]} {normalized_bbox[3]}\n"
            f.write(label_line)


def convert(image_path, mask_path, txt_path):
    images = os.listdir(image_path)
    class_index = 0
    count = 0

    for image in images:
        image_file = os.path.join(image_path, image)
        mask_file = os.path.join(mask_path, image)
        label_file = os.path.join(txt_path, image[:-4] + '.txt')

        mask = cv2.imread(mask_file, cv2.IMREAD_GRAYSCALE)
        bboxes = convert_mask_to_bbox(mask)
        save_yolo_labels(image_file, bboxes, class_index, label_file)
        print('process image ', count)
        count += 1


# 示例用法
train_image_path = "../../detection/images/train/"
train_mask_path = "../../detection/train/masks/"
train_txt_path = "../../detection/labels/train/"
# test_image_path = "../data/detection/test/train/"
# test_mask_path = "../data/detection/test/masks/"
# test_txt_path = "../data/detection/test/train/"

convert(train_image_path, train_mask_path, train_txt_path)
# convert(test_image_path, test_mask_path, test_txt_path)
