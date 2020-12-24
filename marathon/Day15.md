# Day15 使用 Python 進行 WebCam 視訊擷取與輸出

## 作業一

問題：執行 lsusb -v 指令，觀察系統顯示的 usb 裝置，透過 grep “14 Video” 指令篩選顯示的結果，了解 webcam 裝置在系統層次支援的狀態。

**目前必須透過以下指令安裝 v4l2**，如直接使用`$ sudo apt v4l2`則 import 的時候會報錯

```
$ git clone https://github.com/antmicro/python3-v4l2
$ cd python3-v4l2
$ sudo python3 setup.py install
```

開啟 python 來測試是否安裝成功

```python3
>>> import v4l2
>>> import fcntl
>>> vd = open('/dev/video0', 'r')
>>> cp = v4l2.v4l2_capability()
>>> fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)
0
>>> cp.driver
'uvcvideo'
>>> cp.card
'USB 2.0 Camera'
```

透過以下指令看 webcam 是否有支援 UVC

```
sudo lsusb -v | grep '14 Video'
```

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day15-1.1.png)

如圖，有支援的話會顯示：

* bFunctionClass 14 Video
* bInterfaceClass 14 Video

## 作業二

問題：安裝 fswebcam，執行 fswebcam 拍一張照片，確定 webcam 動作正常，並且透過更改參數與設定參數檔案的方式，執行 fswebcam，確定可以產生隨時間依序儲存的檔案。

安裝 fswebcam

```
sudo apt install fswebcam
```

最簡單的拍攝，沒有指定參數

```
sudo fswebcam image.jpg
```

ls 指令可以看到出現一個 image.jpg 的檔案

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day15-2.1.png)

除了上述的指令外，也可以指定一些特定參數，例如：解析度、跳過幾張、使用的裝置、儲存檔名 等等

```
sudo fswebcam -r 640x360 -S 10 -d /dev/video1 webcam.jpg
```

也可以透過`$ fswebcam -c fs.conf`指令執行先寫好的設定檔

fs.conf 內輸入：

```
device /dev/video1
loop 2 
skip 10
timestamp "%d-%m-%Y %H:%M:%S (%Z)"
title "AIOT-Demo"
save ~/Desktop/webcam/%H-%M-%S-viewcam.jpg
```

fs.conf 的詳細參數可以查閱[這裡](http://manpages.ubuntu.com/manpages/bionic/man1/fswebcam.1.html)

ls 指令可以看出確實以每2秒的週期拍攝一張照片

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day15-2.2.png)

## 作業三

問題：透過 python 呼叫 fswebcam，觀察 python 呼叫 fswebcam 執行外部參數的方式，並且練習更改 fswebcam 的參數檔案，不更動 python 程式碼的方式，儲存各種類型的拍照結果。

```python3
import time
import os
while True:
	os.system('fswebcam -d /dev/video1 -r 320x240 -S 3 --jpeg 50 \
	--save /home/pi/Desktop/webcam/webcam_python1_%H%M%S.jpg')
	time.sleep(2)

```
