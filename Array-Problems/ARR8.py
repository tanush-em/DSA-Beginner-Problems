# MISSING NUMBER IN ARRAY

def missingno(arr,n):
    sum1 = 0
    for i in arr:
        sum1 = sum1 + i
    sum2 = (n*(n+1))/ 2
    return(sum2-sum1)

arr = [5,6,7,3,4,1,2,8,10]
n = 10

print(f"The missing number from the array is {int(missingno(arr,n))}")