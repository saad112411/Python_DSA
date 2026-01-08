"""
Given an array of integers nums, return the value of the largest element in the array
Examples:
Input: nums = [3, 3, 6, 1]
Output: 6
Explanation: The largest element in array is 6
"""
# time comlexity is o(n)
def brute_force_method(arr):
    largest=arr[0]
    for num in arr:
        if largest<num:
            largest=num
    return largest

arr=[3, 3, 6, 1]
print(brute_force_method(arr))