def to_roman(num):
    roman = ""
    roman_dict = {
        'M' : 1000,
        'XM' : 990,
        'LM' : 950,
        'CM' : 900,
        'D' : 500,
        'LD' : 450,
        'CD' : 400,
        'C' : 100,
        'XC' : 90,
        'L' : 50,
        'XL' : 40,
        'X' : 10,
        'IX' : 9,
        'V' : 5,
        'IV' : 4,
        'I' : 1
    }
    
    for key, value in roman_dict.items():
        # print(f'Roman {key} has {value} value')
        while num >= value:
            num -= value
            roman += key
        
    return roman
print(to_roman(4))
print(to_roman(9))
print(to_roman(14))
print(to_roman(44))
print(to_roman(944))
