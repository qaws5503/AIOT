# Day 6

## 作業一
問題：至 [w3schools](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all)，練習 SQL 的查詢指令 Select，使用 where 條件篩選，數字條件與字串條件篩選指令。

首先先查看資料庫內有什麼資料，發現是客戶資料
![image1](https://github.com/qaws5503/AIOT/blob/master/pictures/Day6-1.1.png)

透過 SQL 的 where 語法選出 Country 欄位為 USA 的資料

```SQL
SELECT * FROM Customers where Country='USA';
```
![image2](https://github.com/qaws5503/AIOT/blob/master/pictures/Day6-1.2.png)

再透過 like 語法篩選出 PostalCode 欄位8開頭的資料
```SQL
SELECT * FROM Customers where Country='USA' and PostalCode like '8%';
```

## 作業二

問題：至 [JSONLint](https://jsonlint.com/)，寫一個 JSON 文件，物件內容為: {"aiotid": 1,"description": "temperature", "value":23.5}，點選 Validate JSON，檢查正確性。

```
{
	"aiotid": 1,
	"description": "temperature",
	"value": 23.5
}
```