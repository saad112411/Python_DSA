"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending 
position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

 Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

"""

def searchRange(nums,target):
    def find_first(nums,target):
            n=len(nums)
            low=0
            high=n-1
            first=-1
            while(low<=high):
                mid=(low+high)//2
                if nums[mid]==target:
                    first=mid
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return first 

    def find_last(nums,target):
        n=len(nums)
        low=0
        high=n-1
        last=-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last
    first=find_first(nums,target)
    if first==-1:
        return [-1,-1]
    last=find_last(nums,target)
    return [first,last]


nums = [5,7,7,8,8,10]
print(searchRange(nums,8))        
    



        