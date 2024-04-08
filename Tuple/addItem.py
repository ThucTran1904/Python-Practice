'''
- Write a Python program to add an item in a tuple
'''

def add_item_to_tuple(tuple, new_item):
    tuple += (new_item,)
    return tuple

thuk_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
new_item = 90
updated_tuple = add_item_to_tuple(thuk_tuple, new_item)
print('Updated tuple: ', updated_tuple)
    