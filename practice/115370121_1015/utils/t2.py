##
import datetime

print("t2,hello, world!")

def print_current_time():
    current_time=datetime.datetime.now()
    print(f"current date and time :{current_time}")

def calu_product(a,b):
    return a*b

def main():
    print_current_time()
    result=calu_product(5,10)
    print(f"The product of 5 and 10 is :{result}")

# if __name__ =='__main__':
#     result = calu_product(5,10)
#     print(f"The product of 5 and 10 is :{result}")

if __name__ == "__main__":
    main()