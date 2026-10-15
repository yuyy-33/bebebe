## calc sum form 1 to 100
sum=0 ## accumulator or variable
for i in range(1,101): ##range (stard,end,step)
    sum+=i
print("the sum is:", sum)

##odd sum from 1 to 100
sum=0##accumulator or variable
for i in range(1,101,2):##range (stard,end,step)
    sum+=i
print("the sum is:", sum)

##even sum from 1 to 100
sum=0##accumulator or variable
for i in range(2,101,2):##range (stard,end,step)
    sum+=i
print("the sum is:", sum)