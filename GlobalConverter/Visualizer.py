from GlobalConverter.CSV import CSV
from GlobalConverter.Yolo4Darknet import Yolo4Darknet

import cv2
import os
import random

class Visualizer:

    def __init__(self, annotationFilePath:str, annotationFileFormat:str, imagePath:str=None):
        if imagePath:
            self.imagePath = imagePath
        
        self.annotationFile = annotationFilePath
        self.annotationFileFormat = annotationFileFormat

        if annotationFileFormat == 'csv':
            self.globalFormat = CSV.Import(self.annotationFile) 
        elif annotationFileFormat == 'yolo4_darknet':
            self.globalFormat = Yolo4Darknet.Import(self.annotationFile)

    def visualize(self, imagePath=None, colorMap=None, fontSize=0.5, stime=0):
        
        if imagePath:
            self.imagePath = imagePath
        basename = os.path.basename(self.imagePath)
        Image = cv2.imread(self.imagePath, cv2.IMREAD_UNCHANGED)
        
        if colorMap:
            colormap = colorMap
        else:
            colormap = {x:(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for x in self.globalFormat[basename]["count"].keys()}
        
        for annotation in self.globalFormat[basename]["data"]:
            bbox = list(map(lambda x: int(x), annotation["bbox"]))
            cv2.rectangle(Image, tuple(bbox[:2]), tuple(bbox[2:]), colormap[annotation["class"]], 1)
            cv2.putText(Image, annotation["class"], tuple(bbox[:2]), cv2.FONT_HERSHEY_PLAIN, 1, colormap[annotation["class"]])
        cv2.imshow("Image BBOX", Image)
        cv2.waitKey(stime)


    