##open data.txt file
with open ("/Users/shanyu/Desktop/Ｃ/practice/115370121_1022_w7/data/data.txt","r",encoding="utf-8") as f:
    ##read file
    data=f.readlines()##readlines()
print(data)
name=input("enter your name: ")
for i, line in enumerate(data):  ##data is a list, so we can use for loop to print each line
    if name in line:  ##if name is in line, print the line
        print(f"{i+1} {name}: {line.strip()}")##strip()method removes the newline character 
        found_name=line.strip()
##open file
with open ("/Users/shanyu/Desktop/Ｃ/practice/115370121_1022_w7/data/found.txt","w",encoding="utf-8") as f:
    f.write(found_name)


