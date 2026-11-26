##generate an arragy using numpy

import numpy as np ##load numpy library, short name up

a_list = []
for i in range(1,51):
    a_list.append(i)

arr = np.array(a_list) ##a_list=[1...50]

##mean
mean=np.mean(arr)
print(mean)

##standrad deviation
std=np.std(arr)
print(std)

##max and min
max_value=np.max(arr)
min_value=np.min(arr)
print(max_value,min_value)

##np.arange() function
arr2 = np.arange(1,51) ##generate an array from 1 to 50
arr3=np.linspace(1,50,50) ##generate an array from 1 to 50 with 50 elements

##property of array
##reshape into 5*10
arr2=arr2.reshape(5,10) ##reshape into 5 rows and 10 columns
print(arr2) ##print the array
print(arr2.shape) ##shape of the array

##matrix multiplication :different shapes 2*3 and 3*2 

A=np.array([[1,2,3],[4,5,6]]) ##2*3 matrix
B=np.array([[7,8],[9,10],[11,12]]) ##3*2 matrix
C=np.dot(A,B) ##matrix multiplication
print(C)