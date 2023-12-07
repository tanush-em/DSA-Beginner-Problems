# PRINT REVERSE OF A STRING USING RECURSION

def rev_string(str,l):
    if l >= 0:  
        print(str[l], end=' ')
        rev_string(str,l-1)
    else:
        return
    
str = "Tanush"
l = len(str)-1
rev_string(str,l)