'''
- Write a Python program to check a dictionary is empty or not
'''

def empty_dict(dict):
    return len(dict) == 0

my_dict = {}
thuk_dict = {'Name': 'Thuc', 'trait': 'Studious - Sincere - Knowledgeable - Kind - Ambitious', 'Appearance':'Handsome','Age':'22'}
if empty_dict(thuk_dict):
    print('Empty dictionary')
else:
    print('Non-empty dictionary')
    