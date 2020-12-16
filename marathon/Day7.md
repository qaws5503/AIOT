## 作業一

### 透過 brew 安裝

相關文件：[mongo 的 github](https://github.com/mongodb/homebrew-brew)

```
$ brew tap mongodb/brew
$ brew install mongodb-community
```

### 手動安裝

從 [Mongo](https://www.mongodb.com/try/download/community) 這裡下載檔案，將下載下來的檔案解壓縮到`/usr/local/bin`裡面。[教學影片](https://youtu.be/dxrW-W4AR2A)

### 運行 Mongo

```
# 建立db資料夾
sudo mkdir ~/data/db

# 啟動 mongo 資料庫
sudo mongod --dbpath ~/data/db

# ctrl+c為結束資料庫
```

再開啟新的終端機打上`mongo`即可連線進入資料庫

## 作業二

### 使用終端機操作mongo

```
db.member.insert({
	"name": "Kevin",
	"email": "test@abc.com",
	"phone":"0912345678"
})
db.member.find().pretty()
```

![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day7-2.1.png)

```
db.member.update({"name": "Kevin"},
{$set:{
	"name": "Cathy",
	"age": "25"
}})
db.member.find().pretty()
```

![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day7-2.2.png)

### 使用 Robo 3T

對著Collections點選右鍵選擇create collections 新增 collections，再對已新增的 collections點選右鍵選擇 Insert document，輸入

```
"name": "Kevin",
"email": "test@abc.com",
"phone":"0912345678"
```

![image3](https://github.com/qaws5503/AIOT/blob/master/pictures/Day7-2.3.png)

對著 document 點選 edit document 即可修改。修改後：

![image4](https://github.com/qaws5503/AIOT/blob/master/pictures/Day7-2.4.png)

## 補坑
補充一個坑如果資料庫創建資料庫時顯示

```
Address already in use MONGODB
shutting down with code:48
```

代表這個port已經被佔用了，也就是有另一個資料庫並沒有被關閉。此時執行` sudo killall mongod`即可關閉全部的資料庫。

