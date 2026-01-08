"""
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums 
such that they add up to target.
Each input will have exactly one solution, and the same element cannot be used twice.
 Return the answer in increasing order.
 
Input: nums = [1, 3, 5, -7, 6, -3], target = 0
Output: [1, 5]
Explanation:
nums[1] + nums[5] = 3 + (-3) = 0
 """

#brute Force
def Two_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i]+arr[j]==target:
                return [i,j]
    return False


arr=[1, 3, 5, -7, 6, -3]
print(Two_sum(arr,0))

