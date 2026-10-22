##read name.txt.file

fn = "name.txt"
import os
print(f"current working directory:{os.getcwd()}")
fn = "name.txt"
data_list=[]
with open(fn,"r") as file:
    data = file.readlines()
    for line in data:
        data_list = line.strip().split(" ")
        print(data_list)