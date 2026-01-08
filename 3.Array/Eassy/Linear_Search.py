"""
Input: nums = [2, 3, 4, 5, 3], target = 3
Output: 1
Explanation:
The first occurence of 3 in nums is at index 1
"""

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    
    return -1


arr= [0,2, 3, 4, 5, 3]
target=int(input("Enter a targeted Element :"))
print(linear_search(arr,target))