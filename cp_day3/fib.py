# checks whether argument is a fib num and/or which fib number it is
def is_fib(num_to_check):
    if num_to_check == 0: 
        which_fib = 0
        return which_fib
        # return True
    prev = 1
    double_prev = 0
    which_fib = 1
    if (int(num_to_check) != num_to_check or num_to_check < 0):
        return -1
        # return False
    while prev <= num_to_check:
        
        if prev == num_to_check:
            return which_fib
            # return True
        temp = prev
        prev += double_prev
        double_prev = temp
        which_fib += 1
    # return False
    return -1
        
# print(is_fib(0))
# print(is_fib(21))
# print(is_fib(6))
# print(is_fib(1))
# print(is_fib(13))

# Find the nth fib number
def fib_memo(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0: return 0
    if n <= 2: return 1
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
    
print(fib_memo(1))
print(fib_memo(2))
print(fib_memo(3))
print(fib_memo(5))
print(fib_memo(8))
print(fib_memo(13))
print(fib_memo(21))