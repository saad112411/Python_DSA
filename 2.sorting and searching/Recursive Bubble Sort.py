"""
Given an array of integers nums, sort the array in non-decreasing order using the recursive
Bubble Sort algorithm, and return the sorted array.
You must implement Bubble Sort using recursion only.
Do not use built-in sorting functions (sort, sorted, Arrays.sort, etc.).
A sorted array in non-decreasing order is an array where each element is greater than or 
equal to the previous one.

Example 1
Input: nums = [7, 4, 1, 5, 3]
Output: [1, 3, 4, 5, 7]
Explanation: 1 <= 3 <= 4 <= 5 <= 7.
Thus the array is sorted in non-decreasing order.
"""

def recursive_buble_sort(arr):
    pass


nums = [7, 4, 1, 5, 3]
print(recursive_buble_sort(nums))



def buble_sort(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
               count+=1
        if count == 0:
            return arr
    return arr

