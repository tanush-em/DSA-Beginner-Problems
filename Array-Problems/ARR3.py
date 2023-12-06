# WAVE ARRAY

def wavify(arr):
    i = 0
    j = 1
    arr.sort()
    while j < len(arr):
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 2
        j = j + 2
    print(arr)

arr = [1,2,3,4,5]
wavify(arr)              