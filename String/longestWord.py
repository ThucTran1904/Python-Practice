'''
Write a Python function that takes a list of words and returns the longest word and the length of the longest one

'''

def find_longest_word(words):
    longest_world = max(words, key=len)
    return longest_world, len(longest_world)

words = ['i','love', 'Diu Thao','more','than','i','can','say']
longest, length = find_longest_word(words)
print(f'Longest word is {longest}, with the length {length}')