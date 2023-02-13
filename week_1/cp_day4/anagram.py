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
    

# print(anagram_1('charm', 'march') == True)
# print(anagram_1('zach', 'attack') == False)
# print(anagram_1('CharM', 'mARcH') == True)
# print(anagram_1('abcde2', 'c2abed') == True)
# print(anagram_1('Anna Madrigal', 'A man and a girl') == True)


def anagram_2(search_word, list_of_words):
    list_of_anagrams = []
    letter_count = {}
    for char in search_word:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
            
    for word in list_of_words:
        to_check = {}
        for letter in word:
            if letter in to_check:
                to_check[letter] += 1
            else:
                to_check[letter] = 1
        add_word = True
        for key in to_check:
            if key not in letter_count:
                add_word = False
                break
            if to_check[key] != letter_count[key]:
                add_word = False
                pass
        
        if add_word == True:
            list_of_anagrams.append(word)
            
    return list_of_anagrams


print(anagram_2("threads", ["threads", "trashed", "hardest", "hatreds"]) == ["threads", "trashed", "hardest", "hatreds"])
print(anagram_2("apple", ["threads", "trashed", "hardest", "hatreds"]) == [])


# list_1 = [[9],1,2,3,4]
# list_2 = list_1[:]

# list_1[0] = 0

# print(list_1,list_2)

# my_dict = {'a':1}
# other_dict = {'b':1}
# key = 'b'
# if other_dict[key] != my_dict[key]:
#     print('my logic works')