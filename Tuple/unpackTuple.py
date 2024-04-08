'''
- Write a Python program to unpack a tuple in several variables
'''

thuk_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

var1, var2, *rest_value = thuk_tuple
print('var1: ', var1)
print('var2: ', var2)
print('rest_value: ', rest_value)