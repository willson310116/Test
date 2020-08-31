import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import pandas as pd
#資料索引：pd.DataFrame(字典,index=索引列表)
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
},index=['a','b','c'])
print(data)
print("------------------")
# 觀察資料
#print("資料數量",data.size)
#print("資料型態（列,欄）",data.shape)
#print("資料索引",data.index)

#取得列：根據順序、根據索引
#print("取得第二列",data.iloc[1],sep="\n")
#print("------------------")
#print("取得第c列",data.loc["c"],sep="\n")

#取得欄(Column/直向)的Series資料：根據欄位名稱
#print("取得name欄位",data["name"],sep="\n")
names = data["name"] #取得單維度的Series資料
print("把name全部轉大寫",names.str.upper(),sep="\n")
#計算薪水平均值
salaries = data["salary"]
print("薪水平均值：",salaries.mean())

#建立新欄位
#data[新欄位名稱]=列表
data["renvenue"]=[500000,400000,300000]
#data[新欄位名稱]=Series 的資料
data["rank"] = pd.Series([3,6,1],index=["a","b","c"])
data["cp"] = data["renvenue"]/data["salary"]
print(data)




