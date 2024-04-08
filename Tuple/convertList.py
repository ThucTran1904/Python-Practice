'''
- Write a Python program to convert a list to a tuple
'''

def convert_list_to_tuple(l):
    return tuple(l)

my_list = [30, 9, 4, 19, 4, 2]
the_tuple = convert_list_to_tuple(my_list)
print(type(the_tuple) )