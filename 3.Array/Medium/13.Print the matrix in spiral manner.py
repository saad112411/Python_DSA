"""
Given an M * N matrix, print the elements in a clockwise spiral manner.
Return an array with the elements in the order of their appearance when printed in a 
spiral manner.
Examples:
Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Explanation:
The elements in the spiral order are 1, 2, 3 -> 6, 9 -> 8, 7 -> 4, 5

"""
def Matrix_by_spiral(matrix):
    row=len(matrix)
    col=len(matrix[0])
    left,right = 0,col-1
    top,bottom = 0,row-1
    result=[]
    while(top<=bottom and left<=right):
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1

        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1

        if (top<=bottom):
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
        bottom-=1

        if (left<=right):
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
        left+=1
    return result

matrix=[[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
print(Matrix_by_spiral(matrix))