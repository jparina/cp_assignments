# returns factorial of num passed as arg
def factorial(num):
    if num == 0: return 1
    return num * factorial(num-1)
                           
print(factorial(25))