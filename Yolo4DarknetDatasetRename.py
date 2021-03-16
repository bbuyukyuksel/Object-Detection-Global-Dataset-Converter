import os
import glob
import shutil

if __name__ == "__main__":
    source_path = 're-dataset-0-yolo4_darknet'
    target_path = 'renamed-dataset-0-yolo4_darknet'
    prefix = "20210311-{:0>6}.{}"


    files = glob.glob(os.path.join(source_path, '*'))

    FILTER = [".csv"]
    files = list(filter(lambda x: x.split(".")[-1] not in FILTER, files))

    images = set(list(filter(lambda x: ".txt" not in x , files)))
    
    os.mkdir(target_path)
    
    for index, file in enumerate(images):
        full_source_path = file
        basename = os.path.basename(file)
        dirname = os.path.dirname(file)

        by_name = ".".join(basename.split(".")[:-1])
        im_type = basename.split(".")[-1]
        annotation_filename = by_name + '.txt'


        print("Full Path", file)
        print("Dirname", dirname)
        print("Annotation File", annotation_filename)
        print("Image      File", basename)
        print('-'*20)

        shutil.copy(file, os.path.join(target_path, prefix.format(index, im_type) ))
        shutil.copy(os.path.join(dirname, annotation_filename), os.path.join(target_path, prefix.format(index, "txt") ))

