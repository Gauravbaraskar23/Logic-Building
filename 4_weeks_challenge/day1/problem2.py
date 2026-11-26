# Remove duplicates from a list while keeping the order.
def remove_duplicates(nums):
    seen = set()
    result = []
    for i in nums:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
    
nums = [1, 2, 1, 3, 2]
# nums = [1,2,2,3,3,4,5,6,6,7]
print(remove_duplicates(nums))