import json
import os
import glob

class BaseParser():
    @classmethod
    def Load(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()[1:]
            lines = list(map(lambda x: x.replace("\n", "").replace("\r", ""), lines))
            lines = list(filter(lambda x: x, lines))
    
    @classmethod
    def LoadJSON(cls, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    @classmethod
    def list_dir(cls, path, except_extension=".json"):
        return filter(lambda x: except_extension not in x, glob.glob(os.path.join(path, "*")))

    @classmethod
    def get_filename(cls, path):
        return ".".join(os.path.basename(path).split('.')[:-1])
    
    @classmethod
    def get_imagename(cls, path):
        filename = cls.get_filename(path)
        list_dir = cls.list_dir(os.path.dirname(path), except_extension=".txt")
        images = tuple(filter(lambda x: filename in x, list_dir))
        
        print("Filename", filename)
        print("Path", path)
        print("List Dir", tuple(list_dir))
        print("Images", images)

        return images[0] if len(images) > 0 else None

    @classmethod
    def count_of_classes(cls, GlobalFormat:dict):
        count = {}
        for obj in GlobalFormat.values():
            _count_ = obj.get("count", None)
            assert _count_ != None, "object has not key: 'class'"

            for _class_ in _count_.keys():
                if _class_ not in count.keys():
                    count[_class_] = 0
                count[_class_] += _count_[_class_] 

        return count
    
    @classmethod
    def Import(cls, ):
        pass

    @classmethod
    def Export(cls, globalFormat:dict, filename:str, labelmap:dict=None, rename:bool=False):
        pass
