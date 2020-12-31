# Day24 在樹莓派上布署與使用 YOLOv3-tiny

## 建置

和昨天的建置大多相同，只是將 4 個重要的檔案置換成 tiny-yolo 的。所以我先在 yolo 目錄底下創建一個 tiny-yolo 目錄來放置檔案

```
yolo
├── darknet
├── tiny-yolo
│	├── obj.data
│	├── obj.names
│	├── test.jpg
│	├── yolov3_training.cfg
│	└── yolov3_training_last.weights
├── obj.data
├── obj.names
├── test.jpg
├── test.py
├── yolov3_training.cfg
└── yolov3_training_last.weights
```

將檔案複製到 YOLO 內

```
$ cd ~/Desktop/yolo
$ sudo cp -f tiny-yolo/obj.names darknet/data/
$ sudo cp -f tiny-yolo/obj.data darknet/data/
$ sudo cp -f tiny-yolo/yolov3_training_last.weights darknet/cfg/
$ sudo cp -f tiny-yolo/yolov3_training.cfg darknet/cfg/
```

## 推論

執行`python3 test.py "檔案位置"`

### 結果

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day24-1.1.png)

## 作業

### 作業1

問題：請思考使用 YOLO 和 tinyYOLO 進行訓練時，他們之間需要調整的差異在哪裡？

都要修改 classes 和 filters，唯一不同就是要修改的指定列數不相同

### 作業2

問題：請思考當我們要訓練一個 7 個 class 的 tiny_yolo 時，要如何設定 cfg 檔？

* `classes=7`
* `filters=36` filter 計算公式：( 5 + classes number) * 3

```
!cp -f cfg/yolov3-tiny.cfg cfg/yolov3_training.cfg

!sed -i 's/batch=1/batch=64/' cfg/yolov3_training.cfg
!sed -i 's/subdivisions=1/subdivisions=16/' cfg/yolov3_training.cfg
!sed -i 's/max_batches = 500200/max_batches = 4000/' cfg/yolov3_training.cfg
!sed -i '135 s@classes=80@classes=7@' cfg/yolov3_training.cfg
!sed -i '177 s@classes=80@classes=7@' cfg/yolov3_training.cfg
!sed -i '127 s@filters=255@filters=36@' cfg/yolov3_training.cfg
!sed -i '171 s@filters=255@filters=36@' cfg/yolov3_training.cfg
```