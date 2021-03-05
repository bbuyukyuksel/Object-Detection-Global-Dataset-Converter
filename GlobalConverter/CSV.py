from tqdm import tqdm
import json
class CSV:
    @classmethod
    def Import(cls, filename):

        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            lines = list(map(lambda x: x.replace("\n", "").replace("\r", ""), lines))

        parsed = list(map(lambda x: {
            "filename": x.split(',')[0],
            "width": x.split(',')[1],
            "height": x.split(',')[2],
            "class": x.split(',')[3],
            "bbox": x.split(',')[4:]
        }, lines))

        filenames = cls.get_filenames(parsed)        
        globalFormat = {}
        for filename in tqdm(filenames):
            if filename not in globalFormat.keys():
                globalFormat[filename] = {}
            
            data = list(filter(lambda x: x["filename"] == filename, parsed))
            globalFormat[filename]["count"] = cls.get_class_counts(data)
            globalFormat[filename]["data"] = data
        
        return globalFormat

    @classmethod
    def Export(cls, globalFormat:list, filename:str):
        with open(filename, 'w') as file:
            file.write("filename,width,height,class,xmin,ymin,xmax,ymax\n")
            for fname in tqdm(globalFormat.keys()):
                for obj in globalFormat[fname]["data"]:
                    obj_image_filename = obj["filename"]
                    obj_width = obj["width"]
                    obj_height = obj["height"]
                    obj_class = obj["class"]
                    obj_bbox = obj["bbox"]
                    str_line = f"{obj_image_filename},{obj_width},{obj_height},{obj_class}," + ",".join(obj_bbox) + "\n"                    
                    file.write(str_line )
    
    @classmethod
    def get_filenames(cls, parsed):
        return list(set(map(lambda x: x["filename"], parsed)))

    @classmethod
    def get_classnames(cls, parsed):
        return list(set(map(lambda x: x["class"], parsed)))

    @classmethod
    def get_class_counts(cls, parsed):
        counts = {x:0 for x in cls.get_classnames(parsed)}
        for d in parsed:
            counts[d["class"]] += 1
        return counts

if __name__ == '__main__':
    globalFormat = CSV.Import("../datasets/csv/dataset.csv")
    CSV.Export(globalFormat, "test.csv")

    with open("globalFormat.json", 'w') as f:
        json.dump(globalFormat, f, indent=4)


    '''
    for k in globalFormat.keys():
        print(globalFormat[k]["count"])
        for j in globalFormat[k]["data"]:
            print(j)
        print('\n'*2)
    '''
    
