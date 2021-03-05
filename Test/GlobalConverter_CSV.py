import sys
sys.path.append(r"D:\03#PERSONAL\Projects\global_dataset_converter")

from GlobalConverter.CSV import CSV
from GlobalConverter.Visualizer import Visualizer

if __name__ == '__main__':

    ## Import Tensorflow CSV Annotation File as GlobalFormat
    globalFormat = CSV.Import("../datasets/csv/dataset.csv")

    ## Export GlobalFormat as Tensorflow CSV Annotation File 
    CSV.Export(globalFormat, "test.csv")

    ## Visualize the image "../datasets/csv/000_1OC3DT.jpg" using globalFormat
    Visualizer("test.csv", "csv", "../datasets/csv/000_1OC3DT.jpg").visualize()

