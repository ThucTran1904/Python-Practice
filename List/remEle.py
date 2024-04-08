'''
- Write a Python program to remove all elements from a given list present in another list
'''

def remove_common_elements(l1, l2):
    return list(filter(lambda x: x not in l1, l2))

my_list = [30, 9, 4, 19, 4, 2]
her_list = [15,11,19,68,10,9,19,76]
result = remove_common_elements(my_list, her_list)
print('The list after removing the common elements is:', result)