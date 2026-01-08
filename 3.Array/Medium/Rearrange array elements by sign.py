"""
Given an integer array nums of even length consisting of an equal number of positive and negative 
integers.Return the answer array in such a way that the given conditions are met:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Examples:
Input : nums = [2, 4, 5, -1, -3, -4]
Output : [2, -1, 4, -3, 5, -4]
Explanation:
The positive number 2, 4, 5 maintain their relative positions and -1, -3, -4 maintain their 
relative positions
"""
def Rearrange_element(arr):
    n=len(arr)
    positve_arr=[]
    negative_arr=[]
    for i in range(n):
        if arr[i]>-1:
            positve_arr.append(arr[i])
        else:
            negative_arr.append(arr[i])
    new_arr=[]
    for i in range(n//2):
        new_arr.append(positve_arr.pop(0))
        new_arr.append(negative_arr.pop(0))
    return new_arr

#arr=[2, 4, -1, 5, -3, -4]
#print(Rearrange_element(arr))

def Rearrange_best_method(arr):
    n=len(arr)
    positve_arr=[]
    negative_arr=[]
    for i in range(n):
        if arr[i]>-1:
            positve_arr.append(arr[i])
        else:
            negative_arr.append(arr[i])
    for i in range(n//2):
        arr[i*2]=positve_arr[i]
        arr[i*2+1]=negative_arr[i]
    return arr

#arr=[2, 4, -1, 5, -3, -4]
#print(Rearrange_best_method(arr))

def rearrange_optimal_solu(arr):
    n=len(arr)
    new_arr=[0]*len(arr)
    positive=0
    negative=1
    for i in range(n):
        if arr[i]<0:
            new_arr[negative]=arr[i]
            negative+=2
        else:
            new_arr[positive]=arr[i]
            positive+=2
    return new_arr

#arr=[2, 4, -1, 5, -3, -4]
#print(rearrange_optimal_solu(arr))


