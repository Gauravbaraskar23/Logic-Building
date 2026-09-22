# Write a Python program to calculate the sum of a list of numbers using recursion.

def sum_of_list(nums):
    
    n  = len(nums)
    if  n == 1:
        return nums[0]
    else:
        return nums[0] + sum_of_list(nums[1:])


nums = [2,4,5,6,7]
print(sum_of_list(nums))