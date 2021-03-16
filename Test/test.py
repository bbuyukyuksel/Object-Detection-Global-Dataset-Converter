import os
import cv2

if __name__ == '__main__':

    files = os.listdir("re-dataset-0-yolo4_darknet")

    FILTER = [".csv"]
    files = list(filter(lambda x: x.split(".")[-1] not in FILTER, files))

    images = set(list(filter(lambda x: ".txt" not in x , files)))
    annots = set(list(filter(lambda x: ".txt" in x, files)))

    images = set(map(lambda x:  ".".join(x.split(".")[:-1]), images))
    annots = set(map(lambda x:  ".".join(x.split(".")[:-1]), annots))

    print("Count files", len(files))
    print("Count image", len(images))
    print("Count annot", len(annots))
    
    print(images - annots)
    
    