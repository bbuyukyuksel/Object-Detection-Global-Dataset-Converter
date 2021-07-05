## GlobalFormat

```json
{
    "test1.jpg": {
        "count": {
            "0": 3
        },
        "data": [
            {
                "filename": "test1.jpg",
                "width": 128,
                "height": 128,
                "class": "0",
                "bbox": [
                    "37",
                    "68",
                    "44",
                    "85"
                ]
            },
            {
                "filename": "test1.jpg",
                "width": 128,
                "height": 128,
                "class": "0",
                "bbox": [
                    "32",
                    "16",
                    "49",
                    "58"
                ]
            },
            {
                "filename": "test1.jpg",
                "width": 128,
                "height": 128,
                "class": "0",
                "bbox": [
                    "59",
                    "3",
                    "75",
                    "39"
                ]
            }
        ]
    },
    "test2.jpg": {
        "count": {
            "0": 3
        },
        "data": [
            {
                "filename": "test2.jpg",
                "width": 128,
                "height": 128,
                "class": "0",
                "bbox": [
                    "37",
                    "68",
                    "44",
                    "85"
                ]
            },
            {
                "filename": "test2.jpg",
                "width": 128,
                "height": 128,
                "class": "0",
                "bbox": [
                    "32",
                    "16",
                    "49",
                    "58"
                ]
            },
            {
                "filename": "test2.jpg",
                "width": 128,
                "height": 128,
                "class": "0",
                "bbox": [
                    "59",
                    "3",
                    "75",
                    "39"
                ]
            }
        ]
    }
}
```

```python
annotations["imge1.png"]["data"][0]["filename"]
annotations["imge1.png"]["data"][0]["width"] = 300
annotations["imge1.png"]["data"][0]["height"] 
annotations["imge1.png"]["data"][0]["class"]
annotations["imge1.png"]["data"][0]["bbox"] => [xmin, ymin, xmax, ymax]

annotations["imge1.png"]["data"][1]["filename"]
annotations["imge1.png"]["data"][1]["width"] = 300
annotations["imge1.png"]["data"][1]["height"] 
annotations["imge1.png"]["data"][1]["class"]
annotations["imge1.png"]["data"][1]["bbox"] => [xmin, ymin, xmax, ymax]

annotations["imge.png"]["count"]["class1"] = x adet
annotations["imge.png"]["count"]["class2"] = y adet
```



## yolov4_darknet

```
AlexeyAB commented on Jul 2, 2018
.txt-file for each .jpg-image-file - in the same directory and with the same name, but with .txt-extension, and put to file: object number and object coordinates on this image, for each object in new line: <object-class> <x> <y> <width> <height>

Where:

<object-class> - integer number of object from 0 to (classes-1)
<x> <y> <width> <height> - float values relative to width and height of image, it can be equal from (0.0 to 1.0]
for example: <x> = <absolute_x> / <image_width> or <height> = <absolute_height> / <image_height>
atention: <x> <y> - are center of rectangle (are not top-left corner)
For example for img1.jpg you will be created img1.txt containing:

1 0.716797 0.395833 0.216406 0.147222
0 0.687109 0.379167 0.255469 0.158333
1 0.420312 0.395833 0.140625 0.166667
````
## csv
filename,width,height,class,xmin,ymin,xmax,ymax
000_1OC3DT.jpg,300,300,Mask,6,55,28,80
000_1OC3DT.jpg,300,300,Mask,47,48,67,77
000_1OC3DT.jpg,300,300,Mask,84,46,105,76
000_1OC3DT.jpg,300,300,Mask,112,62,131,82

## kitti
For example for img1.jpg you will be created img1.txt containing:
<classname> <0> <0> <0> <xmin> <ymin> <xmax> <ymax> <0> <0> <0> <0> <0> <0> <0>
Mask 0 0 0 6 55 28 80 0 0 0 0 0 0 0



## LabelmeJSON

```json
{
  "version": "4.5.7",
  "flags": {},
  "shapes": [
    {
      "label": "masked",
      "pointsfi": [
        [
          98.14814814814815,
          58.95061728395061
        ],
        [
          204.320987654321,
          284.876543209877
        ]
      ],
      "group_id": null,
      "shape_type": "rectangle",
      "flags": {}
    }
  ],
  "imagePath": "20210311-000011.jpg",
  "imageData": null,
  "imageHeight": 300,
  "imageWidth": 300
}
```

