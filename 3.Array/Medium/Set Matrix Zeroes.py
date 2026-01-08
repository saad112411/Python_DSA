"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0.
You must do it in place.
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation:
Element at position (1,1) is 0, so set entire row 1 and column 1 to 0.
"""
#brute Force Method
def set_matrix_to_zoro(martix):
    n=len(matrix)
    m=len(matrix[0])
    row=set()
    column=set()
    for i in range(n):
        for j in range(m):
            if martix[i][j]==0:
                row.add(i)
                column.add(j)
    for i in range(n):
        for j in range(m):
            if i in row or j in column:
                matrix[i][j]=0
          
    return matrix



matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_matrix_to_zoro(matrix))