import sys
sys.path.append("/usr/local/lib/python3.8/site-packages")
import pandas as pd

#篩選練習-Series
# data = pd.Series([30,15,20])
# #condition = [True,False,True]
# condition = data>18
# print(condition)
# filteredData = data[condition]
# #print(data)
# print(filteredData)

# data = pd.Series(["您好","Python","Pandas"])
# # condition = [False,True,True]
# condition = data.str.contains("P")
# print(condition)
# filteredData = data[condition]
# print(filteredData)

#篩選練習-DataFrame
data = pd.DataFrame({
	"name":["Amy","Bob","Charles"],
	"salary":[30000,50000,40000]
	})
print(data)
print("------------------")
#condition = [False,True,True]
# condition = data["salary"]>=40000
condition = data["name"]=="Amy"
print(condition)
filteredData = data[condition]
print(filteredData)

