try:
    with open("/Users/shanyu/Desktop/Ｃ/practice/115370121_1022_w7/data/data.csv","r",encoding="utf-8") as f:
        data=f.readlines()##readlines()
except FileNotFoundError:
    print("file not found.Please check the file path and try again.")