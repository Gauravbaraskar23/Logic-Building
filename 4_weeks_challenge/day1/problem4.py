# Rewrite a filter-and-transform for loop as a comprehension.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []
# for n in nums:
#     if n % 2 == 0:
#         result.append(n * n)
# print(result)


# List comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num*num for num in nums if num%2 == 0]
print(result)

# Set comprehension
numbers = [1, -1, 2, -2, 3]
squares = {num*num for num in numbers}
print(squares)

# Dict comprehension
# Expected: {'apple': 5, 'fig': 3, 'banana': 6}.
fruits = ["apple", "fig", "banana"]
fruit_len = {fruit: len(fruit) for fruit in fruits }
print(fruit_len)