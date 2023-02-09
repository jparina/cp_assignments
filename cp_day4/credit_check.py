import functools

def digit_sum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = int((num - digit) / 10)
    return sum
    


def credit_check(str):
    list_nums = list(map(int, list(str)))
    
    for i in range(0, len(list_nums), 2):
        list_nums[i] *= 2 
    
    for num in range(len(list_nums)):
        if list_nums[num] > 9:
            list_nums[num] = digit_sum(list_nums[num])
            
    
    list_of_nums_sum = functools.reduce(lambda agg, num : agg + num, list_nums)
    return list_of_nums_sum % 10 == 0

print(credit_check('5541808923795240'))

