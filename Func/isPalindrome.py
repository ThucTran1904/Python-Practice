'''
-Write a Python function that checks whether a passed string is palindrome or not

'''

def is_palindrome(s):
    return s == s[::-1]
user_input = str(input('Please enter a word: '))
if is_palindrome(user_input):
    print(f'-> The word {user_input} is a palindrome')
else:
    print(f'-> The word {user_input} is not a palindrome')