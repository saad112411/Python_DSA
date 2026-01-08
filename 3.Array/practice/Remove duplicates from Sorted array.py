def removeDuplicates(nums):
    length=len(nums)-1
    k=len(set(nums))-1
    new_list=[0]*k
    for i in range(length):
        if nums[i]!=nums[i+1]:
            new_list.append(nums[i])
    return new_list,k


nums=[1,1,2]
print(removeDuplicates(nums))