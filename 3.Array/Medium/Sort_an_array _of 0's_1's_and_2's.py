"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.
The sorting must be done in-place, without making a copy of the original array.
Input: nums = [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]
Explanation:
The nums array in sorted order has 2 zeroes, 2 ones and 1 two
"""
#Dutch National Flag problem
#time complexity is O(n)
def Dutch_National_Flag(arr):
    low,mid,high=0,0,len(arr)-1
    while(mid<=high):
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
    

arr = [1, 0, 2, 1, 0]
print(Dutch_National_Flag(arr))

#pythonic Approch
def Sort_one_Two(arr):
    return sorted(arr)

#arr = [1, 0, 2, 1, 0]
#print(Sort_one_Two(arr))
