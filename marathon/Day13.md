# Day 13 PI 之接腳介紹與 GPIO

## Raspberry PI 接腳圖

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/RaspberryPI_pin.png "圖片取自 Cupoy 課程")

* PI 共有 40 隻接腳
* 5V PWR：5V 輸出 (2 個)
* 3.3V PWR：3.3V 輸出 (2 個)
* GND：接地端 (有 8 個)
* UARTO TX：序列輸出
* UARTO RX：序列輸入
* GPIO 數字：GPIO 接腳
* Reserved：未使用 (2 個)
* SPI：可切換 GPIO 為 SPI
* I2C：可切換 GPIO 為 I2C

## GPIO指令

```
# 將 GPIO 啟動，可以用 sysfs 控制
$ echo 4 > /sys/class/gpio/export
# 設定 GPIO4 為輸出
$ echo out > /sys/class/gpio/gpio4/direction
# 設定 GPIO4 輸出值為 1 (0：低電位，1：高電位)
$ echo 1 > /sys/class/gpio/gpio4/value
# 設定 GPIO4 輸出值為 0 (0：低電位，1：高電位)
$ echo 0 > /sys/class/gpio/gpio4/value
# 將 GPIO4 卸載，不用 sysfs 控制
$ echo 4 > /sys/class/gpio/unexport
```

上面為操作的指令，如需要觀察 GPIO 各 pin 的狀態要使用下列的指令

```
$ sudo cat /sys/kernel/debug/gpio
```

## 作業一

問題：實際練習 /sys/class/gpio 啟動 gpio，設定 gpio 接腳的狀態，並且卸載所啟動的 gpio。同時觀察卸載之後的 gpio 接腳，繼續送設定狀態的資料，將會發生什麼樣的狀態。

```
$ echo 4 > /sys/class/gpio/export
$ echo out > /sys/class/gpio/gpio4/direction
```

設定完透過`sudo cat /sys/kernel/debug/gpio`觀察 gpio 的狀況

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-1.1.png)

可以看到 gpio-4 被設定為 out lo 了，之後透過`echo 4 > /sys/class/gpio/unexport`將 gpio-4 卸載，再嘗試設定 gpio-4的腳位

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-1.2.png)

此時會報錯沒有檔案，此時

```
$ cd /sys/class/gpio
$ ls -alh
```

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-1.4.png)

確實沒有 gpio4 這個檔案，那我們再讓 sysfs 控制一次 gpio4

![image5](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-1.3.png)

這時就看到 gpio4 的檔案了，所以當執行`echo 4 > /sys/class/gpio/export`就是在創建 gpio4 這個檔案

## 作業二

問題：使用 raspi-config 啟動 i2c，觀察 gpio2 以及 gpio3 的變化，透過 /sys/kernel/debug/gpio 觀察改變的情形，嘗試重新做一次作業1，針對 gpio2 以及 gpio3 操作，觀察在 i2c 啟動的狀態下，gpio2 以及 gpio3 相對 gpio4 有何不同。

先透過`sudo cat /sys/kernel/debug/gpio`觀察腳位

![image6](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-2.1.png)

`sudo raspi-config`進入設定介面

```
Interface Options->I2C->Enable
```

設定後

![image7](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-2.2.png)

分別將 gpio2 和 gpio4 設定為 out hi，看不出有什麼明顯區別

![image8](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-2.3.png)

## 作業三

問題：使用 raspi-config 啟動 spi，觀察 gpio 各接腳的變化狀態，嘗試將 spi 關閉之後，透過 /sys/kernel/debug/gpio，觀察可以使用 gpio 數量的變化情形 。

`sudo raspi-config`進入設定介面

```
Interface Options->SPI->Enable
```

設定後

![image9](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-3.1.png)

看出 gpio7 和 gpio8 已經被佔用了，嘗試去寫入這兩個腳位會報錯

![image10](https://github.com/qaws5503/AIOT/blob/master/pictures/Day13-3.2.png)