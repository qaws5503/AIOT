# Day23 在 Raspberry Pi 上使用 YOLO 已訓練好的模型

## 準備資料

YOLO 模型總共幾個重要的檔案

* obj.names/obj.data 用來設定需要辨識的類別參數
* yolov3_training_last.weights 訓練出來的模型權重
* yolov3_training.cfg 模型架構設定

使用`$ tree`印出我的檔案目錄：

```
yolo
├── darknet
├── obj.data
├── obj.names
├── test.jpg
├── test.py
├── yolov3_training.cfg
└── yolov3_training_last.weights
```

因此首先要將幾個重要的檔案複製進去 YOLO 的模型內

```
$ cd ~/Desktop/yolo
$ sudo cp -f obj.names darknet/data/
$ sudo cp -f obj.data darknet/data/
$ sudo cp -f yolov3_training_last.weights darknet/cfg/
$ sudo cp -f yolov3_training.cfg darknet/cfg/
```

## 推論

### 方法一

直接到 darknet 的位置目錄下執行終端機指令

```
$ cd ~/Desktop/yolo/darknet
$ ./darknet detector test ./data/obj.data ./cfg/yolov3_training.cfg ./cfg/yolov3_training_last.weights ~/Desktop/yolo/test.jpg
```

* `./darknet detector test` 執行推論
* `./data/obj.data` 類別設定檔
* `./cfg/yolov3_training.cfg` 模型架構
* `yolov3_training_last.weights` 模型權重
* `~/Desktop/yolo/test.jpg` 被推論的圖片

### 方法二

使用 python

```python3
import os  # 導入函式庫
import argparse # 導入函式庫
import imghdr # 導入函式庫

if __name__ == "__main__": # 程式碼開頭，用來避免被其他程式呼叫時誤動作
    os.chdir('/home/pi/Desktop/yolo/darknet') # 移動到yolo(darknet)所在的資料夾
    
    parser = argparse.ArgumentParser() # 設定一個參數接收器
    parser.add_argument('img_abs_path') # 在參數接收器裡面增加一個"img_abs_path"參數
    args = parser.parse_args() # 取得參數接收器的實例
    img_path = args.img_abs_path # 從參數接收器裡面，取出接收到的參數
    
    lis = ['jpeg', 'png', 'bnp'] # 檢測是否為圖片
    if imghdr.what(img_path) in lis: # 判斷接收到的參數是否為有效的檔案路徑
        os.system("""./darknet detector test\ # 執行偵測
            ./data/obj.data\
            ./cfg/yolov3_training.cfg\
            ./cfg/yolov3_training_last.weights """\
            +img_path) 
    else: # 如果接收到的參數並非有效的檔案路徑
        print('path error')
```

* `imghdr.what()`取得檔案的副檔名
* `add_argument()`新增參數
* `parse_args()`取得整筆指令

最後執行`python3 test.py "測試檔案路徑"`

### 結果

成功推論為 TUG：

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day23-1.1.png)

## 作業

### 作業一

問題：請問我們要使用 ArgumentParser 的哪一個方法來新增一個參數？

使用 `add_argument("參數")`來新增參數，`parse_args()`來取得整筆指令，再用`.參數`的方式把一個一個參數取出

### 作業二

問題：在使用 YOLO 的推論程序 darknet detector test 時，我們需要指定那些參數？

欲預測圖片的路徑參數