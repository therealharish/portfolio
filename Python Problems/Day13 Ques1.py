arr = [[1,2,3], [4,5,6], [7,8,9]]
row = len(arr)
col = len(arr[0])

def checkIfLowerTriangular(arr, row, col):
    for i in range(row):
        for j in range(col):
            if i < j and arr[i][j] != 0:
                return False
    return True

def makeLowerTriangular(arr, row, col):
    for i in range(row):
        for j in range(col):
            if i < j:
                arr[i][j] = 0
                
def printMatrix(arr):
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end = " ")
        print()
                
if checkIfLowerTriangular(arr, row, col):
    print(arr)
else:
    makeLowerTriangular(arr, row, col)
    printMatrix(arr)