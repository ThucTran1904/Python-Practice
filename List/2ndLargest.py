'''
- Write a Python program to find the second largest number in a list

'''
def find_second_largest_sorted(l):
    sorted_list = sorted(l)
    return sorted_list[-2]

my_list = [30, 9, 4, 19, 4, 2]
print(f"The second largest number in a list is {find_second_largest_sorted(my_list)}")