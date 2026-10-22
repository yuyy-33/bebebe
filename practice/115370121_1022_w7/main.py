f=open ("/Users/shanyu/Desktop/Ｃ/practice/115370121_1022_w7/data/data.txt","r",encoding="utf-8")
##read file
data=f.read()
##close file
f.close()
##print data
print(data)

##print data f.close
with open ("/Users/shanyu/Desktop/Ｃ/practice/115370121_1022_w7/data/data.txt","r",encoding="utf-8") as f:
    print(data)