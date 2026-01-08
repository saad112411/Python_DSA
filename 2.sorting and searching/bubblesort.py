def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        swapped = False
        for j in range(1,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
        if not swapped:
            break
    return nums
nums=[1,2,7,4,2]
#print(bubble_sort(nums))


def bubble(nums):
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)-1-i):# at each step it will sort from right side 
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                count+=1
        if count==0:
            return nums
    return nums
print(bubble(nums))