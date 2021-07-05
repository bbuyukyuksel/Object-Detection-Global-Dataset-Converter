from GlobalConverter.LabelmeJSON import LabelmeJSON
from GlobalConverter.BaseParser import BaseParser

import random
from termcolor import colored
from tabulate import tabulate

def dict_split(headers:list, data:dict, padding:str=None):
    l = []
    for index, key in enumerate(headers):
        if padding != None:
            l.append(padding)
        else:
            l.append(data.get(key, '-'))
    return l

def process(GlobalFormat:dict, train:float, dev:float, iteration:int, history:list, verbose=False):

    test = 1 - (train + dev)
    all_files = list(GlobalFormat.keys())
    
    len_all_files = len(all_files)
    train_count = int(len_all_files * train)
    dev_count = int(len_all_files * dev)
    test_count = len_all_files - (train_count + dev_count)

    train_limit = train_count
    dev_limit = train_limit + dev_count

    for i in range(iteration):
        # Shuffle
        random.Random(i).shuffle(all_files)
        
        # Get Samples
        train_samples = all_files[0:train_limit]
        dev_samples = all_files[train_limit:dev_limit]
        test_samples = all_files[dev_limit:]

        train_set = {x:GlobalFormat[x] for x in train_samples}
        dev_set = {x:GlobalFormat[x] for x in dev_samples}
        test_set = {x:GlobalFormat[x] for x in test_samples}
        if verbose:
            print("Total Sample:\t", len_all_files)
            print("Train Sample:\t", train_count)
            print("Dev   Sample:\t", dev_count)
            print("Test  Sample:\t", test_count)
            print("-"* 50)
        
        all_objects = BaseParser.count_of_classes(GlobalFormat)
        all_classes = list(all_objects.keys())

        
        if verbose: print("Train Set Objects:\t%s" % colored(all_objects, "green"))

        if train_set != []:
            train_set_objects = BaseParser.count_of_classes(train_set)
            if verbose: print("Train Set Objects:\t%s" % colored(train_set_objects, "red"))
            l = dict_split(all_classes, train_set_objects)
            l.insert(0, "Train")
            l.insert(0, i)
            history.append(l)
            
        if dev_set != []:
            dev_set_objects = BaseParser.count_of_classes(dev_set)
            if verbose: print("Dev Set Objects:\t%s" % colored(dev_set_objects, "red"))
            l = dict_split(all_classes, dev_set_objects)
            l.insert(0, "Dev")
            l.insert(0, i)
            history.append(l)

        if test_set != []:
            test_set_objects = BaseParser.count_of_classes(test_set)
            if verbose: print("Test Set Objects:\t%s" % colored(test_set_objects, "red"))
            l = dict_split(all_classes, test_set_objects)
            l.insert(0, "Test")
            l.insert(0, i)
            history.append(l)
        if verbose: print("."* 50)

    headers = ["id", "type"]
    headers.extend(all_classes)

    return train_set, dev_set, test_set, headers

def main(GlobalFormat:dict, train:float, dev:float, iteration:int, log_file:str="records.log", ):

    file = open(log_file, 'w')
    history = []
    headers = process(GlobalFormat, train, dev, iteration, history)[-1]
    print(tabulate(history, headers=headers))
    


if __name__ == '__main__':    
    GlobalFormat = LabelmeJSON.Import(r"D:\03#PERSONAL\Projects\global_dataset_converter\datasets\labelme_json")

    main(GlobalFormat, 0.8, 0.1, 5)