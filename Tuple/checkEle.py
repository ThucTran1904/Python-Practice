'''
- Write a Python program to check whether an element exists within a tuple
'''

def element_in_tuple(tuple, element):
    return element in tuple
thuk_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
element = 100
if element_in_tuple(thuk_tuple, element):
    print(f"'{element}' exists in the tuple" )
else:
    print(f"'{element}' does not exist in the tuple ")