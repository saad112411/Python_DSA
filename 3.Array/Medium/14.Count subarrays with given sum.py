"""
Given an array of integers nums and an integer k, return the total number of subarrays 
whose sum equals to k.
Examples:
Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: In the given array [1, 1, 1],
there are two subarrays that sum up to 2: [1, 1] and [1, 1]. Hence, the output is 2.
"""
def subarr_with_sum_optimal(arr):
    left,right=0,0
    while(right<n):
        while(left<=right):
            pass
            

nums = [1, 1, 1]
k = 2
print(subarr_with_sum_optimal(nums,k))


def Subarr_with_given_sum_brute_force(arr,k):
    count=0
    n=len(arr)
    current_sum=0

    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum+=arr[j]
            if current_sum==k:
                count+=1            
    return count

#arr = [1, 1, 1]
#print(Subarr_with_given_sum_brute_force(arr,2))