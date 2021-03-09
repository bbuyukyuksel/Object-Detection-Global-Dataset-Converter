import glob
from GlobalConverter.Visualizer import Visualizer
import os

if __name__ == '__main__':
    image_path = r'D:\02#OTOKAR\Projects\UT2001#Maske-Tespiti\total\images'
    dataset_name = "dataset.csv"

    FILTER = ["txt", "csv", "pbtxt"]
    images = filter(lambda x: os.path.basename(x).split('.')[1] not in FILTER ,glob.glob(os.path.join(image_path, '*')))

    print(os.path.join(image_path, dataset_name))


    myVisualizer = Visualizer(os.path.join(image_path, dataset_name), "csv")

    colorMap = {
        "Mask": (0,255,0),
        "No-Mask": (0,0,255)
    }
    for i, image_path in enumerate(images):
        print("{:0>5} - {}".format(i+1, image_path))
        myVisualizer.visualize(imagePath=image_path, stime=100, colorMap=colorMap)
    
    ## Visualize CSV Dataset
    #Visualizer("../datasets/csv/dataset.csv", "csv", "../datasets/csv/000_1OC3DT.jpg").visualize()

    ## Visualize Yolo4Darknet Dataset
    #Visualizer('../datasets/yolo4_darknet', "yolo4_darknet", "../datasets/yolo4_darknet/test1.jpg").visualize(colorMap={"0":(0,255,0)})
    