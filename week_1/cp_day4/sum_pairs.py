def sum_pairs(array_nums, needed_sum):
    array_of_pairs = []
    repeat_check = set()
    sum_map = {}
    i = 0
    
    while i < len(array_nums):
        sum_map[array_nums[i]] = i
        i += 1
    print(sum_map)
    for i in range(len(array_nums)):
        pair = []
        num_to_find = needed_sum - array_nums[i]
        
        if num_to_find in sum_map and num_to_find not in repeat_check and array_nums[i] not in repeat_check:
            repeat_check.add(array_nums[i])
            repeat_check.add(num_to_find)
            pair = [array_nums[i], num_to_find]
            
        if len(pair) == 2:
            array_of_pairs.append(pair)
        
    return array_of_pairs
    
    
print(sum_pairs([1,2,3,4,5], 7))