# REVERSE WORDS IN A STRING

def rev_words(input_str):
    rev_str = []
    words = input_str.split()  
    for i in range(len(words) - 1, -1, -1):  
        rev_str.append(words[i])  
    reversed_string = " ".join(rev_str)  
    return reversed_string

input_str = "I love pizza very much"
print(f"The string when the words are reversed is '{rev_words(input_str)}'")