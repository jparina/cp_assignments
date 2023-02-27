def factorial(x):
    if x == 1: return 1
    return x * factorial(x-1)

import re
def palindrome(string): # "A man, a plan, a canal: Panama" ------- "race a car"
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
    if len(cleaned_string) <= 1:
        return True
    if cleaned_string[0] != cleaned_string[len(cleaned_string) - 1]:
        print(cleaned_string[0])
        print(cleaned_string[len(cleaned_string) - 1])
        return False
    return palindrome(cleaned_string[1:-1])

