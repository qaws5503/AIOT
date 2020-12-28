# Day19 撰寫 Flask Web 程式存取 MongoDB

## RESTful

RESTful 不是標準，而是一種設計風格。

### RESTful URI 的命名習慣

* 使用 / 斜線符號表示資源間的層次關係
* 不要在結尾使用 / 斜線符號
* 使用 - 連字符號提高可讀性，不要使用 _ 底線
* 全部用小寫的字母
* 不要再 URI 中包含 CRUD 函數的名稱

### RESTful API 規範下的方法

* POST 通常用於新增資料(包含檔案上傳)
* GET 用於獲取資料
* PUT/PATCH 用於更改資料
* DELETE 用於刪除資料

## 作業

問題：使用 Flask 撰寫一個會員系統，將會員資料存入 MongoDB，並提供 4 種 API 操作 MongoDB 中的資料，分別是新增、修改、刪除、查詢。

首先先安裝必要的函式庫

```
$ pip install flask
$ pip install Flask-PyMongo
$ pip install bson
```

先 import 重要的函式庫，並且透過`app.config['MONGO_URI']`指定 mongo 的位置，最後有`/test`是因為要取用的是 test Database

```python3
from pymongo import MongoClient
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/test'
mongo = PyMongo(app)
```

### 查詢

創造兩個網址 `/members` `/member/<id>`，前者為沒有指定的搜尋，後者為指定特定`id`的搜尋。  
函式先確認是否有`id`傳入

* 沒有：利用`mongo.db.member.find({})`搜尋全部資料，存入一個 object 叫`members`，之後將一筆一筆的資料用字串形式寫入 `result`的 list 內，最後用`jsonify()`印出比較漂亮的結果。
* 有：利用`mongo.db.member.find_one({})`找到一個特定搜索範圍的結果存入`result`並轉成字串，最後一樣使用`jsonify()`印出漂亮的結果。

```python3
@app.route('/members')
@app.route('/member/<id>', methods = ['GET'])
def get_member(id=None):
	if id is None:
		members = mongo.db.member.find({})
		result = []
		for member in members:
			member['_id'] = str(member['_id'])
			result.append(member)
		return jsonify(result)
		
	else:
		result = mongo.db.member.find_one({'_id': ObjectId(id)})
		if result is not None:
			result['_id'] = str(result['_id'])
		return jsonify(result)

```

Robo 3T 搜尋資料庫結果：

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.1.png)

Get`:5000/members`的結果：

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.2.png)

兩者結果一致

### 新增

先使用`request.form.get()`取得 Post 傳輸過來的資料，要逐個 KEY 來取得資料，取得後使用`mongo.db.member.insert_one({ })`來新增資料。  
最後回傳存入資料的 id 。

```python3
@app.route('/members', methods = ['POST'])
def add_member():
	name = request.form.get('name')
	result = mongo.db.member.insert_one({'name': name})
	return str(result.inserted_id)
```

回傳資料 id：

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.3.png)

將回傳的 id 透過查詢指令：

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.4.png)

看到查詢結果和輸入時一致

### 刪除

使用`mongo.db.member.find_one({ })`搜尋傳入的 id 資料，再利用`mongo.db.member.delete_one()`刪除該筆資料，最後使用`del_result.deleted_count`來統計總共刪除多少筆資料。

```python3
@app.route('/members/<id>', methods = ['DELETE'])
def remove_member(id):
	result = 0
	member = mongo.db.member.find_one({'_id': ObjectId(id)})
	
	if member is not None:
		del_result = mongo.db.member.delete_one(member)
		result = del_result.deleted_count
		
	return "Delete %s data" % str(result)
```

原始有 5 筆資料：

![image5](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.5.png)

透過 Robo 3T 取得要刪除資料的 id：

![image6](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.6.png)

刪除後，剩餘 4 筆資料：

![image7](https://github.com/qaws5503/AIOT/blob/master/pictures/Day19-1.7.png)

### 更新

更新指令使用 Put 來完成，一樣先使用`request.form.get()`來取得 Put 傳遞過來的資料，再將想更新的資料寫入一個叫`new_value`的 Dictionary，裡面放著`$set`的 Key，value 為更改過後的值`{ "$set": { "name": name} }`。  
資料都準備好後，使用`mongo.db.member.update_one({"_id": ObjectId(id)}, new_value)`來更新資料，`id`為要更改資料的 id，`new_value`為剛剛準備好的 Dictionary。  
最後再使用`upd_result.modified_count`來統計總共更改了多少筆資料

```python3
@app.route('/members/<id>', methods = ['PUT'])
def update_member(id):
	result = 0
	name = request.form.get('name')
	new_value = { "$set": { "name": name} }
	upd_result = mongo.db.member.update_one({"_id": ObjectId(id)}, new_value)
	
	if upd_result is not None:
		result = upd_result.modified_count
	
	return "Update %s data" % str(result)
```

## 補充

可以利用`myclient.list_database_names()`來查看現在資料庫中有哪些 Database

```python3
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
myclient.list_database_names()
```