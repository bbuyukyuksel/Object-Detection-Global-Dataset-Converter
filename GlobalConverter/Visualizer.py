from GlobalConverter.CSV import CSV

import cv2
import os
import random

class Visualizer:

    def __init__(self, annotationFile:str, annotationFileFormat:str, imagePath:str):
        self.imagePath = imagePath
        self.annotationFile = annotationFile
        self.annotationFileFormat = annotationFileFormat

        self.globalFormat = CSV.Import(self.annotationFile) 
    
    def visualize(self, colorMap=None, fontSize=0.5):
        basename = os.path.basename(self.imagePath)
        
        Image = cv2.imread(self.imagePath, cv2.IMREAD_UNCHANGED)
        
        if colorMap:
            colormap = colorMap
        else:
            colormap = {x:(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for x in self.globalFormat[basename]["count"].keys()}
        
        for annotation in self.globalFormat[basename]["data"]:
            bbox = list(map(lambda x: int(x), annotation["bbox"]))
            cv2.rectangle(Image, tuple(bbox[:2]), tuple(bbox[2:]), colormap[annotation["class"]], 1)
            cv2.putText(Image, annotation["class"], tuple(bbox[:2]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colormap[annotation["class"]])
        cv2.imshow("Image BBOX", Image)
        cv2.waitKey(0)


if __name__ == '__main__':
    #TEST
    Visualizer("test.csv", "csv", "../datasets/csv/000_1OC3DT.jpg").visualize()#.visualize(colorMap={"Mask":(0,255,0),"No-Mask":(0,0,255)})
