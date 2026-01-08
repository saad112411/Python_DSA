"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
"""
def movese_zeros_to_last(arr):
    n=len(arr)
    j=0
    for i in range(n):
        if arr[i]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr


nums=[1,1,11,0,1,0,3,12]
print(movese_zeros_to_last(nums))
