import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import pandas as pd

#data = pd.Series([5,4,-2,3,7])
#可以自訂索引
#data = pd.Series([5,4,-2,3,7],index=['a','b','c','d','e'])
#print(data)

#觀察資料
#print("資料型態",data.dtype)
#print("資料數量",data.size)
#print("資料索引",data.index) #索引形態是object

#取得資料：根據順序、根據索引
#print(data[0],data[2])
#print(data["e"],data["d"])

# 數字運算：基本、統計、順序
#print("最大值",data.max())
#print("總和",data.sum())
#print("標準差",data.std())
#print("中位數",data.median())
#print("最大三個數",data.nlargest(3)) #data.nsmallest(2) 最小兩個數

data = pd.Series(["您好","Python","Pandas"])
#字串運算：基本、串接、搜尋、取代
#print(data.str.lower()) #變小寫
#print(data.str.len()) #算出每個字串的長度
#print(data.str.cat(sep='-')) #把字串串起來，需要參數連接
#print(data.str.contains("P")) #判斷字串中是否包含__，回傳bool
print(data.str.replace("您好","Hello")) #把指定的代換掉
