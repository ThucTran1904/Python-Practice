'''
- Write a Python script to merge two Python dictionaries
'''

def merge_two_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result
    
thuk_dict = {'Name': 'Thuc', 'trait': 'Studious - Sincere - Knowledgeable - Kind - Ambitious', 'Appearance':'Handsome','Age':'22'}
dict1 = {'a': 10, 'b': 8}
merged_dict = merge_two_dicts(thuk_dict, dict1)
print('Merged dic', merged_dict)


