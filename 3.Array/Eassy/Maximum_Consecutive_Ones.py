"""
Given a binary array nums, return the maximum number of consecutive 1s in the array.
A binary array is an array that contains only 0s and 1s.
Examples:
Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
Output: 3
Explanation:
The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s
"""

def Consecutive_number(arry):
    current_count=0
    max_count=0

    for i in arry:
        if i==1:
            current_count+=1
        else:
           max_count=max(max_count,current_count)
           current_count=0
    return max(max_count,current_count)    

arr=[1, 1, 0, 0, 1, 1, 1, 0]
print(Consecutive_number(arr))
