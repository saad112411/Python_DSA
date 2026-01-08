#Input: nums = [7, 4, 1, 5, 3]
#Output: [1, 3, 4, 5, 7]
def selection_sort(nums):
    n=len(nums)
    for i in range(n-1):
        minimum=i
        for j in range(i,n):
            if nums[j]<nums[minimum]:
                minimum=j
        nums[i],nums[minimum]=nums[minimum],nums[i]
    return nums
nums=[7, 4, 1, 5, 3]
#print(selection_sort(nums))


def selection(arr):
    for i in range(len(arr)):
        minimum=i
        for j in range(i,len(arr)):
            if arr[j]<arr[minimum]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]
    return arr

print(selection(nums))