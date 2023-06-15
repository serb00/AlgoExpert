# O(l*h) time, where l and h are lenght and height of matrix
# 0(l*h) space
def transposeMatrix(matrix):
    # Write your code here.
    res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res[j][i] = matrix[i][j]
    return res
