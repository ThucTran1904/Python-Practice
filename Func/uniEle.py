'''
- Write a Python function that takes a list and returns a new list with unique elements of the first list
'''

def get_unique_elements(my_list):
    return list(set(my_list))

thuk_list = [30,9,4,19,4,2]
unique_list = get_unique_elements(thuk_list)
print(unique_list)