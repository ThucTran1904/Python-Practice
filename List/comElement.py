'''
- Write a Python program to find common items from two lists
'''

# List comprehension
def find_common_items(l1, l2):
    return [element for element in l1 if element in l2]

my_list = [30, 9, 4, 19, 4, 2]
her_list = [15,11,19,68,10,9,19,76]
result = find_common_items(her_list, my_list)
print(f'Common item(s): {result}')