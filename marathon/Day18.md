# Day18 使用 Python 開發 Flask 網頁程式

## 作業一

問題：撰寫一個 Flask Web 應用程式，分別使用 Get / Post 來發送 Request，且能取得 Request 傳遞的參數。

### 使用 GET 發出請求，並回傳 Hello World

```python3
from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
	return "Hello World"
if __name__ == '__main__':
	app.run()
```

可以直接在網頁上前往 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)，或是透過 [Postman](https://www.postman.com/downloads/) 來請求。

以下示範 Postman，開啟程式後，點選 Create a request

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.1.png)

在上方選擇 GET 方法，並且輸入`:5000`，按 send 就能得到回傳結果

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.2.png)

我們再回去看程式方面，會顯示有連線的詳細資料，方法、IP 等等

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.3.png)

### 使用 GET 取得 Request 中的參數

更改上述 index 函式，用`request.args.get('name')`取得 KEY 為 name 的 value，最後再回傳這個 value

```python3
@app.route('/', methods=['GET'])
def index():
	name = request.args.get('name')
	return "Hello " + name
```

使用 Postman，在 Key 和 VALUE 輸入 name 和 Jimmy，會發現上面的GET 網址有改變了，再按 Send 會看到我們要的輸出 Hello Jimmy

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.4.png)

## 使用 Post 傳遞參數資料

透過`request.form.get()`來取得參數

```python3
@app.route('/', methods=['POST'])
def index():
	name = request.form.get('name')
	passwd = request.form.get('passwd')
	return "Your name: " + name + ", Your passwd: " + passwd
```

在 Postman 選擇 POST，按 body 再按 form-data 輸入程式需要的參數，再按 Send

![image5](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.5.png)

## 使用 Post 檔案上傳單一檔案

`request.files['file']`取得檔案，`file.save()`把檔案存起來，最後返回儲存的檔案

```python3
@app.route('/', methods=['POST'])
def index():
	file = request.files['file']
	file.save(file.filename)
	return file.filename
```

Postman 地方按 POST 再按 Body，然後 KEY 輸入 file，並從 text 更改為 File

![image6](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.6.png)

## 使用 Post 檔案上傳多個檔案

`request.files.getlist('file')`取得多個檔案，回傳總共上傳的數量

```python3
@app.route('/', methods=['POST'])
def index():
	files = request.files.getlist('file')
		total = 0
	for file in files:
		total += 1 
		file.save(file.filename)
	return str(total)
```

## 取得 Flask Server 上的檔案

一樣透過`request.files.get('files')`取得檔案，利用`redirect(url_for('upload_finish, filename=file.filename'))`直接導向`upload_finish`函式所產生的網址。  
`upload_finish`回傳剛剛儲存下來的檔案

```python3
@app.route('/', methods=['POST'])
def index():
    file = request.files.get('file')
    file.save(file.filename)
    return redirect(url_for('upload_finish', filename=file.filename))

@app.route('/upload_finish/<filename>')
def upload_finish(filename):
    return send_file(filename)
```

![image7](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.7.png)

## 回傳 HTML 畫面

`app.config['APPLICATION_ROOT'] = "."`. 代表取得程式當前目錄，並在這個目錄下創建 templates 資料夾，裡面入著 html 檔。  
再透過`render_template('index.html')`讀取 index.html 的檔案

python：

```python3
from flask import Flask, request, render_template
app = Flask(__name__)
app.config['APPLICATION_ROOT'] = "."

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run()
```

html 檔：

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

Postman 取得請求會顯示為 html 語法

![image8](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.8.png)

可以選擇上面 Preview 顯示真正會看到的網頁

![image9](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-1.9.png)

* [鏈結](https://www.lifewire.com/edit-html-with-textedit-3469900)有教學 Mac 如何創建 html 檔
* [HTML線上編譯器](http://myweb.ncku.edu.tw/~arter/20171212/source.cgi)

## 作業二

問題：實作檔案上傳功能，並提供簡易畫面使其能透過畫面上傳檔案。

先將 methods 設定有 GET 和 POST，利用`request.method`判斷現在請求是哪個方法，如果是 POST 執行迴圈內也就是存上傳的檔案，如果不是 POST 意味著是 GET 就回傳先設定好的 html 檔案。  
迴圈內一樣最後回傳 `upload_finish`函式的網址，即可在傳完檔案直接轉跳到顯示檔案的網址。

python：

```python3
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        file.save(file.filename)
        return redirect(url_for('upload_finish', filename=file.filename))
    return render_template('upload_demo.html')
```

html檔：

```html
<!DOCTYPE html>
<html>

 <head>
  <Title>Flask Upload Demo</Title>
 </head>


 <body>
  <h1>Upload A File!!</h1>
  
  <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
  </form>

 </body>
</html>
```

進入網頁：

![image10](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-2.1.png)

上傳檔案後：

![image11](https://github.com/qaws5503/AIOT/blob/master/pictures/Day18-2.2.png)

* [教學](https://medium.com/@charming_rust_oyster_221/flask-%E6%AA%94%E6%A1%88%E4%B8%8A%E5%82%B3%E5%88%B0%E4%BC%BA%E6%9C%8D%E5%99%A8%E7%9A%84%E6%96%B9%E6%B3%95-1-c11097c23137)