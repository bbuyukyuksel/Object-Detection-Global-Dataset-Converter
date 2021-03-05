# Dataset Converter & Smart Dataset Splitter

**Versiyon	:**  1.0 		<br />
**Lisans  	:**  GPL 		<br />
**Contributors  :**  Burak Büyükyüksel	<br />

<hr />

## Nedir?

Nesne tespiti uygulamalarında destek gören veri setlerinin birbirine dönüşümünü sağlamaktadır.

### Not
* 	Bu repoda, veri seti dönüşüm scriptleri ve veri setini akıllı (dengeli, balance) bölmek için kullanılabilecek SmartSplitter scripti bulunmaktadır.


## Desteklenen Veri Seti Dönüşümleri;
*	<i> `Tensorflow Object Detection Api CSV` &gt; 
        `globalFormat` &gt;  
        `Tensorflow Object Detection Api CSV`
    </i>


```python
from GlobalConverter.CSV import CSV
from GlobalConverter.Visualizer import Visualizer

## Import Tensorflow CSV Annotation File as GlobalFormat
globalFormat = CSV.Import("../datasets/csv/dataset.csv")

## Export GlobalFormat as Tensorflow CSV Annotation File 
CSV.Export(globalFormat, "test.csv")

## Visualize the image "../datasets/csv/000_1OC3DT.jpg" using globalFormat
Visualizer("test.csv", "csv", "../datasets/csv/000_1OC3DT.jpg").visualize()
```

## Changelog

### v1.0.0
* Yayımlanma : Mart 5, 2021
* CSV import, export
* globalFormat visualizer

Initial release