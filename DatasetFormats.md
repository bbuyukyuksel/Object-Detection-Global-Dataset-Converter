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