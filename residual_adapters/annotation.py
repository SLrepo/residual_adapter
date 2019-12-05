import datetime
import json
import os
import re
import fnmatch
from PIL import Image


ROOT_DIR = '/home/sihui/Datasets/decathlon-1.0'
DATA_DIR = "/data/utensils/val"
IMAGE_DIR = os.path.join(ROOT_DIR, DATA_DIR)
ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations/utensils_val")

ID = 120000001
INFO = {
    "description": "utensils",
    "url": "http://homepages.inf.ed.ac.uk/rbf/UTENSILS/",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "Robert Fisher",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}

LICENSES = [
    {
        "id": 1,
        "name": "Sihui",
        "url": ""
    }
]

CATEGORIES = [{"id":120000001,"name":"Bottle Opener","supercategory":"utensils"},
{"id":120000002,"name":"Bread Knife","supercategory":"utensils"},
{"id":120000003,"name":"Can Opener","supercategory":"utensils"},
{"id":120000004,"name":"Dessert Spoon","supercategory":"utensils"},
{"id":120000005,"name":"Dinner Fork","supercategory":"utensils"},
{"id":120000006,"name":"Dinner Knife","supercategory":"utensils"},
{"id":120000007,"name":"Fish Slice","supercategory":"utensils"},
{"id":120000008,"name":"Kitchen Knife","supercategory":"utensils"},
{"id":120000009,"name":"Ladle","supercategory":"utensils"},
{"id":120000010,"name":"Masher","supercategory":"utensils"},
{"id":120000011,"name":"Peeler","supercategory":"utensils"},
{"id":120000012,"name":"Pizza Cutter","supercategory":"utensils"},
{"id":120000013,"name":"Potato Peeler","supercategory":"utensils"},
{"id":120000014,"name":"Serving Spoon","supercategory":"utensils"},
{"id":120000015,"name":"Soup Spoon","supercategory":"utensils"},
{"id":120000016,"name":"Spatula","supercategory":"utensils"},
{"id":120000017,"name":"Tea Spoon","supercategory":"utensils"},
{"id":120000018,"name":"Tongs","supercategory":"utensils"},
{"id":120000019,"name":"Whisk","supercategory":"utensils"},
{"id":120000020,"name":"Wooden Spoon","supercategory":"utensils"}
]


def main():
    coco_output = {
        "info": INFO,
        "images": [],
        "annotations": [],
        "licenses": LICENSES,
        "categories": CATEGORIES
    }

    image_id = ID
    category_id = ID
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