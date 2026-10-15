name= "fang-chin" #string
surname= "chen"
print(name[0],name[7])
# name[0] = "t" #string不可變更 
print(name[3:5]) 
print("f"in name)
fullname= name + " " + surname
print(fullname)

print(len(fullname)) #計算長度
print(fullname.upper()) #大寫
print(fullname.lower()) #小寫

fullname=" Fang-Chin Chen "
print(fullname)
print(fullname.strip()) #前後空格拿掉
fullname=fullname.strip()
print(fullname.replace("Fang","Tang")) #取代
print(fullname[-1]) #取最後一個字元


