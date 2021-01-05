# 存取已經建立好的mongoDB
from pymongo import MongoClient  
import base64

# 連接到local端的MongoDB，MongoDB database使用Robot3T建立
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['test_db'] # 建立一個data base名為test_db
coll = db['Collections'] # 在test_db中 建立一個collections名為coll
img_name = "waves.jpg"

# 讀取圖片，轉成二進制
with open(img_name, "rb") as f: #使用python內建的檔案讀寫工具open
    strpic = base64.b64encode(f.read()).decode('utf-8') # 將讀取到的圖片(f)編碼成二進制檔
    mydata = {'jpg_base64': strpic} # 將jpg_base64這個key和二進制化的圖片編成一組字典my_data
    result = coll.insert_one(mydata) # 在coll裡面新增my_data
    print(result.inserted_id) # 打印出my_data在儲存時，DB分配出來的id

# 將圖片的檔名、以及在DB中對應的id儲存下來
with open("imageList.txt", "a+") as file: # 編輯imageList.txt文件。不存在則創建之
    old = file.read() # read everything in the file # 讀取imageList.txt
    file.seek(0) # rewind
    content = '%\n'+img_name+'\n'+str(result.inserted_id) # 將圖片名和id整合到變數content中
    # 接著將content儲存到imageList.txt中
    file.write(content+"\n" + old) # write the new line before 