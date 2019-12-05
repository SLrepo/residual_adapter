import datetime
import json
import os
import re
import fnmatch
from PIL import Image


ROOT_DIR = '/home/sihui/Datasets/decathlon-1.0'
DATA_DIR = "/data/homeoffice/val"
IMAGE_DIR = os.path.join(ROOT_DIR, DATA_DIR)
ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations/homeoffice_val")

ID = 110000001
INFO = {
    "description": "HomeOffice",
    "url": "http://hemanthdv.org/OfficeHome-Dataset/",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "Hemanth Venkateswara",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Sihui",
        "url": ""
    }
]

CATEGORIES = [{"id":110000001,"name":"Alarm Clock","supercategory":"homeoffice"},
{"id":110000002,"name":"Backpack","supercategory":"homeoffice"},
{"id":110000003,"name":"Batteries","supercategory":"homeoffice"},
{"id":110000004,"name":"Bed","supercategory":"homeoffice"},
{"id":110000005,"name":"Bike","supercategory":"homeoffice"},
{"id":110000006,"name":"Bottle","supercategory":"homeoffice"},
{"id":110000007,"name":"Bucket","supercategory":"homeoffice"},
{"id":110000008,"name":"Calculator","supercategory":"homeoffice"},
{"id":110000009,"name":"Calendar","supercategory":"homeoffice"},
{"id":110000010,"name":"Candles","supercategory":"homeoffice"},
{"id":110000011,"name":"Chair","supercategory":"homeoffice"},
{"id":110000012,"name":"Clipboards","supercategory":"homeoffice"},
{"id":110000013,"name":"Computer","supercategory":"homeoffice"},
{"id":110000014,"name":"Couch","supercategory":"homeoffice"},
{"id":110000015,"name":"Curtains","supercategory":"homeoffice"},
{"id":110000016,"name":"Desk Lamp","supercategory":"homeoffice"},
{"id":110000017,"name":"Drill","supercategory":"homeoffice"},
{"id":110000018,"name":"Eraser","supercategory":"homeoffice"},
{"id":110000019,"name":"Exit Sign","supercategory":"homeoffice"},
{"id":110000020,"name":"Fan","supercategory":"homeoffice"},
{"id":110000021,"name":"File Cabinet","supercategory":"homeoffice"},
{"id":110000022,"name":"Flipflops","supercategory":"homeoffice"},
{"id":110000023,"name":"Flowers","supercategory":"homeoffice"},
{"id":110000024,"name":"Folder","supercategory":"homeoffice"},
{"id":110000025,"name":"Fork","supercategory":"homeoffice"},
{"id":110000026,"name":"Glasses","supercategory":"homeoffice"},
{"id":110000027,"name":"Hammer","supercategory":"homeoffice"},
{"id":110000028,"name":"Helmet","supercategory":"homeoffice"},
{"id":110000029,"name":"Kettle","supercategory":"homeoffice"},
{"id":110000030,"name":"Keyboard","supercategory":"homeoffice"},
{"id":110000031,"name":"Knives","supercategory":"homeoffice"},
{"id":110000032,"name":"Lamp Shade","supercategory":"homeoffice"},
{"id":110000033,"name":"Laptop","supercategory":"homeoffice"},
{"id":110000034,"name":"Marker","supercategory":"homeoffice"},
{"id":110000035,"name":"Monitor","supercategory":"homeoffice"},
{"id":110000036,"name":"Mop","supercategory":"homeoffice"},
{"id":110000037,"name":"Mouse","supercategory":"homeoffice"},
{"id":110000038,"name":"Mug","supercategory":"homeoffice"},
{"id":110000039,"name":"Notebook","supercategory":"homeoffice"},
{"id":110000040,"name":"Oven","supercategory":"homeoffice"},
{"id":110000041,"name":"Pan","supercategory":"homeoffice"},
{"id":110000042,"name":"Paper Clip","supercategory":"homeoffice"},
{"id":110000043,"name":"Pen","supercategory":"homeoffice"},
{"id":110000044,"name":"Pencil","supercategory":"homeoffice"},
{"id":110000045,"name":"Postit Notes","supercategory":"homeoffice"},
{"id":110000046,"name":"Printer","supercategory":"homeoffice"},
{"id":110000047,"name":"Push Pin","supercategory":"homeoffice"},
{"id":110000048,"name":"Radio","supercategory":"homeoffice"},
{"id":110000049,"name":"Refrigerator","supercategory":"homeoffice"},
{"id":110000050,"name":"ruler","supercategory":"homeoffice"},
{"id":110000051,"name":"Scissors","supercategory":"homeoffice"},
{"id":110000052,"name":"Screwdriver","supercategory":"homeoffice"},
{"id":110000053,"name":"Shelf","supercategory":"homeoffice"},
{"id":110000054,"name":"Sink","supercategory":"homeoffice"},
{"id":110000055,"name":"Sneakers","supercategory":"homeoffice"},
{"id":110000056,"name":"Soda","supercategory":"homeoffice"},
{"id":110000057,"name":"Speaker","supercategory":"homeoffice"},
{"id":110000058,"name":"Spoon","supercategory":"homeoffice"},
{"id":110000059,"name":"Table","supercategory":"homeoffice"},
{"id":110000060,"name":"Telephone","supercategory":"homeoffice"},
{"id":110000061,"name":"Toothbrush","supercategory":"homeoffice"},
{"id":110000062,"name":"Toys","supercategory":"homeoffice"},
{"id":110000063,"name":"Trash Can","supercategory":"homeoffice"},
{"id":110000064,"name":"TV","supercategory":"homeoffice"},
{"id":110000065,"name":"Webcam","supercategory":"homeoffice"}
]


def main():
    coco_output = {
        "info": INFO,
        "images": [],
        "annotations": [],
        "licenses": LICENSES,
        "categories": CATEGORIES
    }

    image_id = 110000001
    category_id = 110000001
    # segmentation_id = 110000001
    lst = os.listdir(ROOT_DIR + DATA_DIR)
    lst.sort()
    for subdir in lst:
        subdir_input = ROOT_DIR + DATA_DIR + "/" + subdir
        img_lst = os.listdir(subdir_input)
        img_lst.sort()
        for image_filename in img_lst:
            image_full_path = subdir_input + "/" + image_filename
            image = Image.open(image_full_path)
            width, height = image.size
            image_info = {"id":image_id, "width":width, "height":height, "file_name": DATA_DIR + "/" + subdir + "/" + image_filename}
            coco_output["images"].append(image_info)
            annotation_info = {"id":image_id, "image_id": image_id, "category_id": category_id, "segmentation":[], "area":0, "bbox":[], "iscrowd":0}
            coco_output["annotations"].append(annotation_info)
            image_id = image_id + 1
        category_id = category_id + 1

    with open('{}.json'.format(ANNOTATION_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)


if __name__ == "__main__":
    main()