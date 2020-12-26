# Day17 使用 Docker 架設 Flask Web Server

## 架設網站

```python3
#!/usr/bin/env python3

# 引用需要的套件, 若有多個套件要引用，可使用逗號隔開
from flask import Flask, request

app = Flask(__name__)

# 設定網址路由，及接受的 method(預設是 GET)
@app.route('/', methods=['GET'])
def index():
    return "Hello World"
    
if __name__ == '__main__':
    app.run()
```

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day17-1.1.png)

執行過後，依照指示訪問 [http://127.0.0.1:5000](http://127.0.0.1:5000)，就可以看到 Hello World 的字樣

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day17-1.2.png)