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
*	<i> Kitti Dataset > Tensorflow Object Detection Api CSV </i>
```python
$ python Kitti2Csv.py --folder "datasets/kitti" --output "out/dataset.csv"
```

## Smart Dataset Splitter
* <i> Veri setini dengeli olarak train ve test olarak bölünmesini gerçekleştirir</i>
```python
## SmartSplitter
#**required: dataset.csv
$ python SmartSplitter4CSV.py --trainsplit 0.8 --iteration 200000 --csvfilename "out/dataset.csv" --imagefolderpath "datasets/kitti"

## Export
#**required: register.json
$ python SmartSplitter4CSV.py --csvfilename "out/dataset.csv" --imagefolderpath "datasets/kitti" --export True 
```

## Changelog

### v1.0.0
* Yayımlanma : Şubat 23, 2021
* Kitti > CSV dönüşümü gerçekleşiyor.
* SmartSplitter ile veri seti dengeli olarak `train` ve `test` olarak bölünebiliyor

Initial release