"""
Given an array nums of n integers.
Return the length of the longest sequence of consecutive integers. The integers in this sequence
can appear in any order.
Examples:

Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation:
The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which has a length of 4.
This sequence can be formed regardless of the initial order of the elements in the array.

Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9
Explanation:
The longest sequence of consecutive elements in the array is [0, 1, 2, 3, 4, 5, 6, 7, 8], 
which has a length of 9. 
"""
#we can solve this by sorting and find the diffrence and create a varaible to count 
# the longest subsequnce 

# the given code time complexity is O(n) only 
def Longest_seq_count(arr):
    new_arr=set(arr)
    max_len=0
    for i in new_arr:
        if (i-1) not in new_arr:
            Current_count=1

            while(i+Current_count) in new_arr:
                Current_count+=1
            max_len=max(max_len,Current_count)
    return max_len

arr= [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Longest_seq_count(arr))



# time complexity is O(nlog(n)) but we can optimize to O(n) using set methed 
def brute_force(arr):
    n=len(arr)
    arr.sort()
    count=1
    max_count=1
    for i in range(n-1):
        if arr[i+1]-arr[i]==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=1
    return max_count

#arr=[1,11,21,31,34,65]
#print(brute_force(arr))

#arr1= [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#print(brute_force(arr1))