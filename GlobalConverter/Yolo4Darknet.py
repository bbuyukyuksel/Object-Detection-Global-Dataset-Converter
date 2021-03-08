from tqdm import tqdm
import glob
import cv2
import os
import shutil
import math

class Yolo4Darknet:
    @classmethod
    def Import(cls, path:str):
        files = glob.glob(f"{path}/*")

        annotation_files = tuple(filter(lambda x: ".txt" in x, files))
        image_files      = tuple(filter(lambda x: ".txt" not in x, files))

        globalFormat = {}
        for annotation_file in annotation_files:
            # Get Image File
            image_file = tuple(filter(lambda x: os.path.basename(x).split(".")[0] in annotation_file, image_files))
            assert len(image_file) > 0, Exception("Could not file image file using by annotation filename")
            image_file = image_file[0]
            base_image_filename = os.path.basename(image_file)

            with open(annotation_file, 'r') as f:
                annotations = f.readlines()

            # Read Images
            Image = cv2.imread(image_file)
            ImHeight, ImWidth = Image.shape[:2]
            
            data = []
            count = {}
            for i, annotation in enumerate(annotations):
                CLASS, X, Y, Width, Height = map(lambda x: float(x), annotation.replace("\n", "").replace("\r", "").split(" "))
                CLASS = str(int(CLASS))

                if CLASS not in count.keys():
                    count[CLASS] = 0
                count[CLASS] += 1

                X, Width = X*ImWidth, Width*ImWidth
                Y, Height = Y*ImHeight, Height*ImHeight

                X -= Width /2
                Y -= Height /2

                pt1 = tuple(map(lambda x: int(x),(X, Y)))
                pt2 = tuple(map(lambda x: int(x),(X+Width, Y+Height)))
                cv2.rectangle(Image, pt1, pt2, (255,0,0), 1)
                
                _data_ = {
                    "filename"  : base_image_filename,
                    "width"     : ImHeight,
                    "height"    : ImWidth,
                    "class"     : CLASS,
                    "bbox"      : list(map(lambda x: str(int(x)), (X,Y, X+Width, Y+Height)))
                }
                data.append(_data_)

            globalFormat[base_image_filename] = {
                "count": count,
                "data": data
            }
        return globalFormat
            
    @classmethod
    def Export(cls, globalFormat:dict, path:str, labelmap=None):
        if os.path.exists(path):
            shutil.rmtree(path)
        os.mkdir(path)

        for fname in tqdm(globalFormat.keys()):
            with open(os.path.join(path, fname.split(".")[0] + ".txt"), 'w') as file:
                for obj in globalFormat[fname]["data"]:
                    obj_image_filename = obj["filename"]
                    obj_width = obj["width"]
                    obj_height = obj["height"]
                    obj_class = labelmap[obj["class"]] if labelmap else obj["class"]
                    obj_bbox = tuple(map(lambda x: float(x), obj["bbox"]))

                    #CLASS, X, Y, Width, Height
                    X, Y, Width, Height = obj_bbox[0], obj_bbox[1], obj_bbox[2] - obj_bbox[0], obj_bbox[3] - obj_bbox[1]
                    X, Y, Width, Height = X/float(obj["width"]), Y/float(obj["height"]), Width/float(obj["width"]), Height/float(obj["height"])

                    X += Width / 2
                    Y += Height/2

                    X,Y,Width,Height = tuple(map(lambda x: round(x,6), (X,Y,Width, Height)))

                    str_line = f"{obj_class} {X} {Y} {Width} {Height}\n"
                    file.write(str_line)

if __name__ == '__main__':
    globalFormat = Yolo4Darknet.Import('../datasets/yolov4_darknet')
    Yolo4Darknet.Export(globalFormat, "yolo4_test")    



