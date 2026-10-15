import utils.t1 as t1 ##縮寫
import utils.t2 as t2

# t1.calu_sum(5,10)
# t2.calu_product(5,10)
def main():
    sum1=t1.calu_sum(5,10)
    print(f"The sum of 5 and 10 is :{sum1}")
    product1=t2.calu_product(5,10)
    print(f"The product of 5 and 10 is :{product1}")

if __name__=='__main__':
    main()