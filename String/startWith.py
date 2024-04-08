'''
- Write a Python program to check whether a string starts with specified characters

'''

def starts_with(string, prefix):
    """
    Checks if a string starts with the specified prefix.

    Args:
        string (str): The input string.
        prefix (str): The prefix to check.

    Returns:
        bool: True if the string starts with the prefix, else False.
    """
    return string.startswith(prefix)

# Example usage:
user_string = input("Enter a string: ")
user_prefix = input("Enter the prefix to check: ")

if starts_with(user_string, user_prefix):
    print(f"The string '{user_string}' starts with '{user_prefix}'.")
else:
    print(f"The string '{user_string}' does not start with '{user_prefix}'.")