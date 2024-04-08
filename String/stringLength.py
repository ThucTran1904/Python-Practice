'''
- Write a Python program to calculate the length of a string

'''

def stringLength(s):
    return len(s)

user_input = input('Enter a string: ')
print(f"Length of input: {stringLength(user_input)}")