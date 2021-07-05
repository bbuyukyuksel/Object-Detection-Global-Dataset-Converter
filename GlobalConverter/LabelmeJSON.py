# System Packages
import datetime
import json
import os
import glob

# Local Packages
try:
    from GlobalConverter.BaseParser import BaseParser
except:
    from BaseParser import BaseParser

# 3rd party packages
from tqdm import tqdm

class LabelmeJSON(BaseParser):
    @classmethod
    def Import(cls, path:str):
        GlobalDataset = {}
        
        for filepath in tqdm(glob.glob(os.path.join(path, "*.json"))):
            count = {}
            content = cls.LoadJSON(filepath)
            filename = content["imagePath"]

            GlobalDataset[filename] = {}
            data = []
            for obj in content["shapes"]:

                x0, y0 = obj["points"][0]
                x1, y1 = obj["points"][1]

                xmin = min(x0, x1)
                ymin = min(y0, y1)

                xmax = max(x0, x1)
                ymax = max(y0, y1)
            
                data.append({
                    "filename": filename,
                    "width": content["imageWidth"],
                    "height": content["imageHeight"],
                    "class": obj["label"],
                    "bbox": [
                        int(xmin),
                        int(ymin),
                        int(xmax),
                        int(ymax),
                    ]}
                )

                # Count of CLASSES
                CLASS = obj["label"] 
                if CLASS not in count.keys():
                    count[CLASS] = 0
                count[CLASS] += 1

            GlobalDataset[filename]["data"] = list(data)
            GlobalDataset[filename]["count"] = dict(count)

        return GlobalDataset

    @classmethod
    def Export(cls, globalFormat:dict, filename:str, labelmap:dict=None, rename:bool=False):
        pass
    

if __name__ == '__main__':
    content = LabelmeJSON.Import(r"D:\03#PERSONAL\Projects\global_dataset_converter\datasets\labelme_json")
