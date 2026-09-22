def total_nodes(nums):
  freq = {}
  count = 0
  for num in nums:
    if num not in freq:
      freq[num] = 1
    else:
      freq[num] += 1
  for i in freq.values():
    if i == 2:
      count += 1
  if count > 0:
    return count
  else:
    return -1

nums = [1,2,3,4,5]
nums1 = [1,2,2,3,3,4,5]
nums2 = [1]
nums3 = [1,2,2,3,3,3,5,5,6,6,7,7,8,9,9,]

print(total_nodes(nums))
print(total_nodes(nums1))
print(total_nodes(nums2))
print(total_nodes(nums3))