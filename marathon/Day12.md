# Day12 Linux 常用指令教學

## 作業一

問題：使用 raspi-config 更改 root 的密碼，設定連線的無線基地台，開啟 ssh 伺服器，確定可以用遠端連線進入 pi。

```
$ sudo raspi-config
```

```
Interface Options->SSHD
```

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day12-1.1.png)

## 作業二

問題：切換至 /opt 路徑，建立一個 /opt/aiot 子目錄，切換至 /opt/aiot 子目錄，用 wget 指令下載一個網路上的檔案，下載完成後用 ls –al 指令，確定下載的檔案存在。

```
$ cd /opt
$ sudo mkdir aiot
$ cd aiot
$ wget *download link*
```

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day12-2.1.png)

下載後透過`ls -al`可以看到檔案確實下載了

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day12-2.2.png)

也可以透過檔案管理程式查看

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day12-2.3.png)

## 作業三

問題：切換至/根目錄(指令: cd /)，壓縮 /opt 子目錄進行備份，使用 tar zcvf opt.tar.gz /opt，以及 bzip2 opt.tar.gz 壓縮成 bz2 格式，最後將 opt.tar.gz 用 tar zxvf opt.tar.gz 指令練習解壓，或者將 opt.tar.gz 解壓至 /tmp 之下，確定 /opt 子目錄有壓縮備份成功 。

先移動到`/`再將`/opt`整個資料夾壓縮名字為 `opt.tar.gz`的檔案，之後把這個檔案移動到`/tmp`之後解壓縮

```
$ cd /
$ sudo tar zcvf opt.tar.gz /opt
$ sudo mv opt.tar.gz /tmp
$ cd /tmp
$ sudo tar zxvf opt.tar.gz
```

透過`ls -al`可以看到`/opt`已經順利備份到`/tmp`

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day12-3.1.png)

## Linux 指令補充

* pwd：顯示目前的工作路徑
* mkdir piaiot：在目前所在路徑的子目錄，建立 piaiot 子目錄
* cd piaiot：切換至 piaiot 子目錄
* ls -al：顯示目前工作目錄的所有檔案
* cp aiot /tmp：將名稱包含aiot的檔案複製到 /tmp 底下
* chmod 755 *：將目錄內所有檔案權限設定為 +rwxr-xr-x
* rm aiot：將名稱包含 aiot 檔案刪除 (要小心，刪除無法復原)
 * rm -r /aiot 刪除整個資料夾
* uptime：目前系統從開機到現在已經經過多久的時間 (這可以觀察是否 pi 運作的過程中，是否有不穩定重開機的現象)
* top：系統運作的狀態，可以觀察記憶體與 cpu 的使用量s