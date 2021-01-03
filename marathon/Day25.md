# Day25 使用 YOLO 訓練如何辨識橘子

## macOS 安裝 labellmg

```
$ pip install pyqt5 lxml
$ pip install labelImg
```

安裝完後直接輸入`$ labelImg`

以下有其他的安裝文章

* [windows](https://tzutalin.github.io/labelImg/)
* [macOS](https://github.com/tzutalin/labelImg)
* [一分鐘搞定 Mac 安裝labelImg](https://www.itread01.com/content/1546283899.html)

## labelImg 使用教學

### 準備圖片和類別

如果想要載入自己定義的 classes 和圖片，只需要在指令後面分別增加圖片和 predefined_classes.txt 的位置參數，圖片的資料夾記得更改為 image

```
$ labelImg [IMAGE_PATH] [PRE-DEFINED CLASS FILE]
```

predefined_classes.txt 的格式為：

```
class 1
class 2
...
class N
```

### 標記前設定

標記之前先在將 labelImg 設定好：

1. File 確認自己現在是否為自己要訓練的模型

	![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day25-1.1.png)

2. View 開啟 Auto Saving
3. 左側工具列改變存放目錄，改到和圖片相同位置

	![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day25-1.2.png)

### 標記

1. 按快捷鍵 Ｗ 或是 Edit 裡面的創建區塊
2. 框出物體的位置
3. 選擇 predefined_classes.txt 裡定義好 classes
	
	![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day25-1.3.png)
	
4. 按下save，就會出現該圖片的標記資料了
	
	![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day25-1.4.png)

5. 重覆 1~4 的步驟標記完所有圖片後，**刪除 classes.txt 檔案**

將資料都標記完後，即可把 image 資料夾壓縮成 image.zip，就可以把資料丟進去 YOLO 訓練囉！