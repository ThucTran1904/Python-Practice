'''
- Write a Python program to insert an element at a specified position into a given list
'''

def insert_element_at_position(l, ele, pos):
    l.insert(pos, ele)

my_list = [30, 9, 4, 19, 4, 2]
insert_element_at_position(my_list, 3, 2)
print('Updated list: ', my_list)

    