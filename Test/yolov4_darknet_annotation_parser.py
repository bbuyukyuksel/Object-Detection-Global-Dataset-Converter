import os
import glob
import cv2

dataset_dir = "datasets/yolov4_darknet"

files = glob.glob(f"{dataset_dir}/*")

annotation_files = tuple(filter(lambda x: ".txt" in x, files))
image_files      = tuple(filter(lambda x: ".txt" not in x, files))

annotation_file = annotation_files[0]


# Get Image File
image_file = tuple(filter(lambda x: x.split(".")[0] in annotation_file, image_files))
assert len(image_file) > 0, Exception("Could not file image file using by annotation filename")
image_file = image_file[0]


with open(annotation_file, 'r') as f:
    annotations = f.readlines()

Image = cv2.imread(image_file)
height, width = Image.shape[:2]
cv2.imshow("Image", Image)


for i, annotation in enumerate(annotations):
    CLASS, X, Y, Width, Height = map(lambda x: float(x), annotation.replace("\n", "").replace("\r", "").split(" "))
    
    X, Width = X*width, Width*width
    Y, Height = Y*height, Height*height
    
    X -= Width /2
    Y -= Height /2

    pt1 = tuple(map(lambda x: int(x),(X, Y)))
    pt2 = tuple(map(lambda x: int(x),(X+Width, Y+Height)))
    cv2.rectangle(Image, pt1, pt2, (255,0,0), 1)

cv2.imshow("Test", Image)

cv2.waitKey(0)