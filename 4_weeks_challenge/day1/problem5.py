# Write a function that modifies a list passed into it, and observe what happens outside.
def add_item(lst):
    lst.append(99)

def reassign(lst):
    lst = [1, 2, 3]

a = [10, 20]
add_item(a)
print(a)      

b = [10, 20]
reassign(b)
print(b)     

def add_item_pure(lst):
    return lst + [99]

c = [10, 20]
new_c = add_item_pure(c)

print(c)
print(new_c)