n=int(input("輸入項數："))
ln2=0.6931471805599453

total=0
next_print=1
for i in range(n):
    total=total+1/((2*i+1)*(2*i+2))
    if i+1==next_print:
        print(f"第{i+1}項部分和＝{total:.8f}")
        next_print=next_print*10

error=abs(ln2-total)
print(f"ln2={ln2:.8f}")
print(f"誤差={error:.8f}")

def cal():
    n=int(input("輸入項數："))
    ln2=0.6931471805599453

    total=0
    next_print=1
    for i in range(n):
        total=total+1/((2*i+1)*(2*i+2))
        if i+1==next_print:
            print(f"第{i+1}項部分和＝{total:.8f}")
            next_print=next_print*10
            
    error=abs(ln2-total)
print(f"誤差={error:.8f}")

print(cal())
