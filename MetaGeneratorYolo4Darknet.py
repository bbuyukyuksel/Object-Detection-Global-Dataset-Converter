import os
import shutil

def create_obj_data(path, classes):
    lines = [
            f'classes = {classes+1}\n',
            'train = data/train.txt\n',
            'valid = data/valid.txt\n',
            'names = data/obj.names\n',
            'backup = backup/\n',
    ]
    with open(os.path.join(path, 'obj.data'), 'w') as f:   
        f.writelines(lines)
        

def create_obj_names(path, labels):
    
    with open(os.path.join(path, 'obj.names'), 'w') as f:   
        for i in labels:
            f.write(i + '\n')
        
    
def create_txt(path, source_path, filename):
    with open(os.path.join(path, f"{filename}.txt"), 'w') as f:
        for file in filter(lambda x: ".txt" not in x, os.listdir(source_path)):
            f.write(f"data/obj/{file}" + '\n')

if __name__ == '__main__':
    folder = 'MetaYolo4Darknet'
    train_path = r'yolo4_darknet_train'
    test_path = r'yolo4_darknet_test'
    labels = [
        "Mask",
        "No-Mask",
    ]

    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.mkdir(folder)

    create_obj_data(folder, classes=2)
    create_obj_names(folder, labels=labels)

    create_txt(folder, train_path, 'train')
    create_txt(folder, test_path, 'test')

    
