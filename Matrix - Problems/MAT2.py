# MAXIMUM ELEMENT OF EACH ROW IN A MATRIX

def greatest_in_row(arr):
    temp = arr[0]
    for i in range(0,len(arr)):
        if arr[i] > temp:
            temp = arr[i]
        else:
            continue
    return temp

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

for i in range(len(mat)):
    print(f"The greatest element in row {i+1} is {greatest_in_row(mat[i])}")
    