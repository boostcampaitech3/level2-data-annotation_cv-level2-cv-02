#
# boostcamp AI Tech
# Text Image Annotation Competition
#


from json_io import read_json, write_json
from typing import List


ANNOTATION = '/opt/ml/input/data/ICDAR17_Korean/ufo/polygon_train.json'
SAVE_DIR = '/opt/ml/input/data/ICDAR17_Korean/ufo/train.json'


def make_rectangle(points: List[float]) -> List[float]:
    x, y = [], []

    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])

    return [[min(x), min(y)], [max(x), min(y)], [max(x), max(y)], [min(x), max(y)]]


if __name__ == '__main__':
    annotation = read_json(ANNOTATION)

    empty_images = []

    for image in annotation['images']:
        # Bounding box가 없는 이미지의 목록 작성
        if len(annotation['images'][image]['words']) == 0:
            empty_images.append(image)
            continue

        # Points가 6개 이상인 이미지의 annotation 정제
        for word_idx in annotation['images'][image]['words']:
            points = annotation['images'][image]['words'][word_idx]['points']

            assert len(points) % 2 == 0

            if len(points) > 4:
                annotation['images'][image]['words'][word_idx]['points'] = make_rectangle(points)

    # Bounding box가 없는 이미지를 annotation에서 제거
    for image in empty_images:
        del annotation['images'][image]

    write_json(annotation, SAVE_DIR)
