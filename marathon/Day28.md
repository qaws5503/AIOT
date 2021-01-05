# Day28 設計一個影像與辨識結果的資料庫

## 開啟資料庫

```
$ sudo mongo --dbpath ~/data/db
```

`~/data/db`為設置 db 的位置

## 上傳圖片到資料庫

upload_image.py：

```python3
from pymongo import MongoClient  
import base64

client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['test_db']
coll = db['Collections']
img_name = "waves.jpg"

# 讀取圖片，轉成二進制
with open(img_name, "rb") as f: # rb為用二進制打開一個文件用於唯讀
    strpic = base64.b64encode(f.read()).decode('utf-8') # 將讀取到的圖片編碼成二進制檔
    mydata = {'jpg_base64': strpic}
    result = coll.insert_one(mydata)
    print(result.inserted_id)

# 將圖片的檔名、以及在DB中對應的id儲存下來
with open("imageList.txt", "a+") as file: # a+打開一個文件用於讀寫 文件存在則文件指針在文件結尾 如不存在則創建
    old = file.read()
    file.seek(0) # 將指針移到開頭
    content = '%\n'+img_name+'\n'+str(result.inserted_id)
    file.write(content+"\n" + old)
```

用 Robo 3T 確認檔案存進資料庫內：

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day28-1.1.png)

imageList.txt 內儲存的內容：

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day28-1.2.png)

第一行為檔案名稱，第二行為資料庫內的 id

## 下載圖片到資料庫

先安裝以下必要的函式庫

```
$ conda install -c conda-forge matplotlib
$ conda install -c anaconda pillow
```

load_image.py：

```python3
import base64
from PIL import Image
from io import BytesIO
from pymongo import MongoClient  
import matplotlib.pyplot as plt

client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['test_db']
coll = db['Collections']

img_name = 'waves.jpg'
_id = []
with open("imageList.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if img_name in lines[i]:
        # 注意: 讀取到的每一列其實後面會有看不到的’\n’
            a = lines[i+1].split('\n') # 把\n跟內容隔開
            _id.append(a[0])
# print(_id[0])

# 尋找指定ID的圖片
img_base64 = []
for i in coll.find():
    if str(i['_id']) == _id[0]:
        img_base64.append(i['jpg_base64'])

im = Image.open(BytesIO(base64.b64decode(img_base64[0])))
im.save('mongoDB_image.jpg', 'JPEG')
```

檔案被下載下來名為：`mongoDB_image.jpg`

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day28-1.3.png)

## 問題

問題1：請問使用 open 方法後，指定"rb"是什麼意思？  
開啟一個唯讀檔，open 的其他參數如下：

* `t` 文本模式(默認)。
* `x` 寫模式，新建一個文件，如果該文件已存在則會報錯。
* `b` 二進制模式。
* `+` 打開一個文件進行更新(可讀可寫)。
* `U` 通用換行模式（不推薦）。
* `r` 以只讀方式打開文件。文件的指針將會放在文件的開頭。這是默認模式。
* `rb` 以二進制格式打開一個文件用於只讀。文件指針將會放在文件的開頭。這是默認模式。一般用於非文本文件如圖片等。
* `r+` 打開一個文件用於讀寫。文件指針將會放在文件的開頭。
* `rb+` 以二進制格式打開一個文件用於讀寫。文件指針將會放在文件的開頭。一般用於非文本文件如圖片等。
* `w` 打開一個文件只用於寫入。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。
* `wb` 以二進制格式打開一個文件只用於寫入。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。一般用於非文本文件如圖片等。
* `w+` 打開一個文件用於讀寫。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。
* `wb+` 以二進制格式打開一個文件用於讀寫。如果該文件已存在則打開文件，並從開頭開始編輯，即原有內容會被刪除。如果該文件不存在，創建新文件。一般用於非文本文件如圖片等。
* `a` 打開一個文件用於追加。如果該文件已存在，文件指針將會放在文件的結尾。也就是說，新的內容將會被寫入到已有內容之後。如果該文件不存在，創建新文件進行寫入。
* `ab` 以二進制格式打開一個文件用於追加。如果該文件已存在，文件指針將會放在文件的結尾。也就是說，新的內容將會被寫入到已有內容之後。如果該文件不存在，創建新文件進行寫入。
* `a+` 打開一個文件用於讀寫。如果該文件已存在，文件指針將會放在文件的結尾。文件打開時會是追加模式。如果該文件不存在，創建新文件用於讀寫。
* `ab+` 以二進制格式打開一個文件用於追加。如果該文件已存在，文件指針將會放在文件的結尾。如果該文件不存在，創建新文件用於讀寫。

問題2：請問 python 的 with 有什麼效果？  

傳統 open 需要接著 close 不然程式會報錯

```python3
# 開啟檔案
f = open(filename)

try:
  # ...

finally:
  # 關閉檔案
  f.close()
```

with 則可以在取用完檔案自動關閉，語法為：

```python3
with open(file.txt, 'w') as f:
```

* 將開啟的檔案 file.txt 儲存在 f 內
* with 結束會自動關閉 open
* 因此 with 範圍外無法讀取 f