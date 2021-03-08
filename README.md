# Object Detection Dataset Converter



Versiyon :1.1.0    <br />

Lisans: GPL    <br />

Contributors : Burak Büyükyüksel <br />

<hr />

<img src="https://octodex.github.com/images/baracktocat.jpg" alt="Baracktocat" style="zoom:50%;" />



## Nedir?

Nesne tespiti uygulamalarında destek gören veri setlerinin birbirine dönüşümünü sağlamaktadır.



## Veri Seti Görselleştirme

```python
from GlobalConverter.Visualizer import Visualizer

## Visualize CSV Dataset
Visualizer("datasets/csv/dataset.csv", "csv", "datasets/csv/000_1OC3DT.jpg").visualize()

## Visualize Yolo4Darknet Dataset with Colormap
colorMap = {
    "0": (0,0,255),
    "1": (0,255,0)
}
Visualizer('datasets/yolo4_darknet', "yolo4_darknet", "datasets/yolo4_darknet/test1.jpg").visualize(colorMap=colorMap)
    
```

## Veri Dönüşümü Scriptinin Çalıştırılması



## Veri Dönüşümlerinde Labelmap Uygulanması

*  **CSV :point_right:  CSV** 

  ```sh
  > python Converter.py --inpath datasets\csv\dataset.csv --intype csv ^ 
  					  --outpath mytest.csv --outtype csv ^
  					  --labelmap Mask Maskeli
  ```

  <span style='color:green;'> Labelmap : {'Mask': 'Maskeli'} </span>



* **CSV :point_right: Yolo4Darknet** 

  ```sh
  python Converter.py --inpath datasets\csv\dataset.csv --intype csv ^ 
  					--outpath test_yolo4_darknet --outtype yolo4_darknet ^
  					--labelmap Mask 0 Un-Masked 1
  ```

  <span style='color:green;'> Labelmap : {'Mask': 0, "Un-Masked":1} </span>



## Desteklenen Veri Seti Dönüşümleri;

* <i> `Tensorflow Object Detection Api CSV` &gt; `globalFormat` &gt; `Tensorflow Object Detection Api CSV` </i>

  > Code Example

```python
from GlobalConverter.CSV import CSV
from GlobalConverter.Visualizer import Visualizer

## Import Tensorflow CSV Annotation File as GlobalFormat
globalFormat = CSV.Import("datasets/csv/dataset.csv")

## Export GlobalFormat as Tensorflow CSV Annotation File 
CSV.Export(globalFormat, "test.csv")

## Visualize the image "../datasets/csv/000_1OC3DT.jpg" using globalFormat
Visualizer("datasets/csv/dataset.csv", "csv", "datasets/csv/000_1OC3DT.jpg").visualize()
```

* <i> `Yolo4Darknet` &gt; `globalFormat` &gt; `Yolo4Darknet` </i>

  > Code Example

```python
from GlobalConverter.Yolo4Darknet import Yolo4Darknet
from GlobalConverter.Visualizer import Visualizer

## Import Yolo4Darknet Annotation File as GlobalFormat
globalFormat = Yolo4Darknet.Import("datasets/yolo4_darknet")

## Export GlobalFormat as Yolo4Darknet Annotation File 
Yolo4Darknet.Export(globalFormat, "yolo4_darknet_test")

# Note:
# Please copy images into 'yolo4_darknet_test' folder.
input("Please copy images into 'yolov4_darknet_test' folder...")

## Visualize the image "../datasets/csv/000_1OC3DT.jpg" using globalFormat
Visualizer("yolo4_darknet_test", "yolo4_darknet", "yolo4_darknet_test/test1.jpg").visualize()
```



## Changelog

### v1.1.0

* Yayımlanma : Mart 8, 2021

* Yolo4Darknet import, export
* update globalFormat visualizer

### v1.0.0

* Yayımlanma : Mart 5, 2021

* CSV import, export

* globalFormat visualizer
