'''
- Write a Python program to store a given dictionary in a json file
'''

import json 

thuk_dict = {'Name': 'Thuc', 'trait': 'Studious - Sincere - Knowledgeable - Kind - Ambitious', 'Appearance':'Handsome','Age':'22','Finance':'Wealthy'}
file_name = 'thuc_dict.json'
with open(file_name, 'w') as json_file:
    json.dump(thuk_dict, json_file, indent=4)

print(f"Dictionary saved to '{file_name}' successfully ")
