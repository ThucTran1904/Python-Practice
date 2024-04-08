'''
- Write a Python program to remove duplicates from a list
'''

def remove_duplicates_list_comprehension(l):
    return [x for i, x in enumerate(l) if x not in l[:i]]

# Example usage:
my_list = [30, 9, 4, 19, 4, 2]
print(f"List without duplicates: {remove_duplicates_list_comprehension(my_list)}")
