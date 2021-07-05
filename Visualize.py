import glob
from GlobalConverter.Visualizer import Visualizer
import os
import cv2

if __name__ == '__main__':
    dataset_name = "dataset.csv"
    
    
    _type_ = "labelme_json"
    image_path = r"D:\03#PERSONAL\Projects\global_dataset_converter\datasets\labelme_json"

    FILTER = ["txt", "csv", "pbtxt", "json"]
    images = filter(lambda x: os.path.basename(x).split('.')[-1] not in FILTER ,glob.glob(os.path.join(image_path, '*')))

    path = None
    if _type_ == "csv":
        path = os.path.join(image_path, dataset_name)
    elif _type_ == "yolo4_darknet":
        path = image_path
    elif _type_ == "labelme_json":
        path = image_path

    print("Path", path)
    print("Type", _type_)

    myVisualizer = Visualizer(path, _type_)

    colorMap = {
        "masked": (0,255,0),
        "unmasked": (0,0,255),
        "person": (255,255,0),
    }

    for i, image_path in enumerate(images):
        print("{:0>5} - {}".format(i+1, image_path))
        myVisualizer.visualize(imagePath=image_path, stime=0, colorMap=colorMap)

     