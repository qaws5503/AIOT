# Project

## 訓練 yolo ( by colab)

如有 .ipynb 檔案，則存入 google drive 後，右鍵 -> 選擇開啟工具 -> Google Colaboratory。

先執行匯入 google drive 的指令

```
from google.colab import drive
```

下載訓練需要的檔案

* cfg：設定檔案
	* obj.names：輸出結果有哪些
	* train.txt：欲訓練的資料
* data：訓練檔案
* tiny_weights：模型結果

### 安裝 yolo

到 git 上抓取 yolov4

```
%cd /content/drive/MyDrive/yolov3
!git clone https://github.com/AlexeyAB/darknet.git
```

更改設定檔開啟 GPU、OpenCV、CUDNN

```
%cd /content/drive/MyDrive/yolov3/darknet
!sed -ie "s/GPU=0/GPU=1/g" Makefile
!sed -ie "s/CUDNN=0/CUDNN=1/g" Makefile
!sed -ie "s/OPENCV=0/OPENCV=1/g" Makefile
```

最後用 make，完成安裝

```
!make
```

### 修改 yolo 設定

#### 設定 yolov3-tiny.cfg

* Line 3：set batch=24 → 每一次訓練使用 24 張影像
* Line 4：set subdivisions=8 → 24 張影像分成 8 次訓練
* Line 127：set filters=(classes + 5)\*3 → 有 3 個類別，filters=(3+5)\*3=24
* Line 135：set classes=3 → 辨識共有3個類別
* Line 171：set filters=(classes + 5)\*3 → 有 3 個類別，filters=(3+5)\*3=24
* Line 177： set classes=3 → 辨識共有 3 個類別

### 補充知識

#### sed 取代文字

```
sed -i 's/a/b/flags' file

# if want slash in replace words
sed -i 's=a=b=flags' file
```

* -i：修改檔案
* s：取代
* a：欲被取代的文字
* b：取代後的文字
* flags
	* [0-9]：數字表示只搜尋或者取代第 N 個數字
	* g：全部取代（常用）
	* I：忽略大小寫
	* w：把符合的結果寫入檔案。
* file：要取代文字的檔案

#### chmod 更改權限

```
chmod 755 darknet
```

755 三個數字解釋為

* 所有者的權限
* 使用者群組的權限
* 其它使用者的權限

數字代表的意義可以去[維基百科](https://zh.wikipedia.org/wiki/Chmod)查詢

## 架設 pi 的 yolo 環境

首先先開啟權限

```
$ su root
```

### 安裝 yolov4

```
$ git clone https://github.com/AlexeyAB/darknet.git
```

進入資料夾內修改 Makeflie 的以下參數

```
LIBSO=1
OPECV=1
```

由於要使用到 opencv 的函式庫，因此在 make 前要先安裝好 opencv

```
$ apt install libopencv-dev
$ apt install python-opencv
$ pip3 install opencv-python
```

```
$ make
```

### 預載 yolo 模型

到 [goole drive](https://drive.google.com/file/d/1aCitXYb_GVJ2LcKyfPsy6vgCpGZ_i8qC/view?usp=sharing) 上面下載已訓練好的模型，並且放在 `/opt`  
之後修改 `/mask_50/cfg/obj.data` 將裡面的路徑更改為 pi 上的路徑

### 安裝 yolo 的坑

有時會出現 `ImportError: libjasper.so.1: cannot open shared object file: No such file or directory` 等等的錯誤碼，此原因是因為我們使用 opencv 版本的 yolo。  
解決方法：

```
$ pip3 install opencv-python
$ sudo apt-get install libatlas-base-dev
$ sudo apt-get install libjasper-dev
$ sudo apt-get install libqtgui4
$ sudo apt-get install python3-pyqt5
$ sudo apt-get install libqt4-test
```

### 測試 yolo

```
$ cd darknet
$ python3 darknet_images.py \--weights /opt/mask_50/tiny_weights/yolov3-tiny_88000.weights \--config_file /opt/mask_50/cfg/yolov3-tiny.cfg \--data /opt/mask_50/cfg/obj.data \--input /opt/mask_50/data/A001.jpg \--ext_output --dont_show
```

觀察可以發現不會有輸出影像，可以透過更改 darknet_image.py 最底下的程式碼

![darknet](darknet_image.png)

## 在 pi 上架設 Flask API

```python3
@app.route('/postLabel', methods=['POST'])
def postLabel():
    content = request.json
    list.append(content)
    print ("postLabel execute", datetime.now(), content)
    return "ok"
    
@app.route('/list', methods=['GET'])
def lists():
    print ("list:", json.dumps(list))
    return json.dumps(list)

@app.route('/clear', methods=['GET'])
def clear():
    print ("clear:")
    list.clear()
    return "clear"
    
@app.route('/clearImg', methods=['GET'])
def clearImg():
    print ("clearImg:")
    files = glob.glob('/opt/webcam_mask_flask/*.jpg')
    for f in files:
        print ("rm ",f)
        os.remove(f)
    return "clear"
    
@app.route("/img", methods=['GET'])
def img():
    filename = request.args.get("file")
    print ("filename:", filename)
    return send_file(filename, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000,
       debug = False, threaded = True)
```

mask_flask.py 有 5 個 REST API：

* /postLabel -> 接受 pi 辨識的結果。
* /list -> 回傳目前 postLabel 上傳在 pi 上的辨識結果資料。
* /clear -> 將 pi 上面儲存的辨識結果資料清空。
* /clearImg -> 將 pi 上面儲存的辨識影像資料清空。
* /img -> 依據傳入的 file 參數，回傳某個影像資料。

透過這 5 個 API，pi 即可作為一個提供外部存取的伺服器架構，/postLabel 主要給 pi 的辨識程式上傳資料，其他的 4 個API提供給後端的伺服器作為資料服務使用。

### 確認 ip

```
$ ifconfig -a
```

* eth0：有線網路
* wlan0：無線網路

![ifconfig](ifconfig.png)

### 設定 DNS

In linux

```
$ sudo nano /etc/hosts
```

[教學文章](https://blog.gtwang.org/windows/windows-linux-hosts-file-configuration/)

### 結果

在同網域下打入 http://192.168.2.201:5000/list 會看到空白的 list 代表 API 有連接成功

![API](API_result)

## 辨識程式

透過 OpenCV DNN 方式即時辨識是否戴口罩，將辨識結果傳輸至 PI 本身的flask接收辨識口罩 API，進行前端即時口罩辨識。

使用 webcam_mask.py

* load_yolo(): 載入模型
* start_webcam(): 啟動 webcam 攝影機
* detect_objects(): 將影像輸入神經網路進行預測
* get_box_dimensions() 將預測機率值超過設定的信賴值的區域取出來。
	* w: 辨識區域的寬度
	* h: 辨識區域的高度
	* X: 辨識區域左上角橫座標
	* y: 辨識區域左上角直座標
	* [w,h,x,y] 加入 boxes 陣列
	* conf: 設定顯示物體的閾值
* webcam_detect(): 啟動攝影機，開始讀取影像、偵測物體、取得物件預測結果的區域、將預測類別標籤畫在影像上，進入無窮迴圈的狀態，直到程式執行結束為止。

```
def webcam_detect():
	model, classes, colors, output_layers = load_yolo()
	cap = start_webcam()
	
	while True:
		_, frame = cap.read()
		height, width, channels = frame.shape
		blob, outputs = detect_objects(frame, model, output_layers)
		boxes, confs, class_ids = get_box_dimensions(outputs, height, width)
		draw_labels(boxes, confs, colors, class_ids, classes, frame)
		cv2.imshow('frame',frame)
		key = cv2.waitKey(1)
		if key == 27:
			break
	cap.release()
```

* cv2.waitkey(t): 代表等待 t 秒後關閉，如 t=0 則為永不關閉
* key = 27 代表在 cv2.waitkey 期間按下 esc

### 執行辨識程式

執行 webcam_mask.py 前要先安裝一些必要安裝包

```
$ apt update
$ apt install python3-opencv
$ pip3 install opencv-python
$ apt install libatlas-base-dev
$ apt install libcblas-dev
$ apt install libhdf5-dev
```

之後開啟在 pi 上開啟兩個終端機一個執行 mask\_flask.py 另一個執行 webcam_mask.py

### 將結果儲存到資料庫內

資料庫使用 Mongodb，建構可以參考 [Day07](https://github.com/qaws5503/AIOT/blob/master/marathon/Day07.md) 和 [Day08](https://github.com/qaws5503/AIOT/blob/master/marathon/Day08.md)

開啟 mongodb

```
$ sudo mongod --dbpath ~/data/db
```