# Day22

## 作業1

問題：請問 YOLO 訓練前，分別要對哪幾個檔案做設定？

由於原本 YOLO 是分析很多的項目，但是我們的 Task 只需要分類 3 個類別，因此分別將以下兩個部分的 `classes=5`更改為`classes=3`，下者也要再更改個類別名稱，`ben_afflek\neltron_john\njerry_seinfeld`

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day22-1.1.png)

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day22-1.2.png)

## 作業2

問題：請問 UNIX 的文字取代工具 sed 在使用時，指定參數 -i 有什麼意義？

sed 實務上經常用到的大致有以下幾種：

* `-n`：沉默模式。
* `-e`：直接在命令模式編輯。(可不加，請見詳解)
* `-f`：程式手稿不直接在命列中打上，而是從指定的檔案中載入。
* `-i`：修改檔案。

一般的指令是只有取代沒有改變原本的文本，使用`-i`則會改變到原本的檔案，因此很適合撰寫自動化程式。

[sed 指令詳細講解](https://terryl.in/zh/linux-sed-command/)

## 作業3

問題：請問 UNIX 的文字編輯工具 echo 在使用時，指定參數 -e 有什麼意義？

`-e`：激活轉義字符。

使用-e選項，若字符串中出現以下字符，則特別加以處理，不會將它當成一般文字輸出。

* `\a` 發出警告聲
* `\b` 刪除前一個字符
* `\c` 最後不加上換行符號
* `\f` 換行但光標仍舊停留在原來的位置
* `\n` 換行且光標移至行首
* `\r` 光標移至行首，但不換行
* `\t` 插入tab
* `\\` 插入\字符

例如：輸入`$ echo -e "hello world\n\thello echo"`  
輸出：

```
hello world

hello echo
```

## 補充

更改 classes 時 filters 看似要遵守 **( 5 + class numbers ) * 3**  
因此這個案例 filters 需要更改為 24

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day22-4.1.png)