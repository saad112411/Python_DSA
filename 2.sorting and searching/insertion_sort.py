
def insertion_sort(nums):
    n=len(nums)
    for i in range(n):
        
        for j in range(i,n):
            while(j>0 and nums[j-1]>nums[j]):
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1
        
    return nums
                

#nums=[8,7,6,5,4,3,2,1]
#print(insertion_sort(nums))












def insertion(nums):
    for i in range(1,len(nums)):
        for j in range(i,0,-1):
            if nums[j-1]>nums[j]:
                nums[j-1],nums[j]=nums[j],nums[j-1]
            else:
                break

    return nums
#nums=[9,7,6,5,4,3,12,1]
#print(insertion(nums))

def insertion_sort_optimal(arr):
    for i in range(1,len(arr)):
        current=arr[i] 
        j=i
        while(j>0 and arr[j-1]>current):
            arr[j]=arr[j-1]
            j-=1
        arr[j]=current
    return arr

nums=[9,7,6,5,4,3,12,1]
print(insertion_sort_optimal(nums))