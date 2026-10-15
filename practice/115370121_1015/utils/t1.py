###
import math

print("t1,hello world")

def calu_area_of_circle(radius):
    return math.pi* radius **2

def calu_sum(a,b):
    return a+b

# if __name__ =='__main__':
#     result = calu_sum(5,10)
#     print(f"The sum of 5 and 10 is :{result}")

def main():
    result=calu_sum(5,10)
    print(f"The sum of 5 and 10 is :{result}")

if __name__ == "__main__":
    main()