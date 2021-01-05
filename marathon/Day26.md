# Day26 透過 Flask 將訊息從樹梅派傳送給 PC

## Raspberry PI install flask

首先先在 Raspberry PI 上安裝 flask

```
$ pip3 install flask
```

## Raspberry PI ip

輸入 `$ ifconfig` 的指令，查看 wlan0 裡面 inet 顯示的數字，這組數字即為 ip

## 在 Raspberry PI 上架設 Flask Web

可以先建立一個簡單的 web，host 記得要更改為 Raspberry PI 的 ip

```python3
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	return 'hello, Here is June'
if __name__ == "__main__":
	app.run(host='192.168.2.201', port = 8080, debug = True, threaded = True)
```

## Web API

在 PC 上輸入`http://192.168.2.201:8080`，`:8080`前面會因 Raspberry PI ip 不同而調整

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day26-1.1.png)

## PC 利用 python 取得 Web API 資料

### 安裝 requests

先確認是否有安裝 requests，如果不是用 anaconda 的虛擬環境直接 `pip install requests`，如果是安裝 anaconda 則不同系統指令不同：

#### windows

```
# env 為環境名稱
$ activate env
$ conda install requests
```

#### macOS

```
# env 為環境名稱
$ source activate env
$ conda install requests
```

### 執行 python

執行 Day26.py 的檔案

```python3
import requests
r = requests.get('http://10.17.4.132:8080')
if r.status_code == requests.codes.ok:
    print("OK")
print(r.text)
```

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day26-1.2.png)

接收到 Web API 上的資訊

## 問題

請思考在程序中，@app.route("/")以及下方的def hello()：有什麼樣的關係？

`@app.route("/")` 代表下方函式執行的網址，而`def hello()`裡頭則是包含了這個網址要執行的動作為何