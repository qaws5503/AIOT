# Day20 在 Raspberry PI 上安裝 Flask Web Server

## 安裝 Raspberry PI 環境

```
$ sudo apt update
$ sudo apt install python-rpi.gpio
$ sudo apt install python-pip
$ sudo pip install flask
```

## 測試 Flask

```
$ sudo nano hello_flask.py
```

```python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello(): return "Hello World!"

if __name__ == "__main__"
	app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
```

到瀏覽器上輸入`http://192.168.2.201:8080/`

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day20-1.1.png)

Raspberry PI 顯示連線資料

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day20-1.2.png)

## 新增 template

先創建一個資料夾，cd 到資料夾內

```
$ sudo mkdir templates
$ cd templates
$ sudo touch index.html
$ sudo rmate index.html
```

輸入：

```html
<!DOCTYPE html>
<html>

 <head>
  <Title>Flask Demo</Title>
 </head>


 <body>
  <h1>Hello World</h1>
  
 </body>
</html>
```

再回到目錄

```
$ sudo touch hello_flask.py
$ sudo rmate hello_flask.py
```

```python3
from flask import Flask, request, render_template
app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '.'

@app.route("/")

def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)
```

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day20-1.3.png)

## 補充：設定遠端 VScode

### PC

1. vscode 擴充功能新增 **“Remote VSCODE”**
2. vscode 檔案>喜好設定>設定，右上角選擇切換 json，新增

	```
	// If set to true, error for remote.port already in use won't be shown anymore.
	"remote.dontShowPortAlreadyInUseError": false,
	// Address to listen on.
	"remote.host": "127.0.0.1",
	// Launch the server on start up.
	"remote.onstartup": true,
	// Port number to use for connection.
	"remote.port": 52698
	```

3. 按下 F1 輸入 **“Remote:Start Server”**
4. 終端機輸入：

	```
	ssh -R 52698:localhost:52698 pi@<Pi IP Address>
	```

### RapberryPI

1. 安裝 rmate

	```
	sudo pip install rmate
	```

2. 到要遠端的資料夾

	```
	sudo rmate *.file
	```

