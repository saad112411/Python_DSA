"""
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
"""
# optimal solution 
def rotet_by_90_optimal(matrix):
    #in this solution we follow two steps first transpose then revese that row
    n=len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotet_by_90_optimal(matrix))

# it is the brute force solution  it requred extra space 
def rotet_by_90(matrix):
    n=len(matrix)
    m=len(matrix[0])
    #create a new matrix if we modify the orignal list then it will produce the wrong  result.
    new_matrix=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        index=len(matrix[0])-1
        for j in range(m):
            new_matrix[i][j]=matrix[index][i]
            index-=1
    return new_matrix


#matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#print(rotet_by_90(matrix))