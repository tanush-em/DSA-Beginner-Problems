# ROTATE MATRIX BY 90 DEGREES - incomplete

def rotate90(mat,r,c):
    mat1 = []
    for i in range(c):
        mat1.append([0]*r)
        
    for i in range(0,r):
        for j in range(0,c):
            mat[i][j] = mat1[j][r-i-1]
    
    print(mat1)
    
mat = [[11,12,13],[21,22,23],[31,32,33]]
rotate90(mat,3,3)