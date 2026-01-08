"""
Given an integer array nums, return a list of all the leaders in the array.
A leader in an array is an element whose value is strictly greater than all elements to
its right in the given array. The rightmost element is always a leader.
The elements in the leader array must appear in the order they appear in the nums array.
Examples:
Input: nums = [1, 2, 5, 3, 1, 2]
Output: [5, 3, 2]
Explanation:
2 is the rightmost element, 3 is the largest element in the index range [3, 5],
5 is the largest element in the index range [2, 5]
"""
def Leader_in_arry(arr):
    n=len(arr)
    My_list=[]
    right_most_elem=arr[n-1]
    My_list.append(right_most_elem)
    for i in range(n-2,-1,-1):
        if arr[i]>right_most_elem:
            My_list.append(arr[i])
            right_most_elem=arr[i]
    My_list.reverse()
    return My_list

arr=[10, 10, 5, 2]
print(Leader_in_arry(arr))