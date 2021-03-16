from tqdm import tqdm
import shutil
import glob
import os
if __name__ == '__main__':
    # SET PREFIX
    PREFIX = "20210311-081751-{}"
    
    # Original Images Path
    SOURCE = r"datasets\III_yolo4_darknet"
    
    # Copy into..
    DESTINATION = r"III-re-dataset"

    for file in tqdm(glob.glob(os.path.join(SOURCE, '*'))):
        dest_filename = PREFIX.format(os.path.basename(file))
        filename = os.path.join(DESTINATION, dest_filename)
        shutil.copy(file, filename)
