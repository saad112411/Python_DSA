"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
def Maximum_subarray(arr):
    max_sum=arr[0]
    current_sum=0
    for i in range(len(nums)):
        if current_sum<0:
            current_sum=0
            
        current_sum+=arr[i]
        max_sum=max(max_sum,current_sum)
    return max_sum



nums=[-2,1,-3,4,-1,2,1,-5,4]
print(Maximum_subarray(nums))
    