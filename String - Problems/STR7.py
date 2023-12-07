# CONVERTING INTEGER NUMBERS TO ROMAN NUMERALS

dict = {1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M'}
den = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
def int_to_roman(num):
    roman_numeral = ''
    i = 0
    
    while num > 0:
        div = num // den[i]
        num = num % den[i]
        roman_numeral = roman_numeral + dict[den[i]] * div
        i += 1
    
    return roman_numeral

number = 83
result = int_to_roman(number)
print(f"The Roman numeral for {number} is : {result}")

