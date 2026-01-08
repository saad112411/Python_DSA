"""
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k.
If no such sub-array exists, return 0.
Examples:
Input: nums = [10, 5, 2, 7, 1, 9],  k=15
Output: 4
Explanation:
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], 
which has a length of 4. This sub-array starts at index 1 and ends at index 4, 
and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.
"""

# Metheod 1 Brute Force 
def Longest_sub_arry_bruteForce(arr,sum):
    lenth=0
    n= len(arr)
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if s==sum:
                lenth=max(lenth,j-i+1)
    return lenth

#arr= [1,2,3,4,5,4,5,7,1,1,1]
#print(Longest_sub_arry_bruteForce(arr,3))

#optimal soution 
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


arr= [1,2,1,4,5,4,5,2,1,1,1]
print(Longest_sub_arry_optimal(arr,5))