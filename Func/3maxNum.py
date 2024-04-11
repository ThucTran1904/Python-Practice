'''
- Write a Python function to find the Max of three numbers
'''

def find_max_3_num(num1, num2, num3):
    max_num = max(num1, num2, num3)
    return max_num

a = 30
b = 9
c = 2004
print(find_max_3_num(a, b, c))