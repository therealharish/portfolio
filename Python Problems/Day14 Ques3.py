# fill in missing entries of a magic square
mat = [[0,7,6], [9,0,1], [4,3,0]]


def magicSquare(mat):
  
    sum1 = sum(mat[0]) 
    sum2 = sum(mat[1])
    sum3 = sum(mat[2])

    mat[1][1] = ((sum1 - sum2) + sum3) // 2
    mat[0][0] = sum3 - mat[1][1]
    mat[2][2] = sum1 - mat[1][1]

    for i in range(3):
        for j in range(3):
            print(mat[i][j], end=" ")
        print()
    
magicSquare(mat)