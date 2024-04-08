'''
- Write a Python program to slice a tuple
'''

def slice_tuple(my_tuple):
    return my_tuple[1:5:2] # 2 is the step


thuk_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
print(slice_tuple(thuk_tuple))