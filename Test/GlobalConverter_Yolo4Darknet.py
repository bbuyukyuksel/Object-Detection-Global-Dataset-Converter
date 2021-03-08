import sys
sys.path.append(r"D:\03#PERSONAL\Projects\global_dataset_converter")

from GlobalConverter.Yolo4Darknet import Yolo4Darknet
from GlobalConverter.Visualizer import Visualizer

if __name__ == '__main__':

    ## Import Yolo4Darknet Annotation File as GlobalFormat
    globalFormat = Yolo4Darknet.Import("../datasets/yolo4_darknet")

    ## Export GlobalFormat as Yolo4Darknet Annotation File 
    Yolo4Darknet.Export(globalFormat, "yolo4_darknet_test")


    # Note:
    # Please copy images into 'yolo4_darknet_test' folder.
    input("Please copy images into 'yolov4_darknet_test' folder...")
    
    ## Visualize the image "../datasets/csv/000_1OC3DT.jpg" using globalFormat
    Visualizer("yolo4_darknet_test", "yolo4_darknet", "yolo4_darknet_test/test1.jpg").visualize()

