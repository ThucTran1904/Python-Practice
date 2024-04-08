'''
Write a Python function to reverses a string if it's length is a multiple of 4

'''

def reverseString(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else: 
        return s
    
user_input = input('Enter a string: ')
result = reverseString(user_input)
print(f"Modified string {result}")