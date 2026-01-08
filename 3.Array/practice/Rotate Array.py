"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
def rotet_an_array(nums,k):
    length=len(nums)-k
    first_half=nums[:length]
    second_half=nums[length:]
    return second_half+first_half
    
#print(rotet_an_array(nums,k))

def optiml_solution(nums,k):
    n=len(nums)
    k=k%n
    nums.reverse()
    nums[:k]=reversed(nums[:k])
    nums[k:]=reversed(nums[k:])
    return nums 

nums=[1,2,3,4,5,6,7]
print(optiml_solution(nums,k=31))