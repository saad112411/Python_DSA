"""
Given an array nums of size n and an integer k, find the length of the longest sub-array 
that sums to k. If no such sub-array exists, return 0.
Examples:
Input: nums = [10, 5, 2, 7, 1, 9],  k=15
Output: 4
Explanation:
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15.
 Therefore, the length of this sub-array is 4.
"""
"in this algoritham what we can do we first cheak if the number is "
"greter than that then equl then increase that sum "
def optimal_solution(arr,k):
    n=len(arr)
    left,right=0,0
    current_sum=arr[0]
    max_len=0
    while(right<=n):
        while(left<=right and current_sum>k):
            current_sum-=arr[left]
            left+=1
        if current_sum==k:
            max_len=max(max_len,right-left+1)
        right+=1
        if right<n:
            current_sum+=arr[right]
    if max_len<0:
        return "Your number is not present "
    return max_len
    

nums = [10, 5, 2, 7, 1, 9]
print(optimal_solution(nums,15))