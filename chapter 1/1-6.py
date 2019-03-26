# w, h = 5, 5
# Matrix = [[1 + x + y * 8 for x in range(w)] for y in range(h)]
# print(Matrix)
# Matrix[2][3] = 1000
# print(Matrix)
import math


def rotateMatrix(n, Matrix):
    for i in range(n):
        for j in range(i, n):
            temp = Matrix[i][j]
            Matrix[i][j] = Matrix[j][i]
            Matrix[j][i] = temp
    for i in range(math.ceil(n / 2)):
        for j in range(n):
            temp = Matrix[i][j]
            Matrix[i][j] = Matrix[n - 1 - i][j]
            Matrix[n - 1 - i][j] = temp


def rotateMatrix2(n, Matrix):
    for i in range(math.floor(n / 2)):
        first = i
        last = n - i - 1
        for j in range(first, last):
            temp = Matrix[i][j]
            Matrix[i][j] = Matrix[j][last]
            Matrix[j][last] = Matrix[last][n - j - 1]
            Matrix[last][n - j - 1] = Matrix[n - j - 1][i]
            Matrix[n - j - 1][i] = temp


n = 4
Matrix = [[1 + x + y * n for x in range(n)] for y in range(n)]
rotateMatrix2(4, Matrix)
print(Matrix)
