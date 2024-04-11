'''
- Write a Python program to print the even numbers from a given list
'''

def even_number(list):
    initial_list = []
    for i in list:
        if i % 2 == 0:
            initial_list.append(i)
    return initial_list

my_list = [30, 9, 4, 19, 4, 2]
updated_list = even_number(my_list)
print(updated_list)