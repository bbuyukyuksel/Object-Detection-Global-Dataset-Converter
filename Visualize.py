import glob
from GlobalConverter.Visualizer import Visualizer
import os
import cv2

if __name__ == '__main__':
    _type_ = "yolo4_darknet"
    image_path = r'yolo4_darknet_test'
    dataset_name = "dataset.csv"

    FILTER = ["txt", "csv", "pbtxt"]
    images = filter(lambda x: os.path.basename(x).split('.')[-1] not in FILTER ,glob.glob(os.path.join(image_path, '*')))

    path = None
    if _type_ == "csv":
        path = os.path.join(image_path, dataset_name)
    elif _type_ == "yolo4_darknet":
        path = image_path

    print("Path", path)
    print("Type", _type_)

    myVisualizer = Visualizer(path, _type_)

    colorMap = {
        "0": (0,255,0),
        "1": (0,0,255)
    }

    for i, image_path in enumerate(images):
        print("{:0>5} - {}".format(i+1, image_path))
        myVisualizer.visualize(imagePath=image_path, stime=10, colorMap=colorMap)

    