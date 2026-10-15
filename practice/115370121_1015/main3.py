# import math
# def calu_area_of_circle(radius):
#     return math.pi* radius **2

from utils.t1 import calu_area_of_circle
# import datetime
from utils.t2 import print_current_time
import random

def creat_radom_number():
    return random.randint(1,6)

def main():
    print_current_time()
    for _ in range(10):
        random_number=creat_radom_number()
        print(f"random number (die roll) :{random_number}")
    # radius = 5
    # area = calu_area_of_circle(radius)
    # print(f"The area of the circle with radius {radius} is:{area}")

if __name__=='__main__':
    main()