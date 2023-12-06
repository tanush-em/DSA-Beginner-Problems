# SEARCH AN ELEMENT IN AN ARRAY

def linear_search(arr, key):
    i = 0
    for i in range(len(arr)):
        if arr[i] == key:
            return i+1
    return -1

arr = [1,8,3,7,6,4,38,17]
key = 9

if linear_search(arr,key) != -1:
    print(f"The element is found at position {linear_search(arr,key)} in the array")
else:
    print("The element is not found in the array")
