import cv2
import os


def convert_mask_to_bbox(mask):
    _, threshold = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    bboxes = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        bbox = (x, y, w, h)
        bboxes.append(bbox)
    return bboxes


def normalize_bbox(bbox, image_width, image_height):
    x, y, w, h = bbox
    normalized_bbox = ((x+w/2) / image_width, (y+h/2) / image_height, w / image_width, h / image_height)
    return normalized_bbox


def save_yolo_labels(image_file, bboxes, class_index, label_file):
    image = cv2.imread(image_file)
    image_height, image_width, _ = image.shape
    with open(label_file, 'w') as f:
        for bbox in bboxes:
            normalized_bbox = normalize_bbox(bbox, image_width, image_height)
            label_line = f"{class_index} {normalized_bbox[0]} {normalized_bbox[1]} {normalized_bbox[2]} {normalized_bbox[3]}\n"
            f.write(label_line)

# def convert_one(image, mask, txt_path):
#     class_index = 0
#     label_file = os.path.join(txt_path, image[:-4] + '.txt')


def convert_all(image_path, mask_path, txt_path):
    images = os.listdir(image_path)
    class_index = 0
    count = 1

    for image in images:
        image_file = os.path.join(image_path, image)
        mask_file = os.path.join(mask_path, image)
        label_file = os.path.join(txt_path, image[:-4] + '.txt')

        mask = cv2.imread(mask_file, cv2.IMREAD_GRAYSCALE)
        bboxes = convert_mask_to_bbox(mask)
        save_yolo_labels(image_file, bboxes, class_index, label_file)
        print('process image ', count)
        count += 1
        # break


# 示例用法
train_image_path = "../original_data/detection/train/images/"
train_mask_path = "../original_data/detection/train/masks/"
train_txt_path = "../original_data/detection/train/labels/"

convert_all(train_image_path, train_mask_path, train_txt_path)

