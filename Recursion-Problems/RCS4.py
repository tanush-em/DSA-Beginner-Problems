# SUM OF DIGITS OF A NUMBER USING RECURSION

def digit_sum(num, sum):
    if num > 0:
        sum = sum + num%10
        return(digit_sum(num//10,sum))
    else:
        return sum
    
num = 12345
sum = 0
print(digit_sum(num,sum))