import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import pandas as pd

#建立 Series
#data = pd.Series([20,10,15])
'''
print(data)

print("Max",data.max())
print("Median",data.median())

data = data*2

data=data==20
print(data)
'''

#建立DataFrame dictionary
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
print(data)
print("-----------------")
#print(type(data))
#取得特定欄位
#data[欄位名稱]
#print(data["name"])
#print(data["salary"])
#取得特定的列
print(data.iloc[1])
print(data)