'''
- Write a Python function to check whether a number is in a given range
'''

def in_range(start, end, number):
    return start <= number <= end

user_input = float(input('Please enter a number: '))
lower_bound = 0
upper_bound = 1000

if in_range(lower_bound, upper_bound, user_input):
    print(f'The number {user_input} is in the range {lower_bound} to {upper_bound}')
else:
    print(f'The number {user_input} is not in the range {lower_bound} to {upper_bound}')