#
# boostcamp AI Tech
# Text Image Annotation Competition
#


import json


def read_json(ann_path: str) -> dict:
    with open(ann_path, 'r', encoding='UTF-8') as f:
        return json.load(f)


def write_json(annotation: dict, ann_path: str) -> None:
    with open(ann_path, 'w', encoding='UTF-8') as f:
        json.dump(annotation, f)
