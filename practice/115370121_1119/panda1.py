##import panda
import pandas as pd

##read a csv file
data = pd.read_csv('practice/115370121_1119/data/grades.csv',encoding='utf-8-sig') ##read a csv file    
print(data) ##print the data
data.info() ##print the information of the data
data.describe() ##print the statistical information of the data

##calulate the mean of the grades
print(data.isnull().sum()) ##check for missing values

##calculate the mean of the grades
data_subject=data.drop(["班級","學號"],axis=1) ##drop the columns of class and student number
print(data_subject.mean()) ##calculate the mean of the grades
print(data_subject.std()) ##calculate the standard deviation of the grades

##add a total column to the data
data["總分"]=data_subject.sum(axis=1) ##add a total column to the data
print(data) ##print the data

##reanking

data_rank=data.sort_values(by="總分",ascending=False) ##sort the data by total score in descending order
print(data_rank) ##print the data