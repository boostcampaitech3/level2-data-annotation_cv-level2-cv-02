#
# boostcamp AI Tech
# Text Image Annotation Competition
#


from json_io import read_json, write_json


ANNOTATION_1 = '/opt/ml/input/data/ICDAR17_Korean/ufo/original_train.json'
ANNOTATION_2 = '/opt/ml/input/data/ICDAR17_Korean/ufo/annotation.json'
SAVE_DIR = '/opt/ml/input/data/ICDAR17_Korean/ufo/train.json'


if __name__ == '__main__':
    annotation_1, annotation_2 = read_json(ANNOTATION_1), read_json(ANNOTATION_2)

    new_annotation = {}
    new_annotation['images'] = dict(annotation_1['images'], **annotation_2['images'])

    write_json(new_annotation, SAVE_DIR)
