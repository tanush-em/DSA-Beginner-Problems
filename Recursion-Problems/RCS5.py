# FACTORIAL OF A NUMBER USING RECURSION

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        return
    else:
        return (n * factorial(n-1))

n = 5
print(f"The factorial of {n} is {factorial(5)}")   