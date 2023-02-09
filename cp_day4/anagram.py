def anagram_1(str1, str2):
    set_char = {}
    for i in str1:
        if i == ' ':
            continue
        if isinstance(i, int) and i not in set_char:
            set_char[i] += 1
        if isinstance(i, int) and i in set_char:
            set_char[i] = 1
            
        if isinstance(i, str) and i in set_char:
            set_char[i.lower()] += 1
        if isinstance(i, str) and i not in set_char:
            set_char[i.lower()] = 1
        # print(set_char)
    
    for i in str2:
        # print(set_char)
        if i == ' ':
            continue
        if isinstance(i, int) and i not in set_char:
            set_char[i] -= 1
            
        if isinstance(i, int) and i in set_char:
            set_char[i] = -1
            
            
        if isinstance(i, str) and i.lower() in set_char:
            set_char[i.lower()] -= 1
            
        if isinstance(i, str) and i.lower() not in set_char:
            set_char[i.lower()] = -1
            
    
            
    values = set_char.values()
    
    for i in values:
        if i != 0:
            return False
    
    return True
    

print(anagram_1('charm', 'march') == True)
print(anagram_1('zach', 'attack') == False)
print(anagram_1('CharM', 'mARcH') == True)
print(anagram_1('abcde2', 'c2abed') == True)
print(anagram_1('Anna Madrigal', 'A man and a girl') == True)


