"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""
def spiral_matrix(arr):
    len_row=len(arr)
    len_col=len(arr[0])
    left,right = 0,len_col-1
    top,bottom = 0,len_row-1
    result=[]
    while(top<=bottom and left<=right):
        for i in range(left,right+1):
            result.append(arr[left][i])
        
        top+=1
        for i in range(top,bottom+1):
            result.append(arr[i][right])
        
        right-=1
        if(left<=right):
            for i in range(right,left-1,-1):
                result.append(arr[bottom][i])

        bottom-=1
        if (top<=bottom):
            for i in range(bottom,top-1,-1):
                result.append(arr[i][left])
        left+=1
    return result
            




matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(matrix))