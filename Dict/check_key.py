'''
- Write a Python script to check whether a given key already exists in a dictionary
'''

def key_exists(dict, key):
    return key in dict
thuk_dict = {'Name': 'Thuc', 'trait': 'Studious - Sincere - Knowledgeable - Kind - Ambitious', 'Appearance':'Handsome','Age':'22'}
search_key = 'age'
if key_exists(thuk_dict, search_key):
    print(f'{search_key} already exists in the dictionary')
else:
    print(f'{search_key} does not exist in the dictionary')