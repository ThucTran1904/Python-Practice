'''
- Write a Python program to find the index of an item of a tuple
'''

def find_index(tuple, item):
    try:
        return tuple.index(item)
    except ValueError:
        return f" not found in the tuple"
    
thuk_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
item_to_find = 80
result = find_index(thuk_tuple, item_to_find)
print(f"Index of {item_to_find}: {result}")