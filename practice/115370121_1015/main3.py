# import math
import random
# def calu_area_of_circle(radius):
#     return math.pi* radius **2

from utils.t1 import calu_area_of_circle
# import datetime
from utils.t2 import print_current_time
# import random
from utils.t2 import creat_radom_number
from utils.t2 import check_cwd,random_choice

def calc_time_different():
    import time
    start_time =time.perf_counter()
    for i in range(1000):
        random_number =creat_radom_number()
        print(f"random number (die roll):{random_number}")
    end_time =time.perf_counter()
    time_different=end_time - start_time
    print(f"time taken to roll the die 1000 times:{time_different:.6f} seconds")
    return end_time-start_time

def main():
    calc_time_different()
    

if __name__=='__main__':
    main()