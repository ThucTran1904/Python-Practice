'''
Write a Python program to count the number of characters (character frequency) in a string
Sample String : google.com', Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
'''

def characterFreq(s):
    char_freq = {}
    for char in s:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    return char_freq

user_input = input('Enter a string: ')
result = characterFreq(user_input)

print('Character Frequency')
for char, freq in result.items():
    print(f"{char}: {freq}")
