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
*	<i> ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `Tensorflow Object Detection Api CSV` &gt; 
        ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) `globalFormat` &gt;  
        ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `Tensorflow Object Detection Api CSV`
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

- ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) `#f03c15`
- ![#c5f015](https://via.placeholder.com/15/c5f015/000000?text=+) `#c5f015`
- ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+) `#1589F0`


## Changelog

### v1.0.0
* Yayımlanma : Mart 5, 2021
* CSV import, export
* globalFormat visualizer

Initial release