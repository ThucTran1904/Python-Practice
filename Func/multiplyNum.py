'''
- Write a Python function to multiply all the numbers in a list
'''

def multiply_list(list):
    result = 1
    for num in list:
        result *= num
    return result

list2 = [3,2,4]
thuk_list = [30, 9,4,19,4,2]
print(multiply_list(thuk_list))
print(multiply_list(list2))