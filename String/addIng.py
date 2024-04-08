'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged
'''

def modify_string(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else: 
        return s + 'ing'
    
user_input = input('Enter a string: ')
result = modify_string(user_input)
print(f'Modified string: {result}')