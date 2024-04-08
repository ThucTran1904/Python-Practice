'''
- Write a Python program to check a list is empty or not

'''

def is_empty_list(l):
    if len(l) == 0:
        return True
    else:
        return False

my_list = [30, 9, 4, 19, 4, 2]
if is_empty_list(my_list):
    print('The list is empty')
else:
    print('The list is not empty')