# Day 11

## 作業一：安裝 Raspberry PI

問題：觀察 Raspberry PI OS 桌面與純文字版本映像檔案的檔案大小，實際下載之後解壓縮，紀錄實際下載與解壓縮的時間。

至[此處](https://www.raspberrypi.org/downloads/)下載映像檔，插入SD卡後，雙擊映像檔依照指示即可安裝完成。

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day11-1.1.png)

下載後的dmg檔為18 MB

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day11-1.2.png)

安裝後，可用為 264.3 MB，這張SD卡為16GB，因此整個OS占了將近15.8 GB。

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day11-1.3.png)

## 作業二

首次開啟就會設定帳號密碼，事後也可以透過`$ passwd`指令來設定密碼。

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day11-2.1.png)

## 作業三

首次開啟也會引導設定無線網路，可以透過`$ ifconfig`指令搜尋到Raspberry PI 的 ip。

![image5](https://github.com/qaws5503/AIOT/blob/master/pictures/Day11-3.1.png)

## 踩坑

如果使用 VNC 遠端連線 Raspberry PI 時出現Cannot Currently Show the Desktop 的字樣，就代表沒有設定預設要顯示的螢幕尺寸大小。可以透過以下指令設定

```
$ sudo raspi-config
```

進入設定後選擇 Display Options -> Resolution -> change to any selection except default.

