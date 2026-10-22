with open("/Users/shanyu/Desktop/Ｃ/practice/115370121_1022_w7/data/data.csv","r",encoding="utf-8") as f:
    data=f.readlines()##readlines()
##print data
print(data)

name=input("enter your name: ")
for i, line in enumerate(data):
    if i == 0:
        continue
    words=line.split(",")
    if name ==words[0]:
        print(f"{i}: {words[0]},{words[1].strip()},{words[2].strip()}")

