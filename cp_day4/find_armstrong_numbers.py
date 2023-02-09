# finds armstrong number given an array of digits
def armstrong_helper(array):
    sum = 0
    for num in  array:
        sum += num ** len(array)
    return sum
    
def find_armstrong_numbers(num):
    ans = []
    for i in range(num+1):
        
        digits = []
        for char in str(i):
            digits.append(int(char))
        # print(digits)
        armstrong = armstrong_helper(digits)
        # print(i, armstrong)
        if armstrong == i:
            ans.append(i)
    return ans

# given a number n, determine if it's an armstrong number
def useful_armstrong(n):
    num_to_array = list(map(int , list(str(n))))
    
    

# print(find_armstrong_numbers(999))
# print(armstrong_helper([3,7,1]))

useful_armstrong(954)