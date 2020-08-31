import sys
# sys.path.append("/usr/local/lib/python3.8/site-packages")
import pandas as pd
import sklearn
import seaborn

#讀取資料
#把csv檔讀成一個DataFrame
data = pd.read_csv("googleplaystore.csv")
#print(data)
#觀察資料
# print("資料數量",data.shape)
# print("資料欄位",data.columns)
# print("--------------------------------")

#分析資料：評分的各種統計數據
# condition = data["Rating"]<=5
# data = data[condition]
# #print(data)
# print("平均數",data["Rating"].mean())
# print("中位數",data["Rating"].median())
# print("取得前一千個應用程式的平均",data["Rating"].nlargest(1000).mean())

#分析資料：安裝數量的各種統計數據
#print(data["Installs"]) #資料識字串，不能做平均
# 要把資料轉成數字才能做統計
#data["Installs"] = pd.to_numeric(data["Installs"])
# 失敗->字串含有 , +
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))
# #print(data["Installs"][10472])
# #print(data.iloc[10472])
# #print(data["Installs"])
# print("平均數",data["Installs"].mean())
# condition = data["Installs"]>100000
# #data = data[condition]
# print("安裝數量大於十萬的應用程式有幾個",data[condition].shape[0])


#基於資料的應用：關鍵字搜尋應用程式名稱
keyword = input("Type a keyword: ")
condition = data["App"].str.contains(keyword,case=False) #case=False忽略大小寫
print(data[condition]["App"])
print("包含關鍵字的應用程式數量：",data[condition].shape[0])