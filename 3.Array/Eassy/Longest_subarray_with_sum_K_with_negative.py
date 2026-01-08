#Longest subarray with sum K
#Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. 
#If no such sub-array exists, return 0.
def Longest_sub_arry_optimal(arr,k_Sum):
    right=0 
    left=0
    n=len(arr)
    sum=arr[0]
    max_len=0
    while(right<n):
        while(left<=right and sum>k_Sum):
           sum-=arr[left]
           left+=1

        if sum==k_Sum:
            max_len=max(max_len,right-left+1)

        right+=1
        if right<n:
            sum+=arr[right]
    if max_len<0:
        return 0
    return max_len

arr= [-3, 2, 1,6]
print(Longest_sub_arry_optimal(arr,6))

