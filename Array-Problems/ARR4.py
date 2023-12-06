# TRANSPOSE OF A MATRIX

def transpose(mat1,n):
    mat2 = []
    for i in range(n):
        mat2.append([0]*n)
    
    for i in range(0,n):
        for j in range(0,n):
            mat2[j][i] = mat1[i][j]
    
    print(mat2)

mat = [[1,2],[3,4]]
n = 2
transpose(mat,2)