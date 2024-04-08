'''
-Write a Python program to remove a key from a dictionary
'''

def remove_key(dict, key):
    removed_key = dict.pop(key, None)
    if removed_key is not None: 
        print(f"Key '{key}' removed successfully. value: '{removed_key}'")
    else:
        print(f"Key '{key}' does not exist in the dictionary")
        
thuk_dict = {'Name': 'Thuc', 'trait': 'Studious - Sincere - Knowledgeable - Kind - Ambitious', 'Appearance':'Handsome','Age':'22'}
remove_key(thuk_dict, 'Hobby')
print("Updated Dict:", thuk_dict)
