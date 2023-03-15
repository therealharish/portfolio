arr = [[1,2,3], [4,5,6], [7,8,9]]
row = len(arr)
col = len(arr[0])

# make a python program to rotate this matrix such that each element is shifted by one place in a clockwise manner only outer elements
def rotateClockWiseOne(arr, row, col):
    temp = arr[0][col - 1]
    for i in range(col - 1, 0, -1):
        arr[0][i] = arr[0][i - 1]
    
    temp2 = arr[row - 1][col - 1]
    for i in range(row - 1, 0, -1):
        arr[i][col - 1] = arr[i - 1][col - 1]
    arr[1][col - 1] = temp
    
    temp = arr[row - 1][0]
    for i in range(col - 1):
        arr[row - 1][i] = arr[row - 1][i + 1]
    arr[row - 1][col - 2] = temp2
    
    for i in range(row - 1):
        arr[i][0] = arr[i + 1][0]
    arr[row - 2][0] = temp
    
def printMatrix(arr):
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end = " ")
        print()
    
rotateClockWiseOne(arr, row, col)
printMatrix(arr)
