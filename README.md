# Object Detection Dataset Converter



Versiyon :1.1.0    <br />

Lisans: GPL    <br />

Contributors : Burak Büyükyüksel <br />

<hr />

<img src="https://octodex.github.com/images/baracktocat.jpg" alt="Baracktocat" style="zoom:50%;" />



## Nedir?

Nesne tespiti uygulamalarında destek gören veri setlerinin birbirine dönüşümünü sağlamaktadır.

------



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

------



## Veri Dönüşümü Scriptinin Çalıştırılması

* **CSV :point_right:  Yolo4Darknet** 

  ```sh
  > python Converter.py --inpath datasets\csv\dataset.csv --intype csv ^ 
  					  --outpath test_yolo4_darknet --outtype yolo4_darknet ^
  					  --labelmap Mask 0 Un-Masked 1
  ```

* **Yolo4Darknet :point_right: CSV** 

  ```sh
  > python Converter.py --inpath datasets\yolo4_darknet --intype yolo4_darknet ^ 
  					  --outpath test_dataset.csv --outtype csv ^
  					  --labelmap 0 Mask 1 Un-Masked
  ```

------



## Veri Seti içerisindeki Sınıf İsimlerini Değiştirme

*  **CSV :point_right:  CSV** 

  ```sh
  python Converter.py --inpath datasets\csv\dataset.csv --intype csv ^ 
  				  --outpath test_dataset.csv --outtype csv ^
  				  --labelmap Mask Maskeli Un-Masked Maskesiz
  ```

  > <span style='color:green;'> Labelmap : {'Mask': 'Maskeli', 'Un-Masked':'Maskesiz'} </span> 
  >
  > Mask->Maskeli , Un-Masked->Maskesiz şeklinde sınıf isimlendirmeleri değişecektir.



* **Yolo4Darknet :point_right: Yolo4Darknet** 

  ```sh
  python Converter.py --inpath datasets\yolo4_dataset --intype yolo4_darknet ^ 
  					--outpath test_yolo4_darknet --outtype yolo4_darknet ^
  					--labelmap 0 1 1 0
  ```

  > <span style='color:green;'> Labelmap : {"0": "1", "1":"0"} </span>
  >
  > 0->1, 1->0 şeklinde sınıf isimlendirmeleri değişecektir.

------



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

#### v1.2.0

* Yayımlanma : Mart 16, 2021
* Yolo4DarknetDatasetRename scripti eklenerek, yolo4_darknet formatındaki veri setinin yeniden isimlendirilmesi gerçekleştirildi.
* Visualize scripti yazılarak, içerisindeki tip ve veri seti yolunun değiştirilmesi ile veri setlerinin kontrol edilmesi sağlanmaktadır.

#### v1.1.0

* Yayımlanma : Mart 8, 2021

* Yolo4Darknet import, export
* globalFormat visualizer yolo4_darknet formatına destek veriyor

#### v1.0.0

* Yayımlanma : Mart 5, 2021

* CSV import, export

* globalFormat visualizer eklendi
