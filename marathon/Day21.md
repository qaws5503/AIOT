# Day21 YOLO 目標檢測框架介紹

## 問題

問題：請參考 「 什麼是物件偵測？ 」頁的內容，思考 YOLO 是如何找出貓咪的位置以及類別的。

先將輸入照片切割成N個 S x S 的小方格，再分別做兩件事情：

* 產生 k 個定界框，判斷每個定界框包含物體的可信度
* 計算每個方格是同類別的機率

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day21-1.1.png)