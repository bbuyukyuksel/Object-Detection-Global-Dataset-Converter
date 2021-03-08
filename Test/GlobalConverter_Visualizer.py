import sys
sys.path.append(r"D:\03#PERSONAL\Projects\global_dataset_converter")

from GlobalConverter.Visualizer import Visualizer

if __name__ == '__main__':
    ## Visualize CSV Dataset
    Visualizer("../datasets/csv/dataset.csv", "csv", "../datasets/csv/000_1OC3DT.jpg").visualize()

    ## Visualize Yolo4Darknet Dataset
    Visualizer('../datasets/yolo4_darknet', "yolo4_darknet", "../datasets/yolo4_darknet/test1.jpg").visualize(colorMap={"0":(0,255,0)})
    