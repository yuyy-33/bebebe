##import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

##create x y zdata
x=[1,2,3,4,5]
y=[2,4,6,8,10]
z=[1,4,9,16,25]

##plot line graph
plt.plot(x,y,label='y=2x',color='blue',marker='o') ##plot x and y
plt.plot(x,z,label='z=x^2',color='red',marker='s') ##plot x and z
plt.title('Line Graph') ##title of the graph
plt.xlabel('x') ##label of x-axis
plt.ylabel('y and z') ##label of y-axis
plt.legend() ##show legend 
plt.show() ##show the graph