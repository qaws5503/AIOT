# Day 8

## 作業一

問題：安裝 Anaconda，使用 pip 或是 conda 工具安裝 pymongo 套件。

先在 anaconda 內創造一個環境，名字為 pymongo，python版本指定為 3.8

```
$ conda create -n pymongo python=3.8
$ conda activate pymongo
```

進入創造好的環境後，就可以令用以下指令安裝 pymongo

```
$ conda install -c anaconda pymongo
```

# 作業二

問題：使用 python 操作 mongo 資料庫，包含新增、刪除、修改、查詢。

首先要先開啟 mongo 資料庫，打開終端機打上

```
$ sudo mongod --dbpath ~/data/db
```

之後開啟 python

```python3
from pymongo import MongoClient
client = MongoClient(host='127.0.0.1', port=27017)
```

如此就已經連上 mongo 了，之後我們創建一個 test documents 並且在裡面再創建一個 member collection

```python3
db = client['test']
collection = db['member']
```

以下則介紹基本的幾個指令，分別為新增、刪除、修改、查詢。

### 新增

```python3
# insert one data
mydata = {'name': 'Kevin'}
result = collection.insert_one(mydata)
print(result.inserted_id)


# insert many data at once
data_list = [
    {'name': 'Jimmy'},
    {'name': 'Sammy'},
    {'name': 'Molly'},
    {'name': 'Benson'}
]
result = collection.insert_many(data_list)
print(result.inserted_ids)
```

### 刪除

```python3
# delete one data

before = collection.count_documents({})
collection.delete_one({'name': 'Kevin'})
after = collection.count_documents({})
print('There were', before, 'datas, and after delete there still have', after,'datas')

# delete many data
# result = collection.delete_many({'name': 'Kevin'})
```

### 修改

```python3
# update data
filter_ = {'name':'Jimmy'}
update_ = {'$set': {'name': 'Handsome'}}
collection.update_one(filter_, update_)
```

### 查詢

```python3
# find data in db
result = collection.find().sort('name',1)
for i in result:
    print(i)

# limit the result number
# result = collection.find().limit(2)

# find one data
# collection.find_one({})
```