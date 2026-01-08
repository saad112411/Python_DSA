"""
Given an integer array nums  of positive and negative 
integers.Return the answer array in such a way that the given conditions are met:
Every consecutive pair of integers have opposite signs.
if pairs are not there then print remaing element and preserve the index 
Examples:
Input : nums = [2, 4, 5, -1, -3, -4,-5,-6]
Output : [2, -1, 4, -3, 5, -4,-5,-6]
"""
def rearrange_element(arr):
    n=len(arr)
    positive=[]
    negative=[]
    for i in range(n):
        if arr[i]<0:
            negative.append(arr[i])
        else:
            positive.append(arr[i])

    new_arr=[0]*len(arr)
    len_pos=len(positive)
    len_neg=len(negative)
    if len_pos<=len_neg:
        for i in range(len_pos):
            new_arr[i*2]=positive[i]
            new_arr[i*2+1]=negative[i]
        index=len_pos*2
        for i in range(len_pos,len_neg):
            new_arr[index]=arr[i]
            index+=1
    else:
        for i in range(len_neg):
            new_arr[i*2]=positive[i]
            new_arr[i*2+1]=negative[i]
        index=len_neg*2
        for i in range(len_neg,len_pos):
            new_arr[index]=arr[i]
            index+=1
    return new_arr

arr=[2, 4, 5, -1, -3, -4,-5,-6]
print(rearrange_element(arr))