import argparse
import termcolor

from GlobalConverter.Yolo4Darknet import Yolo4Darknet
from GlobalConverter.CSV import CSV


def main(inpath, intype, outpath, outtype, labelmap=None, rename:bool=None):
    globalFormat = None
    if intype == 'csv':
        globalFormat = CSV.Import(inpath)
    elif intype == 'yolo4_darknet':
        globalFormat = Yolo4Darknet.Import(inpath)
    else:
        raise Exception("Unknown input type")

    assert globalFormat != None

    if outtype == 'csv':
        CSV.Export(globalFormat, outpath, labelmap=labelmap, rename=rename)
    elif outtype == 'yolo4_darknet':
        Yolo4Darknet.Export(globalFormat, outpath, labelmap=labelmap)
    else:
        raise Exception("Unknown input type")
    


if __name__ == '__main__':
    doc = '''
        - CSV:
            must be full path of xxx.csv.

        - Yolo4Darknet
            must be folder of annotation files.
    '''
    ap = argparse.ArgumentParser(usage=doc)
    ap.add_argument("--inpath", required=True,  help="In Path")
    ap.add_argument("--intype", required=True,  help="In Path")
    ap.add_argument("--outpath",required=True,  help="In Path")
    ap.add_argument("--outtype",required=True,  help="In Path")
    ap.add_argument("--rename",required=False, type=bool, help="In Path")
    ap.add_argument("--labelmap", required=False, nargs="+",)

    args = ap.parse_args()
    
    print("Input  path: ", termcolor.colored(args.inpath, 'blue') )
    print("Output path: ", termcolor.colored(args.outpath, 'blue'))
    print("Type Converting from {} into {}".format(termcolor.colored(args.intype, 'yellow'), termcolor.colored(args.outtype, 'green')))


    if args.labelmap:
        labelmap = {}
        assert len(args.labelmap) % 2 == 0
        for i in range(0, len(args.labelmap), 2):
            labelmap[args.labelmap[i]] = args.labelmap[i+1]
        termcolor.cprint(f'Labelmap : {labelmap}', 'green')
    else:
        labelmap = None

    main(args.inpath, args.intype, args.outpath, args.outtype, labelmap=labelmap, rename=args.rename)
    
    
