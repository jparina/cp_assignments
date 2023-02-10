def char_count(phrase):
    
    char_dict = {}
    for char in phrase:
        if char == ' ':
            continue
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    sorted_char_dict = sorted(char_dict.items(),key=lambda x: (-x[1], x[0]))
    sorted_char_dict = list(map(list, sorted_char_dict))
    return sorted_char_dict

print(char_count("aaabbc"))
print(char_count("an apple a day will keep the doctor away"))
