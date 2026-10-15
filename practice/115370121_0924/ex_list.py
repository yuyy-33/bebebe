##list##
nums = [1, 2, 3, 4, 5]
print(nums[0])
print(nums[-1])

nums.append(6)
print(nums)
nums[0]=99
print(nums)

nums_2=[7,8,9]

nums_3= nums + nums_2
print(nums_3) #[99, 2, 3, 4, 5, 6, 7, 8, 9]

print(sum(nums_3)) #計算總和
print(sorted(nums_3,reverse=True)) #由大到小排序

print(nums[-2])

nums_4=[1,3,5,7,9,-1,-3,-5,-7,-9]
print(sorted(nums_4))##由小到大排序
print(sorted(nums_4,reverse=True))##由大到小排序
