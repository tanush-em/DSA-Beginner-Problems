# CHECK WHETHER TWO STRINGS ARE ANAGRAM OF EACH OTHER

def is_anagram(str1,str2):
    
    str1 = str1.replace(" ",'').lower()
    str2 = str2.replace(" ",'').lower()
    
    if len(str1) != len(str2):
        return False
    
    hashmap_str1 = {}
    hashmap_str2 = {}
    
    for char in str1:
        if char in hashmap_str1:
            hashmap_str1[char] = hashmap_str1[char] + 1
        else:
            hashmap_str1[char] = 1
            
    for char in str2:
        if char in hashmap_str2:
            hashmap_str2[char] = hashmap_str2[char] + 1
        else:
            hashmap_str2[char] = 1
            
    if hashmap_str1 == hashmap_str2:
        return True
    return False
    
str1 = "Listen"
str2 = "Silent"
if is_anagram(str1,str2):
    print("They are anagrams")
else:
    print("The are not anagrams")
    
    