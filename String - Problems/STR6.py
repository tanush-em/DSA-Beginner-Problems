# DIVISIBILITY BY 7
# The concept is that any number of the form (10a+b) is divisible by 7 only is (a-2b) is divisible by 7

def isDivisible(num):
    if num < 0:
        return 
    elif num == 0 or 7:
        return True
    elif num <= 10:
        return False
    else:
        return isDivisible(num//10 - 2*(num%10))
    
num = 343
if isDivisible(num):
    print("It is divisible")
else:
    print("It is not divisible")