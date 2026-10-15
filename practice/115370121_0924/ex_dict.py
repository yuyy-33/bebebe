d=dict()##空字典
d={}##空字典
d={"a":1,"b":2,"c":3}##key重複，會被覆蓋
print(d)
print(d["a"])##取值
print(d.get("b")) ##取值

d.clear()##clear
print(d)

d1=d.copy()##copy
print(d1)

##items()##取出所有key-value pair
d={"a":1,"b":2,"c":3}
print(d.items(),type(d.items()))
print(d.keys(),type(d.keys()))
print(d.values(),type(d.values()))

keys=d.keys()
values=d.values()
print(list(keys),list(values))##轉換成list
# for k,v in d.items():
#     print(k,v)

##student data using dictionary

student={}
student["name"]="yu-shan" ##key =value
student["age"]=20
student["gender"]="female"
print(student)