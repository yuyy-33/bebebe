##
import datetime
import random

print("t2,hello, world!")

def random_choice(my_list):
    return random.choice(my_list)


def check_cwd():
    import os
    cwd = os.getcwd()
    print(f"current workig directory;{cwd}")

def print_current_time():
    current_time=datetime.datetime.now()
    print(f"current date and time :{current_time}")

def calu_product(a,b):
    return a*b

def creat_radom_number():
    return random.randint(1,6)


def main():
    print_current_time()
    result=calu_product(5,10)
    print(f"The product of 5 and 10 is :{result}")

# if __name__ =='__main__':
#     result = calu_product(5,10)
#     print(f"The product of 5 and 10 is :{result}")

if __name__ == "__main__":
    main()