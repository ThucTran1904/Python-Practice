'''
- Write a Python program to append a list to the second list
'''

# 1st way: Using extend() method
def append_list_to_another(l1, l2):
    l2.extend(l1)
    
my_list = [30, 9, 4, 19, 4, 2]
her_list = [15,11,19,68,10,9,19,76]
append_list_to_another(my_list, her_list)
print('Updated second list:',her_list)

# 2nd way: Using list concatenation
def append_list_concatenation(l1, l2):
    return l1 + l2

my_list1 = [30, 9, 4, 19, 4, 2]
her_list1 = [15,11,19,68,10,9,19,76]


updated_list = append_list_concatenation(my_list1, her_list1)
print('Updated list:',updated_list)