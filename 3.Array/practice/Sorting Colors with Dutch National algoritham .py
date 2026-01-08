"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

# we can solve by this any sorting alogoritham but it cost n(logn) time complexity  min using merge sort

# we can optimize this using dutch national alogo usin O(n) time 
def sorting_colur(arr):
    first=0
    mid=0
    last=len(arr)-1
    for i in arr:
        if arr[mid]==0:
            arr[mid],arr[first]=arr[first],arr[mid]
            mid+=1
            first+=1
        elif arr[mid]==1:
            #correct position 
            mid+=1
        else:
            arr[mid],arr[last]=arr[last],arr[mid]
            last-=1
    return arr


nums = [2,0,2,1,1,0,0]
print(sorting_colur(nums))