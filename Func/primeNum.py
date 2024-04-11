'''
- Write a Python function that takes a number as a parameter and check the number is prime or not
'''

def is_prime(num):
    if num < 2:
        return False
    for n in range(2, int(num**0.5) +1 ):
        if num % n == 0:
            return False
    return True

print(is_prime(11))
print(is_prime(8))