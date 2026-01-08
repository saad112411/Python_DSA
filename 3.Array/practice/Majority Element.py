"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
Example 1:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
#Boyer-Moore Voting Algorithm
def majority_element(arr):
    maj_ele=(len(arr)/2)+1
    current_element=arr[0]
    count=0
    for i in range(len(arr)):
        if count==0:
            current_element=arr[i]
        if current_element==arr[i]:
            count+=1
        else:
            count-=1
    return current_element

nums= [2,2,1,1,1,2,2]
print(majority_element(nums))
