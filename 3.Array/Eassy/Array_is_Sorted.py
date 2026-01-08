#Input : nums = [1, 2, 3, 4, 5]
#Output : true
#Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1],
#  hence it is sorted and we return true.

def is_array_sorted(arr):
    flag=True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            flag=False
            break

    return flag
        

arr = [1, 1,2,  3, 4, 5]
print(is_array_sorted(arr))