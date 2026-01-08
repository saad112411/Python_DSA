"""
Given an integer array nums  of positive and negative 
integers.Return the answer array in such a way that the given conditions are met:
Every consecutive pair of integers have opposite signs.
if pairs are not there then print remaing element and preserve the index 
Examples:
Input : nums = [2, 4, 5, -1, -3, -4,-5,-6]
Output : [2, -1, 4, -3, 5, -4,-5,-6]
"""
def optimal_solution(arr):
    n=len(arr)
    pos_arr=[]
    neg_arr=[]
    for i in range(n):
        if arr[i]>-1:
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])
    My_list=[0]*len(arr)
    len_pos=len(pos_arr)
    len_neg=len(neg_arr)
    if len_pos<=len_neg:
        for i in range(len_pos):
            My_list[i*2]=pos_arr[i]
            My_list[i*2+1]=neg_arr[i]
        Index=len_pos*2
        for i in range(len_pos,len_neg):
            My_list[Index]=neg_arr[i]
            Index+=1
    else:
        for i in range(len_neg):
            My_list[i*2]=pos_arr[i]
            My_list[i*2+1]=neg_arr[i]
        Index=len_neg*2
        for i in range(len_neg,len_pos):
            My_list[Index]=pos_arr[i]
            Index+=1
    return My_list

            

nums = [2, 4, 5, -1, -3, -4,-5,-6]
print(optimal_solution(nums))

